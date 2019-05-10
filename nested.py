#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Determines whether the brackets in a string are matched and nested properly.
"""
__author__ = "jontaylor224"

import sys


def main(args):
    """Determines if various types of brackets are properly matched and nested.

    Parameters
    ----------
    args: input file containing lines of strings

    Returns
    -------
    Returns an output file stating whether each line of the input file has properly nested and matching brackets.  The output will be 'YES' if properly matched and nested, or 'NO #' where # is replaced by the position in the string of the improperly matched bracket if not properly matched and nested.
    For this program, brackets are defined as: '()', '{}', '[]', '<>', and
    '(**)'.  Note that '(*' and '*)' count as a single character when defining the position of the incorrectly matched bracket, and '(*)' is interpreted as '(*' followed by ')'.

    Example:

    Input: (input.txt)
    (*a++(*)
    (*a{+}*)
         <************)>
         ()(***)(**)
        ()(***)(*)
    ({{}{}}[{(){}[]}
        ([))
     ()(**)

    Output: (output.txt)
    NO 6
    YES
    NO 17
    YES
    NO 10
    NO 17
    NO 6
    YES
    """

    input_file = open(args[1], 'r')
    output_file = open('output.txt', 'w+')
    input_lines = input_file.readlines()

    openers = ['(', '{', '[', '<', '@']
    closers = [')', '}', ']', '>', '%']
    for line in input_lines:
        # replacing the two character brackets with single chars for simplicity
        line = line.replace('(*', '@')
        line = line.replace('*)', '%')
        count = 0
        stack = []
        for i in line:
            count += 1
            if i in openers:
                stack.append(i)
            if i in closers:
                if (len(stack) > 0 and openers[closers.index(i)] == stack[-1]):
                    stack.pop()
                else:
                    output = 'NO '+ str(count) + '\n'
                    break
        if len(stack) == 0:
            output_file.write('YES\n')
        else:
            output = 'NO ' + str(count) + '\n'
            output_file.write(output)

    output_file.close()
    input_file.close()


if __name__ == '__main__':
    main(sys.argv)
