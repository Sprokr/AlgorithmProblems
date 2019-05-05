class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        mid = (hi + lo) / 2
        while (hi >= lo):
            if hi == lo+1:
                return min(nums[lo], nums[hi])
            elif nums[hi] >= nums[mid] and nums[mid] >= nums[lo]:
                return nums[lo]
            elif nums[hi] >= nums[mid] and nums[mid] <= nums[lo]:
                hi = mid

            elif nums[hi] <= nums[mid] and nums[mid] >= nums[lo]:
                lo = mid
            mid = (hi + lo) / 2
        return


sol = Solution()

sol.findMin( map(int,raw_input().split()))