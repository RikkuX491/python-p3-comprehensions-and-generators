#!/usr/bin/env python3

def return_evens(num_list):
    even_nums_list = [n for n in num_list if n % 2 == 0]
    return even_nums_list

def make_exclamation(sentence_list):
    sentences_with_exclamations = [f"{sentence}!" for sentence in sentence_list]
    return sentences_with_exclamations