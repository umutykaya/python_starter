# Import function to perform tokenization
# from .token_utils import tokenize
import nltk

class Tokenize:
    def __init__(self, text):
        self.text = text
        self.words = self._word_tokenize()
        self.sentence = self._sentence_tokenize()
         
    def _word_tokenize(self):
        return nltk.word_tokenize(self.text)

    def _sentence_tokenize(self):
        return nltk.sent_tokenize(self.text)