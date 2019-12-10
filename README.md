
# sentiment_ja_train
Training pipeline of sentiment_ja


## How sentiment_ja works?

1. Search Tweets by emojis that corresponding to target emotions. (such as happy, sad, etc)
2. Scrape searched tweets (you can use this: https://github.com/taspinar/twitterscraper)
3. Annotate tweets by its emojis. After that, remove emojis from tweet texts. (This is called "distant supervision")
4. Build model by keras. Input is tweet text, and output is tweet's label.
5. Test model. (Unfortunately, I don't have clean test data for this task. )

## Workflow

The complete workflow is defined as Makefile. You just need to run:

```
make
```

Warning: I hadn't tested Makefile yet, but maybe you can understand what sentiment_ja does if you see the Makefile.