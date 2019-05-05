class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for cnt, num in enumerate(nums):
            if target - num in lookup:
                return lookup[target-num], cnt
            lookup[num] = cnt


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
