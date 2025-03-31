import re

class tokenizerbyVisakhV1:
    def __init__ (self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s, i in vocab.items()}

    def encode(self, text):
        preprocessed_result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed_result = [item.strip() for item in preprocessed_result if item.strip()]

        ids = [self.str_to_int[s] for s in preprocessed_result]

        return ids
    
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s([.,!?;])', r'\1', text) # For removing the spaces before punctuation
        return text
    
    