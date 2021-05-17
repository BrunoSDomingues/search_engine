#!/usr/bin/env python3
from argparse import ArgumentParser

from se.archive import load_archive
from se.index import load_index
from se.search import search
from se.normalizer import clean_text

MSG_DESCRIPTION = "Simple search engine"


def main():
    parser = ArgumentParser(description=MSG_DESCRIPTION)
    parser.add_argument("filename_docs", help="Path to json archive")
    parser.add_argument("filename_index", help="Path to json index")
    parser.add_argument("query", nargs="+", help="Search query")
    args = parser.parse_args()

    docs = load_archive(args.filename_docs)
    index = load_index(args.filename_index)
    
    # [palavra1, operador, palavra2, operador, palavra3]
    list_query = list(map(clean_text, args.query))

    query = " ".join(list_query)

    docs_searched = search(query, index, docs)

    if len(docs_searched) == 0:
        print("No results found.")

    else:
        for doc in docs_searched:
            print(" ".join(doc))
            print("=" * 100)


if __name__ == "__main__":
    main()
