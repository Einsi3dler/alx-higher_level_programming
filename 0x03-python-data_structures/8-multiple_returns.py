#!/usr/bin/python3
def multiple_returns(sentence):
    val_len = len(sentence)
    if val_len == 0:
        return (val_len,None)
    else:
        sentence = list(sentence)
        val_fr = sentence[0]
        return (val_len, val_fr)
