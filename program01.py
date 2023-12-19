#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Your dear friend Pico de Paperis sent you a very strange message scribbled on a postcard.
You haven't seen him in a long time and you've always had fun writing to each other in code.
To decode his message, go and look for a rather particular book in your library,
the Archimedes Pythagorean cipher. The cipher to be applied is the famous "Pharaoh's Cipher".
The decipherment with the Pharaoh's method is based on rules for substituting sequences of symbols in the text.
The reason why it is called "Pharaoh's cipher" is that in ancient Egyptian sequences made up of multiple hieroglyphs
could be written in any order, so any anagram of the sequences was valid.
To make things stranger, Pico de Paperis decided to use a cipher that is not exactly the one of Pharaoh,
but a variant of it. Instead of using anagrams he uses "quasi-anagrams", that is, anagrams that in the original text
have one more spurious character than the searched sequence.
The cipher contains pairs of sequences that indicate how to transform the text.
For example, the pair 'shampoo' -> 'soap' corresponds to searching for a point in the message where the sequence
'shampoo' appears (or an anagram of it) but with an extra character (e.g. 'pmQohaso')
and replace it with the sequence 'soap'.
Decoding the message can lead to more possible final messages, because there can be more sequences in the text
that can be transformed at any time and the order of transformations influences subsequent transformations.
At some point it will happen that none of the "quasi-anagrams" of a cipher sequence is present anywhere
in the sequence of symbols, and therefore it is no longer possible to make transformations.
We call these sequences final sequences.
Of all the possible final sequences, the one we are interested are all the shortest.

To decode the Pico de Paperis message you must implement the function
pharaohs_revenge(encrypted_text : str, pharaohs_cypher : dict[str,str]) -> set[str]:
which receives as arguments:
- the text that Pico de Paperis sent you, as a string of symbols (characters)
- the cipher to be applied, a dictionary whose keys are the sequences to search for a quasi-anagram in the text
    and as the associated value the string to replace the quasi-anagram found with.
The function must return the set of the shortest texts obtainable by repeatedly applying
the transformations until it is no longer possible to apply any of them.

Example:
encrypted_text  = 'astronaut-flying-cyrcus'
pharaohs_cypher = {'tuar': 'me', 'cniy': 'op', 'sorta': 'tur', 'fult': 'at', 'rycg': 'nc'}

Result: {'tmeopcus', 'metopcus', 'ameopcus', 'atmepcus'}
Notice, and all the transformations applied are those contained in the example.txt file
(in alphabetical order and without repetitions)

NOTE: At least one of the functions or methods you implement must be recursive
NOTE: the recursive function/method must be defined at the outermost level
      otherwise you will fail the recursion test.
'''
def quasi_anagram(text, word):
    if len(text) - 1 != len(word):
        return False
    dict1 = {}
    dict2 = {}
    for i, val in enumerate(word):
        try:
            dict1[val] += 1
        except:
            dict1[val] = 1
    for i, val in enumerate(text):
        try:
            dict2[val] += 1
            # dict1[word[i]] += 1
        except:
            dict2[val] = 1
            # dict1[word[i]] = 1
    if len(set(dict2.items())-set(dict1.items())) == 1:
        return True
    return False


def pharaohs(text, cypher, minLen, maxLen, out):
    length = len(text)
    for i, val in enumerate(text):
        startIndex = i
        j = minLen 
        while j <= length:
            searchFor = text[i:j+1]
            # print("search for: "+searchFor)
            for word in cypher.keys():
                # print(text)
                # print(text[:i]+"|"+cypher[word]+"|"+text[j:])
                if quasi_anagram(searchFor, word):
                    newtext = text[:i]+cypher[word]+text[j+1:]
                    out.add(newtext)
                    # print("i, val:" + str(i) + val)
                    pharaohs(newtext, cypher, minLen, maxLen, out)
            out.add(text)
            j += 1
                
    pass

def pharaohs_revenge(encrypted_text : str, pharaohs_cypher : dict[str,str]) -> set[str]:
    # minLen = len(min(dict, key = len(dict.get)))
    # maxLen = len(max(dict, key = len(dict.get)))
    minLen = len(min(pharaohs_cypher, key = lambda x: len(x)))
    maxLen = len(max(pharaohs_cypher, key = lambda x: len(x)))
    length = len(encrypted_text)
    out = set()
    pharaohs(encrypted_text, pharaohs_cypher, minLen, maxLen, out)
    shortestLength = length
    currLength = 0
    finalOut = set()
    for i in out:
        currLength = len(i)
        if currLength < shortestLength:
            shortestLength = currLength
            finalOut.clear()
            finalOut.add(i)
        if currLength == shortestLength:
            finalOut.add(i)
    # finalOut = set()
    # finalOut = {i for i in out if len(i) == shortestLength}
    return finalOut
    pass
    # add here your code



if __name__ == '__main__':
    encrypted_text  = 'astronaut-flying-cyrcus'
    pharaohs_cypher = {'tuar': 'me', 'cniy': 'op', 'sorta': 'tur', 'fult': 'at', 'rycg': 'nc'}
    print(pharaohs_revenge(encrypted_text, pharaohs_cypher))
    # print(quasi_anagram("ut-fl", "fult"))

    pass
    # place here your own tests