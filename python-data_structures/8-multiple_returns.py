#!/usr/bin/python3
def multiple_returns(sentence):
    ple = []
    if not sentence:
        ple = len(sentence), None
        return ple
    else:
        ple = len(sentence), sentence[0]
        return (ple)
