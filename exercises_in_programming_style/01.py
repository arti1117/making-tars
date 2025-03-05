#! /usr/bin/env python3

import sys, os, string


def touchopen(filename, *args, **kwargs):
    try:
        os.utime(filename)
    except os.error:
        pass
    open(filename, "a").close()
    return open(filename, *args, **kwargs)


data = []

f = open("exercises_in_programming_style/stop_words.txt")
data = [f.read(1024).split(",")]
f.close()

data.append([])
data.append(None)
data.append(0)
data.append(False)
data.append("")
data.append("")
data.append(0)

word_freqs = touchopen("word_freqs", "rb+")

f = open(sys.argv[1])

while True:
    data[1] = [f.readline()]
    if data[1] == [""]:
        break
    if data[1][0][len(data[1][0]) - 1] != "\n":
        data[1][0] += "\n"
    data[2] = None
    data[3] = 0
