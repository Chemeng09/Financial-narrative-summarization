class Max_frequency(Abs_Class):

    def max_f(self):
        self.max_frequency = max(C.word_f().values())
        return self.max_frequency