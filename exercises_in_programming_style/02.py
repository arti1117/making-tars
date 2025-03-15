#!/usr/bin/env python3
import sys, re, operator, string

stack = []

heap = {}

def read_file():
    f = open(stack.pop())
    stack.append(f.read())
    f.close()

def filter_chars():
    stack.append(re.compile(r'[\W_]+'))
    stack.append([stack.pop().sub(' ', stack.pop().lower())])

def scan():
    stack.extend(stack.pop()[0].split())

def remove_stop_words():
    f = open('exercises_in_programming_style/stop_words.txt')
    stack.append(f.read().split(','))
    f.close()

    stack[-1].extend(list(string.ascii_lowercase))
    heap['stop_words'] = stack.pop()

    heap['words'] = []
    while len(stack) > 0:
        if stack[-1] in heap['stop_words']:
            stack.pop()
        else:
            heap['words'].append(stack.pop())
    stack.extend(heap['words'])
    del heap['stop_words']
    del heap['words']


def frequencies():
    heap['word_freqs'] = {}
    while len(stack) > 0:
        if stack[-1] in heap['word_freqs']:
            stack.append(heap['word_freqs'][stack.pop()])
            stack.append(1)
            stack.append(stack.pop() + stack.pop())
        else:
            stack.append(1)
        heap['word_freqs'][stack.pop()] = stack.pop()
    
    stack.append(heap['word_freqs'])
    del heap['word_freqs']

def sort():
    stack.extend(sorted(stack.pop().items(), key=operator.itemgetter(1)))

stack.append("exercises_in_programming_style/input.txt")
read_file()
filter_chars()
scan()
remove_stop_words()
frequencies()
sort()

stack.append(0)

while stack[-1] < 25 and len(stack) > 1:
    heap['i'] = stack.pop()
    (w, f) = stack.pop()
    print(w, ' - ', f)
    stack.append(heap['i'])
    stack.append(1)
    stack.append(stack.pop() + stack.pop())

