#!/bin/bash
twitterscraper 😄 --lang ja --limit 1000000 --csv --output happy.csv &
twitterscraper 😢 --lang ja --limit 1000000 --csv --output sad.csv &
twitterscraper 😲 --lang ja --limit 1000000 --csv --output surprise.csv &
twitterscraper 🤮 --lang ja --limit 1000000 --csv --output disgust.csv &
twitterscraper 😡 --lang ja --limit 1000000 --csv --output angry.csv &
twitterscraper 😨 --lang ja --limit 1000000 --csv --output fear.csv & 

wait

echo "Done!"
