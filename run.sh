#!/bin/bash
[ -z "$1" ] && { 
    echo "Query is missing!"
    exit 2
}

rm -f data/*.json

echo "Making archive..."
python scripts/make_archive_from_donald_tweets.py data/donald_tweets.csv data/archive.json
echo "Done."
echo " "
echo "Making index..."
python scripts/make_index_from_archive.py data/archive.json data/index.json
echo "Done."
echo " "
echo "Parsing query results..."
python scripts/search.py data/archive.json data/index.json "$1"
