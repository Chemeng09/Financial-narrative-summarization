class Word_frequencies(Abs_Class):

    def word_f(self):
        for word in doc:
            if word.text.lower() not in stop_words:
                if word.text.lower() not in punctuation:
                    if word.text not in self.word_frequencies.keys():
                        self.word_frequencies[word.text] = 1
                    else:
                        self.word_frequencies[word.text] += 1

        return self.word_frequencies