def quasi_anagram(text, word):
    if len(text) - 1 != len(word):
        return False
    if text.count(text[0]) == len(text) and word.count(word[0]) == len(word) and text[0] != word[0]:
        return False
    char = ''
    for i in text:
        if text.count(i) != word.count(i):
            if char == '':
                char = i
            elif char != i:
                return False
    return True

def pharaohs(text, cypher, minLen, out):
    length = len(text)
    for i in range(length - minLen + 1):
        for word in cypher.keys():
            searchFor = text[i:i+len(word)+1]
            if quasi_anagram(searchFor, word):
                newtext = text[:i]+cypher[word]+text[i+len(word)+1:]
                out.add(newtext)
                pharaohs(newtext, cypher, minLen, out)
            
def pharaohs_revenge(encrypted_text : str, pharaohs_cypher : dict[str,str]) -> set[str]:
    if not pharaohs_cypher:
        return {encrypted_text}
    minLen = len(min(pharaohs_cypher.keys(), key = lambda x: len(x)))
    out = set()
    out.add(encrypted_text)
    pharaohs(encrypted_text, pharaohs_cypher, minLen, out)
    finalOut = set(i for i in out if len(i) == len(min(out, key = lambda x: len(x))))
    return finalOut
    pass
    # add here your code

if __name__ == '__main__':
    pass

    # place here your own tests