#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    elif len(a_dictionary.values()) < 0:
        return None
    else:
        val = []
        for k,v in a_dictionary.items():
            val.append(v)
        val.sort()
        return val[-1]
