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
