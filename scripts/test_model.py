import os
import sys

import sentencepiece as spm
import tensorflow.keras as keras

model = keras.models.load_model(os.path.join(sys.argv[1], "model_best.h5"))
sp = spm.SentencePieceProcessor()
sp.load(os.path.join(sys.argv[1], "sp.model"))


def preprocess(texts, maxlen=300):
    return keras.preprocessing.sequence.pad_sequences(
        [sp.EncodeAsIds(text) for text in texts],
        maxlen=maxlen)


test_data = [
    "まじきもい、あいつ", "今日は楽しい一日だったよ", "ペットが死んだ、実に悲しい", "ふざけるな、死ね", "ストーカー怖い",
    "すごい！ほんとに！？", "葉は植物の構成要素です。", "ホームレスと囚人を集めて革命を起こしたい",
    "ファイナルファンタジーは面白い",
    "クソゲーはつまらん"
]

targets = preprocess(test_data)
emos = ["happy", "sad", "angry", "disgust", "surprise", "fear"]
for i, (ds, text) in enumerate(zip(model.predict(targets), test_data)):
    print('\t'.join(emos))
    print(text)
    print('\t'.join([str(round(100.0 * d)) for d in ds]))
