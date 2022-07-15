"""Given an integer array nums and an integer k,
 return the k most frequent elements.
 You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]"""


def mostKnum(nums,k):
    count = {}
    freq = [[] for i in range(len(nums)+1)]

    for i in range(len(nums)):
        count[nums[i]] = 1 + count.get(nums[i],0)

    for f,c in count.items():
        freq[c].append(f)

    result = []

    for i in reversed(range(len(freq))):
        for n in freq[i]:
            result.append(n)
            if len(result) == k:
                return result




if __name__=='__main__':
    x = mostKnum([1,1,1,2,2,3],2)
    print(x)