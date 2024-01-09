#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    """Returns the length of a string and its first character."""
    return (len(sentence), sentence[0] if sentence else None)
