#!/usr/bin/env python

def sentence(string):
  for word in string.split():
    yield word


my_sentence = sentence("This is a Test")


for word in my_sentence:
  print(word)

