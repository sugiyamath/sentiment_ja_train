import pandas as pd
import sys
import os
from tqdm import tqdm

if __name__ == "__main__":
    df = pd.read_csv(os.path.join(sys.argv[1], "tweets.csv"))["text"]
    with open(os.path.join(sys.argv[1], "tweet_texts.txt"), "w") as f:
        for text in tqdm(df):
            text = str(text).replace("\n", " ")
            f.write(text + "\n")
