JOBS?=2

.PHONY: all
all:
	pip3 install -r requirements.txt
	make scrape_tweets
	make p1
	make p2_3 -j $(JOBS)
	make spm
	make train
	make test

.PHONY: scrape_tweets
scrape_tweets:
	(cd data; bash run.sh)

.PHONY: p2_3
p2_3: p2 p3

.PHONY: p1
p1:
	python3 scripts/merge.py data

.PHONY: p2
p2:
	python3 scripts/fix_tweets.py data

.PHONY: p3
p3:
	python3 scripts/extract_text.py data

.PHONY: spm
spm:
	( cd data; spm_train --input=tweet_texts.txt --model_prefix=sp --vocab_size=8000 --model_type=bpe )

.PHONY: train
train:
	python3 scripts/train.py data

.PHONY: test
	python3 scripts/test_model.py data
