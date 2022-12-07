#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    elif len(a_dictionary.values()) < 0:
        return None
    else:
        val = [0,0]
        for k,v in a_dictionary.items():
            if v => val[1]:
                val[0] = k
                val[1] = v
            else:
                pass
        return val[0]
