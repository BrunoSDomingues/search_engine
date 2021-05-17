from .query import parse_raw_query, parse_json_query
from .rank import rank_documents
from .index import Index


def search(raw_query, index, docs):
    parsedquery = parse_json_query(parse_raw_query(raw_query))

    raw_query = raw_query.split()
    raw_query = [raw_query[i] for i in range(len(raw_query)) if i % 2 == 0]

    idx = Index(index)

    index_query = parsedquery.evaluate(idx)
    ranked_index = rank_documents(raw_query, docs, index_query, idx)

    return [docs[k] for k in ranked_index]
