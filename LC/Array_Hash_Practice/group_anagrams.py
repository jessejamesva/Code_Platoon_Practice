"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

"""
# stolen from the internet. Use to study hash maps
def groupAnagrams(strs):
    res = dict(list)

    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1

        res[tuple(count)].append(s)

    return res.values()


###### GOT TO GET HELP CAUSE THEY GIVE YOU A FUCKING DICTIONARY!!!! ######
# ################## passed 110/118 ######################################    
    # res = [[strs.pop()]]

    # while len(strs) > 0:
    #     word = strs.pop()
    #     temp_res = [word]
    #     word_arr = list(word)
    #     word_dict = {x: word_arr.count(x) for x in word_arr}
    #     match_flag = False

    #     for idx in range(len(res)):
    #         idx_word = res[idx][0]
    #         # print(res, word, idx_word)
    #         idx_arr = list(idx_word)
    #         idx_dict = {x: idx_arr.count(x) for x in idx_arr}
    #         if len(idx_word) != len(word):
    #             continue
    #         elif idx_word == word:
    #             res[idx].append(word)
    #             match_flag = True
    #         elif idx_dict == word_dict:
    #             res[idx].append(word)
    #             match_flag = True
    #     if not match_flag:
    #         res.append(temp_res)
    # print(res)
    # return res
        
         


        

#####  84/118 #### NEED NEW APPROACH!!!
# def groupAnagrams(strs):
#     if strs == [""]:
#         return [[""]]
    
#     if len(strs) == 1:
#         return list(strs)

#     res = [[strs.pop()]]

#     def test_anagram(dict, word):
#         for i in word:
#             if i not in dict:
#                 return False
#             else:
#                 if dict[i] == 0:
#                     return False
#                 dict[i] -= 1
#         return True       

#     while len(strs) > 0:
#         word = strs.pop()
#         word_two = list(word)
#         word_dict = {x: word_two.count(x) for x in word_two}
#         an_flag = False

#         for idx in range(len(res)):
#             idx_word = res[idx][0]
#             print(word_two, word, idx_word)
#             if word == idx_word or word == idx_word[::-1]:
#                 res[idx].append(word)
#                 an_flag = True
#                 print('Word added')
#             elif len(word) != len(idx_word):
#                 continue
#             elif test_anagram(word_dict, idx_word) and idx_word != "":
#                 res[idx].append(word)
#                 an_flag = True
#                 print('Word added')
#         if not an_flag:
#             res.append([word])
            
#     return res


# print(groupAnagrams(["eat","tea","tan","ate","nat","bat","ac","bd","aac","bbd","aacc","bbdd","acc","bdd"]))
# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]])
print(groupAnagrams(["eat","tea","tan","ate","nat","bat","ac","bd","aac","bbd","aacc","bbdd","acc","bdd"]) == [["bdd"],["bat"],["nat","tan"],["ac"],["ate","eat","tea"],["bd"],["aac"],["bbd"],["aacc"],["bbdd"],["acc"]])
print(groupAnagrams([""]) == [[""]])
print(groupAnagrams(["a"]) == [["a"]])
