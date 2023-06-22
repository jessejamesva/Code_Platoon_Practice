"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order"""

def topKFrequent(nums, k):
    # nums_dict = {x: nums.count(x) for x in nums} ### TOO SLOW
    nums_dict = {}

    for i in nums:
        if i not in nums_dict:
            nums_dict[i] = 1
        else: 
            nums_dict[i] += 1
   
    
    res = []
    for i in range(k):
        val = max(nums_dict, key=nums_dict.get)
        res.append(val)
        nums_dict[val] = 0

    

    
    return res





print(topKFrequent([1,1,1,2,2,3],2))
print(topKFrequent([-1, -1], 1))
# print(topKFrequent([1,1,1,2,2,3],2) == [1,2])
# print(topKFrequent([1],1) == [1])
