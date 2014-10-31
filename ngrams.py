#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Arne Neumann <languagemodels.programming@arne.cl>

from collections import Counter


def ngrams(words, n, pad=None):
    """
    generates a list of n-gram tuples from the given list of words.

    Parameters
    ----------
    words : list of str
        a list of strings
    n : int
        1 to generate unigrams, 2 for bigrams etc.
    pad : str or None
        If pad is given, it is used to generate ngram tuples for the last
        n-1 words of the input. For example, in a bigram model, the input
        ['He', 'died', '.'] would produce the ngrams
        [('He', 'died'), ('died', '.'), ('.', pad)]. Otherwise, these ngrams
        would be produced: [('He', 'died'), ('died', '.')].

    Returns
    -------
    ngrams : list of tuples of str
    """
    if pad:
        # we need to add the padding element once in a bigram model, twice in a
        # trigram model etc.
        words = list(chain(words, repeat(pad, n-1)))
    for i in xrange(0, len(words)-n+1):
        yield tuple(words[i:i+n])


def ngram_counts(iterable, n, pad=' '):
    """
    generates a dictionary of ngram counts from the iterable input (e.g.
    character n-grams if the input is a string or token n-grams if the input
    is a list of token strings).
    """
    return Counter(ngrams(iterable, n, pad))
