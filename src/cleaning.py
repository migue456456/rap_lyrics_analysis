import re
from spacy.lang.en.stop_words import STOP_WORDS

stop_words = {w.replace("'", "") for w in STOP_WORDS}

def load_text(path):
    with open(path, "r") as f:
        return f.read()

def clean_text(text):
    text = text.replace("'", "")
    text = text.replace("-", "")
    text = text.replace(".", "")
    text = text.lower()

    # replacements
    text = text.replace("nigga", "fella")
    text = text.replace("niggas", "fellas")
    text = text.replace("hoe", "fox")
    text = text.replace("hoes", "foxs")

    return text

def tokenize(text):
    return re.findall(r"[a-z]+", text)

def count_words(tokens):
    counts = {}
    for t in tokens:
        counts[t] = counts.get(t, 0) + 1
    return counts

def remove_stopwords(word_counts):
    return {w: c for w, c in word_counts.items() if w not in stop_words}

def longest_word(word_counts):
    return max(word_counts.keys(), key=len)

def total_words(word_counts):
    return sum(word_counts.values())

def unique_words(word_counts):
    return [w for w, c in word_counts.items() if c == 1]

def avg_word_length(word_counts):
    total_chars = sum(len(w) * c for w, c in word_counts.items())
    return total_chars / total_words(word_counts)
