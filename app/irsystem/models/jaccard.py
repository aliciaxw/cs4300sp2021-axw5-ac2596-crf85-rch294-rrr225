from __future__ import division
import sys

# Jaccard is the intersection between two string diided by the set of two strings


def j_score(toks1, toks2):
    """
    [j_score(toks1, toks2)] is the jaccard similarity score for two lists of tokens,
    [toks1] and [toks2].

    Note:
      - assumes that [toks1] and [toks2] are not sets.
    """
    toks_1 = set(toks1)
    toks_2 = set(toks2)

    if len(toks_1) > 0 and len(toks_2) > 0:
        intersect = toks_1.intersection(toks_2)
        union = toks_1.union(toks_2)

        if len(union) == 0:
            return 0
        else:
            return len(intersect) / len(union)

    return 0


# def test():
#     t1 = ['hello', 'world']
#     t2 = ['hello', 'a']
#     t3 = []
#     t4 = ['a', 'b', 'c ']
#     t5 = ['a', 'c', 'b', ' ']
#     print(j_score(t1, t1))
#     print(j_score(t1, t2))
#     print(j_score(t3, t3))
#     print(j_score(t4, t1))
#     print(j_score(t4, t5))


# if __name__ == '__main__':
#     test()
