#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consider the positional encoding of a number in base B.  Given the N
digits: a_{N-1} .... a_1 a_0 The value of the number is obtained by
summing, for each index i from 0 to N-1, the values a_i*B^i.

Example: if the base B=6 and the number is (52103)_6
Its value will be 5*6^4 + 2*6^3 + 1*6^2 + 0*6^1 + 3*6^0 = (6951)_10

Let's generalize this notation to use different bases for each
position: we will have a list "bases" consisting of N bases and a
number consisting of N digits contained in a list named "digits."  For
the example above, we will have: bases = [6, 6, 6, 6, 6], digits = [5,
2, 1, 0, 3]. The digits are such that each digit is less than the base
in the same position. The value of the number in base 10 is obtained
as in the initial conversion, using the i-th base from the list for
the i-th power.

NOTE: For convenience, we will use lists of digits and bases in which
the exponent of the power corresponds to the index in the lists. So,
each list will contain bases and digits starting from the units.

NOTE: The number of bases N is strictly greater than 1. The values of
the bases are also greater than 1.

Based on what has been said, one input for the homework is to generate
a list of all possible valid combinations of digits representable with
those bases.

Example: if the input bases are [2, 5], all combinations are:
[[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]

In fact:
- In the first digit, there are only values between [0, 1] because the base is 2.
- In the second digit, there are only values between [0, 4] because the base is 5.

Each combination represents an integer that needs to be converted from
a list to an integer according to the base specified in "bases." Once
all possible combinations have been converted into integers, it is
necessary to find which integers have more than one representation in
the given bases.

Example: If the input bases are [4, 3, 2], then the integers that
admit more than one representation are {3, 4, 5, 6, 7, 8, 9, 10}

In fact, for example, the number 10 with these bases has two representations:
[3, 1, 1] -> 3*4^0 + 1*3^1 + 1*2^2 = 10
[0, 2, 1] -> 0*4^0 + 2*3^1 + 1*2^2 = 10

The problem has already been divided into subproblems, and you need to
implement the following functions:
 - decode_digits is the simplest and fundamental function that
   receives a list of bases and a list of digits and converts it into
   an integer.
 - generate_digits is the function that does most of the work, given a
   list of bases, it calculates all combinations.
- find_doubles is the final function that, given the combinations,
  finds the corresponding integers that have more than one
  representation.

Each test must be completed within a timeout of 0.5 seconds.

ATTENTION: Importing libraries other than those already present is prohibited.
"""

from typing import List, Set


def decode_digits(digits: List[int], bases: List[int]) -> int:
    '''
    Receives a list of digits and a list of bases of the same length.
    Calculates the integer value as explained earlier.
    Parameters
    digits : List[int]    list of digits to convert
    bases   : List[int]    list of bases of the same length
    Returns
    int                    the corresponding integer value
    
    Example: decode_digits( [1, 1, 2], [2, 3, 4] ) -> 36
    in fact, 1*2^0 + 1*3^1 + 2*4^2 = 36
    '''
    # WRITE YOUR CODE HERE
    out = 0
    for i, val in enumerate(digits):
        out += val * bases[i] ** i
    return out
    pass


def generate_digits(bases : List[int] ) -> List[List[int]]:
    '''
    Given a list of bases, generates a list of all possible
    combinations of digits compatible with the given bases. Each
    combination is a list of compatible digits. Specifically, for
    each position corresponding to a base B, it contains one of the
    possible digits in [0..B-1].

    Example: generate_digits([2, 5]) produces the list
    [ [0, 0], [1, 0], [0, 1], [1, 1], [0, 2], [1, 2], [0, 3], [1, 3], [0, 4], [1, 4] ]

    Note: The order in the final list does not matter, and even
    [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]
    is a valid solution.
    '''
    # WRITE YOUR CODE HERE
        # possibleCombinations = 1
        # for i in bases:
        #     possibleCombinations *= i          #number of all possible combinations in [x, y] is xy, [x, y, z] is xyz
        # combinations = [[] for i in range(possibleCombinations)]      # empty list to which an integer will be added
        # for i in range(possibleCombinations):
        #     tempCombinations = []
        #     for j in bases:
        #         for k in range(j):
        #             tempCombinations.append([k])
        #     combinations = tempCombinations

        #combinations = [int(x) for x in combinations]
        #return combinations
        #basesLength = len(bases)
        #out = []
        #for i in bases:
        #   index = 0
        #  newDigitFrequence = int(possibleCombinations/i)
        # for k in range(newDigitFrequence):
            #    for j in range(i):
            #       combinations[index].append(j)
            #      index += 1
                    #print(f"{combinations}, i: {i}, j: {j}, k: {k}, index: {index-1}")
        #return combinations

        # a = bases[0]
        # b = bases[1]
        # out = []
        # for i in range(a):
        #     for j in range(b):
        #         out.append([i, j])
        # return out
    
    generatedList = [[]]        #doesn't work any other way :| (one element is required to get it started)
    newGenerated = []
    for i in bases:             #every base will mean a new integer (for 2 bases, output will have 2 integers in every combination)
        newGenerated = []
        for j in generatedList: #for every integer already in, a new 'combination' will be formed, another integer will be added to the present one
            for k in range(i):
                newGenerated.append(j + [k])    #adding a new integer, using one that is already present, creating a brand new list that now has +1 more elements
                #print(newGenerated)
        generatedList = newGenerated    #we can now replace the existing list with the new one, next 'elements batch' will be added to this one
    return generatedList
    pass


def find_doubles(bases : List[int]) -> Set[int]:
    '''
    Given a list of bases, generates a list of all possible valid
    combinations of digits representable with those bases, converts
    each combination into the corresponding integer, and looks for
    integers that appear more than once.

    Returns the set of integer values that have more than one
    representation in the given bases.

    Example: find_doubles([4, 3, 2]) -> {3, 4, 5, 6, 7, 8, 9, 10}
    In fact, for example, the number 10 with these bases has two representations:
    [3, 1, 1] -> 3*4^0 + 1*3^1 + 1*2^2 = 10
    [0, 2, 1] -> 0*4^0 + 2*3^1 + 1*2^2 = 10
    '''
    # WRITE YOUR CODE HERE
    generatedList = generate_digits(bases)
    currNum = 0
    out = set()
    dict = {}

        #test for 3 elements:
        #first = bases[0] 
        #second = bases[1]
        #third = bases[2] * bases[2]
        #for i in generatedList:
        #    a = i[0]
        #    b = i[1]
        #    c = i[2]
        #    currNum = a + b * second + c*third
        #    if currNum in dict:
        #        dict[currNum] += 1
        #    else:
        #        dict[currNum] = 1
        #for i in dict:
        #    if dict[i] > 1:
        #        out.add(i)
        # return out

    
    for i in generatedList:
        # index = 0
        # currNum = 0
        # while index < len(i):
        #     currNum += i[index] * bases[index] ** index
        #     index += 1
        currNum = decode_digits(i, bases)
        if currNum in dict:
            dict[currNum] += 1
        else:
            dict[currNum] = 1
    # print(dict)
    for i in dict:
        # print(i)
        if dict[i] > 1:
            out.add(i)
    return out

        #numbersList = []
        #for i in range(len(bases)):
        #    numbersList.append(10)
        #generatedNumbers = generate_digits(numbersList)
        #dict = {}
        #decoded = 0
        #out = set()
        #for i in generatedList:
        #    for j in generatedNumbers:
        #        decoded = decode_digits(i, j)
        #        #print(decoded)
        #        if decoded in dict:
        #            dict[decoded] += 1
        #        else:
        #            dict[decoded] = 1
        #for i in dict:
        #    if dict[i] > 1:
        #        out.add(i)
        #print(dict)
        #return out

    pass

###################################################################################
if __name__ == '__main__':
        # print(decode_digits([1, 1, 2], [2, 3, 4]))
        # print(generate_digits([2, 5]))
        # print(generate_digits([2,2,2]))
    # Enter your tests here
    # If you want to test your code on small data
    # Note that to run this main, you should use program.py
    # as a client and not as a module, meaning with 'python program.py'
    pass
