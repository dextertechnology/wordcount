import re

class general:
    def __init__(self, text):
        self.text = re.sub(r'[^\w]', ' ', text.strip())
        

    def count_letters(self):
        return len(self.text)

    def count_words(self):
        return len(self.text.split())

    def words_with_numbers(self):
        splited_words = self.text.split()

        word_number = {}

        for word in splited_words:
            if word in word_number:
                word_number[word] += 1
            else:
                word_number[word] = 1

        return word_number.items()