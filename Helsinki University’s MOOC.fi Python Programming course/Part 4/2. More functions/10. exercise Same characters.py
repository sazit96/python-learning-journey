def first_word(s): 
    word = s.split()
    return word[0];
def second_word (s):
    word = s.split()
    return word[1]
def last_word (s):
    word = s.split()
    return word[-1]

sentence = "it was a dark and stormy python"

print(first_word(sentence)) # it
print(second_word(sentence)) # was
print(last_word(sentence)) # python