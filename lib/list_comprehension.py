#!/usr/bin/env python3

def return_evens(num_list):
    even_num_list = [ n for n in num_list if n% 2 == 0]

    if not even_num_list:
        return []
    
    return even_num_list


def make_exclamation(sentence_list):
    bold_exclamation = [n + '!' for n in sentence_list]

    if not sentence_list:
        return []
    
    return bold_exclamation