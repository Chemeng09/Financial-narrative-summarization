# -*- coding: utf-8 -*-
"""Untitled45.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j_aCr3OwBBcfzUUGto_PvMDECkKCv1OB
"""

class Dummy2_Sentence_Splitter(Sentence_Splitter):
    
    def splitter(self, text):
        text_2 = text.splitlines()
        for substring in text_2:
            substring_split = substring.split(".")
        return substring_split

E = Dummy2_Sentence_Splitter()
y = E.splitter(text)
print(y)