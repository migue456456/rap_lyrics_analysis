import re
from spacy.lang.en.stop_words import STOP_WORDS

class TextCleaner:
    """
    A class to handle loading, cleaning, tokenizing, and analyzing text data.
    Attributes:
        stop_words (set): a set of English stop words for filtering
    """

    def __init__(self):
        # Prepare stop words set and remove apostrophes
        self.stop_words = {w.replace("'", "") for w in STOP_WORDS}

    def load_text(self, path):
        """
        Loads a text file and returns its content as a string.
        Args:
            path (str): Path to the text file
        Returns:
            str: Raw text from the file
        """
        with open(path, "r") as f:
            return f.read()

    def clean_text(self, text):
        """
        Cleans text by removing punctuation, lowering case,
        and applying specific word replacements.
        Args:
            text (str): The raw text
        Returns:
            str: Cleaned text
        """
        text = text.replace("'", "")
        text = text.replace("-", "")
        text = text.replace(".", "")
        text = text.lower()

        # Specific replacements for sensitive or slang terms
        text = text.replace("nigga", "fella")
        text = text.replace("niggas", "fellas")
        text = text.replace("hoe", "fox")
        text = text.replace("hoes", "foxs")

        return text

    def tokenize(self, text):
        """
        Tokenizes text into a list of words (alphabetic characters only).
        Args:
            text (str): Cleaned text
        Returns:
            list: List of word tokens
        """
        return re.findall(r"[a-z]+", text)

    def count_words(self, tokens):
        """
        Counts the occurrences of each word in the list of tokens.
        Args:
            tokens (list): List of word tokens
        Returns:
            dict: Word counts
        """
        counts = {}
        for t in tokens:
            counts[t] = counts.get(t, 0) + 1
        return counts

    def remove_stopwords(self, word_counts):
        """
        Removes stop words from a dictionary of word counts.
        Args:
            word_counts (dict): Word counts dictionary
        Returns:
            dict: Filtered word counts
        """
        return {w: c for w, c in word_counts.items() if w not in self.stop_words}

    def longest_word(self, word_counts):
        """
        Finds the longest word in the word counts dictionary.
        Args:
            word_counts (dict): Word counts dictionary
        Returns:
            str: The longest word
        """
        return max(word_counts.keys(), key=len)

    def total_words(self, word_counts):
        """
        Calculates total number of words (sum of all counts).
        Args:
            word_counts (dict): Word counts dictionary
        Returns:
            int: Total word count
        """
        return sum(word_counts.values())

    def unique_words(self, word_counts):
        """
        Returns a list of words that appear exactly once.
        Args:
            word_counts (dict): Word counts dictionary
        Returns:
            list: Words with count == 1
        """
        return [w for w, c in word_counts.items() if c == 1]

    def avg_word_length(self, word_counts):
        """
        Computes the average word length weighted by word frequency.
        Args:
            word_counts (dict): Word counts dictionary
        Returns:
            float: Average word length
        """
        total_chars = sum(len(w) * c for w, c in word_counts.items())
        return total_chars / self.total_words(word_counts)
