class Sentence_splitter(Abs_Class):

    def splitter(self):
        self.sentence_tokens = [sent for sent in self.doc.sents]
        return self.sentence_tokens