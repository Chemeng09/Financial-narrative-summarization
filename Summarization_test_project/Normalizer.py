class Normalization(Abs_Class):

    def normalizer(self):
        for word in C.word_f().keys():
            self.word_frequencies[word] = self.word_frequencies[word] / D.max_f()
        return self.word_frequencies

