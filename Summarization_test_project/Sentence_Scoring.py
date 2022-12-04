class Sentence_scoring(Abs_Class):

    def scoring(self):
        for sent in self.sentence_tokens:
            for word in sent:
                if word.text.lower() in C.word_f().keys():
                    if sent not in self.sentence_scores.keys():
                        self.sentence_scores[sent] = C.word_f()[word.text.lower()]
                    else:
                        self.sentence_scores[sent] += C.word_f()[word.text.lower()]
        return self.sentence_scores