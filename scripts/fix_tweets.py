import pandas as pd
import random
import sys
import os


def fix(df):
    min_size = min(df[df["label"] == i].shape[0] for i in range(6))
    dfs = []
    for i in range(6):
        tdf = df[df["label"] == i][["text", "label"]]
        tdf = tdf.iloc[random.sample(range(0, tdf.shape[0]), k=min_size)]
        dfs.append(tdf)
    dfs = pd.concat(dfs)
    dfs.to_csv(os.path.join(sys.argv[1], "tweets_fixed.csv"))


if __name__ == "__main__":
    df = pd.read_csv(os.path.join(sys.argv[1], "tweets.csv"))
    fix(df)
