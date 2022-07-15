"""Given an array of strings strs, group the anagrams together.
 You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging 
the letters of a different word or phrase, typically u
sing all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

from regex import I


def grouped_ana(strs):

    #declare dictonary to store anagean
    ana_d = {}
    if len(strs)==1:
        return [[strs[0]]]

    for word in strs:
        sortedword = ''.join(sorted(word))
        if sortedword not in ana_d:
            ana_d[sortedword] = [word]

        else:
            ana_d[sortedword] += [word]

    return [ana_d[i] for i in ana_d]





if __name__ == '__main__':
    # strs = ["eat","tea","tan","ate","nat","bat"]

    x = grouped_ana([""])
    print(x)

