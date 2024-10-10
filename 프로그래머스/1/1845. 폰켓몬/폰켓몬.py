def solution(nums):
    length = len(nums) // 2
    nums = len(set(nums))
    answer = length if length <= nums else nums
    return answer