# change a string into QT style (typing AIDS):
    # randomly replace letters with adjacent letters on keyboard
    # randomly duplicate letters
    # randomly swap two letters
    # change letters to upper case (only after an upper case letter)

import random

# make a dictionary that associates each letter in the alphabet with a list of # its neighbors on the keyboard
alphabet = list("abcdefghijklmnopqrstuvwxyz")
alphabet_upper = [c.upper() for c in alphabet] # will need this later
neighbors_list = [
    list("zqwsx"), # a
    list("vngh "), # b
    list("vxdf "), # c
    list("serfcx"), # d
    list("wsdr34"), # e
    list("drtgcv"), # f
    list("ftyhvb"), # g
    list("gyujbn"), # h
    list("ujko89"), # i
    list("hnmkiu"), # j
    list("jiolm,"), # k
    list("kop;.,"), # l
    list("njk,"), # m
    list("bhjm "), # n
    list("pil90"), # o
    list("o0["), # p
    list("wa1\t"), # q
    list("edt"), # r
    list("wadx"), # s
    list("rfyg56"), # t
    list("yij78"), # u
    list("cb "), # v
    list("q23"), # w
    list("zcs"), # x
    list("tuh6"), # y
    list("xas") # z
]
neighbors_dict = dict(zip(alphabet, neighbors_list))

# simulate hitting the wrong key by replacing its letter with a random choice
# of one of its neighbors; if the key isn't a letter, leave it alone
def wrong_key(char):
    if char.lower() in alphabet:
        choice = random.randint(0, len(neighbors_dict[char.lower()])-1)
        return neighbors_dict[char.lower()][choice]
    else: return char

# simulate hitting a key twice by returning 2 of its letter; this can happen # to any key, not just letters
def duplicate_key(char):
    return char * 2

# simulate holding the shift key too long by making the letter following an
# upper case letter upper case also; this is not the right way to do it, but
# it has some interesting behavior that adds to the effect so whatever
def uppercase_key(charlist):
    for c in charlist:
        if c in alphabet_upper:
            ind = charlist.index(c)
            charlist[ind+1] = charlist[ind+1].upper()

# swap two letters (this happens when typing too quickly)
# the weird index math is sure to cause some bugs but I don't care enough
# to find a better way to do it right now
def swap_keys(charlist):
    for c in charlist:
        if c != " ":
            ind = charlist.index(c) - 1
            temp = charlist[ind]
            charlist[ind] = charlist[ind+1]
            charlist[ind+1] = temp

# the string to be QTfied
example = input("\nOriginal string:\n")

# make an empty list to hold each character of the modified string
new_string = list()

# roll a die for each character in the input string and apply one or none of
# the functions to it; put the returned character in a list
for s in example:
    chance = random.randint(0, 15)
    if chance == 1: new_string.append(wrong_key(s))
    elif chance == 2: new_string.append(duplicate_key(s))
    else: new_string.append(s)

# apply the upper case_key function to the list
uppercase_key(new_string)

# roll a die and apply the swap function to the list
chance = random.randint(0, 20)
if chance == 1: swap_keys(new_string)

# print the QTfied string (actually print each item in the list and suppress
# the newlines)
print("\nQTfied string:")
for c in new_string: print(c, end="")
print("\n")
