#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Arne Neumann <languagemodels.programming@arne.cl>

from collections import Counter


def ngrams(iterable, n, pad=None):
    """
    generates a list of n-gram tuples from the input iterable (e.g.
    character n-grams if the input is a string or token n-grams if the input
    is a list of token strings).

    Parameters
    ----------
    iterable : str or list of str
        a string (to generate character ngrams) or a list of strings (to
        generate token ngrams)
    n : int
        1 to generate unigrams, 2 for bigrams etc.
    pad : str or None
        If the length of iterable is not evenly divisible by n, the
        final tuple is dropped if pad is not specified, or filled to length n
        by pad.

    Returns
    -------
    ngrams : list of tuples of str
    """
    if pad:
        iterable += pad * n
        for i in xrange(0, len(iterable)-n):
            yield tuple(iterable[i:i+n])
    else:
        for i in xrange(0, len(iterable)-n+1):
            yield tuple(iterable[i:i+n])


def ngram_counts(iterable, n, pad=' '):
    """
    generates a dictionary of ngram counts from the iterable input (e.g.
    character n-grams if the input is a string or token n-grams if the input
    is a list of token strings).
    """
    return Counter(ngrams(iterable, n, pad))
