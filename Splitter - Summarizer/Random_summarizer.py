# -*- coding: utf-8 -*-
"""Untitled45.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j_aCr3OwBBcfzUUGto_PvMDECkKCv1OB
"""

import random

class Random_Summarizer(Summarizer):

    def summarizer(self, string_list):
       rand_sum = '.'.join(random.choices(string_list, k=5))
       return rand_sum

S = Random_Summarizer()
summary = S.summarizer(x)
print(summary)