"""
Linear Search

Worst Case Time Complexity: O(n)

"""

def linear_search(tar, nums):
    i=0
    while i < len(nums):
        if nums[i] == tar:
            return i
        i += 1
    return -1

tar = 6
nums = [55, 69, 1, 2, 5, 77, 530, 0, 6, 3]

index = linear_search(tar, nums)

if index != -1:
    print(f'found at index {index}')
else:
    print('not found')


#   linear search and return list of multiple occurances of number

def linear_search_multiple(tar, nums):
    i=0
    occ = []
    while i < len(nums):
        if nums[i] == tar:
            occ.append(i)
        i += 1
    return occ if occ else -1

tar = 6
nums = [55, 69, 1, 2, 6, 6, 530, 0, 6, 3]

index = linear_search_multiple(tar, nums)

print(f'found at index {index}') if index else print('not found')
