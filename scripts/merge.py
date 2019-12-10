import os
import sys
import pandas as pd


if __name__ == "__main__":
    files = (os.path.join(sys.argv[1], x) for x in (
        "happy.csv", "sad.csv", "angry.csv",
        "disgust.csv", "surprise.csv", "fear.csv"
    ))

    dfs = []
    for label, fname in enumerate(files):
        df = pd.read_csv(fname, sep=";")
        df["label"] = label
        dfs.append(df)
    dfs = pd.concat(dfs)
    dfs.to_csv(os.path.join(sys.argv[1], "tweets.csv"))
