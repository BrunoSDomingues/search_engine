from numpy import log2
from .index import Index


def score_document_tf_idf(query, docnum, doc, index: Index):
    N = len(doc)
    score = 0

    for word in query:
        count = index.countWords(word, str(docnum))

        if count != 0:
            score += log2(1 + count) * log2(N / len(index.find(word)))

    return score


def rank_documents(query, docs, index_query, index: Index):
    ranked_index = []

    for docnum in index_query:
        docnum = int(docnum)

        score = score_document_tf_idf(query, docnum, docs[docnum], index)
        ranked_index.append((score, docnum))

    return [item[1] for item in sorted(ranked_index, key=lambda x: -x[0])]
