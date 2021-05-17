from nltk.stem import LancasterStemmer


def clean_text(txt: str):
    txt = txt.lower()

    # Utilizado para checar palavras que possuem bases em comum
    stemmer = LancasterStemmer()
    new_txt = [stemmer.stem(i) for i in txt.split()]

    new_txt = " ".join(new_txt)

    return new_txt
