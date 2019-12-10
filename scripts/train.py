import os
import sys
import pandas as pd
from sklearn.utils import shuffle
import sentencepiece as spm
from tensorflow.keras.layers import Dense, Embedding, GRU
from tensorflow.keras.layers import SpatialDropout1D
from tensorflow.keras.layers import SeparableConv1D, MaxPooling1D
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.preprocessing.sequence import pad_sequences

sp = spm.SentencePieceProcessor()
sp.Load(os.path.join(sys.argv[1], "sp.model"))


def load(trainfile):
    df = shuffle(pd.read_csv(trainfile))
    df_train = df.iloc[:-1000]
    df_valid = df.iloc[-1000:]
    X_train = preprocess(df_train["text"])
    y_train = df_train["label"].astype(int).to_numpy()
    X_valid = preprocess(df_valid["text"])
    y_valid = df_valid["label"].astype(int).to_numpy()
    return X_train, X_valid, y_train, y_valid


def preprocess(texts, maxlen=300):
    return pad_sequences([sp.EncodeAsIds(text) for text in texts],
                         maxlen=maxlen)


def build_model(max_features=8000,
                max_len=300,
                dim=200,
                gru_size=100,
                dropout_rate=0.2,
                outsize=6):
    model = Sequential([
        Embedding(max_features + 1, dim, input_length=max_len),
        SpatialDropout1D(dropout_rate),
        SeparableConv1D(32, kernel_size=3, padding='same', activation='relu'),
        MaxPooling1D(pool_size=2),
        SeparableConv1D(64, kernel_size=3, padding='same', activation='relu'),
        MaxPooling1D(pool_size=2),
        GRU(gru_size),
        Dense(outsize, activation='sigmoid', kernel_initializer='normal')
    ])
    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer='nadam',
                  metrics=['accuracy'])
    return model


def main():
    callbacks = [
        ModelCheckpoint(os.path.join(sys.argv[1], "model_best.h5"),
                        save_best_only=True,
                        monitor='val_loss',
                        mode='min')
    ]
    X_train, X_valid, y_train, y_valid = load(
        os.path.join(sys.argv[1], "tweets_fixed.csv"))
    epochs = 10
    batch_size = 1000
    model = build_model()
    model.fit(X_train,
              y_train,
              validation_data=(X_valid, y_valid),
              epochs=epochs,
              batch_size=batch_size,
              verbose=1,
              callbacks=callbacks)
    model.save(os.path.join(sys.argv[1], "model_last.h5"))


if __name__ == "__main__":
    main()
