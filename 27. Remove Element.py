class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        garb = len(nums) - 1

        i = 0

        while i < garb:
            if nums[i] == val:

                if nums[garb] != val:
                    # switch elements
                    tempi = nums[i]
                    tempgarb = nums[garb]

                    nums[garb] = tempi
                    nums[i] = tempgarb

                    garb -= 1
                    i += 1


                else:
                    garb -= 1

            else:
                if nums[garb] == val:
                    garb -= 1
                else:
                    i += 1

        if len(nums) > 0 and nums[garb] != val:
            return garb + 1
        else:
            return garb

sol = Solution()
print(sol.removeElement([8], 5))
