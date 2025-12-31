class Solution(object):
    def helper(self, nums, i, l, temp):
        if i == len(nums) - 1:
            return l
        else:
            if len(temp) == 2:
                if temp[0] + temp[1] + i == 0:
                    temp.append(nums[i])
                    l.append(temp)
                    self.helper(nums, i+1, l, [])
                else:
                    self.helper(nums, i + 1, l, temp)
            l1 = self.helper(nums, i + 1, l, temp)
            temp.append(nums[i])
            l2 = self.helper(nums, i + 1, l, temp)
            if len(l1) > len(l2):
                return l+l1
            else:
                return l+l2

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.helper(nums, 0, [],[])


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([1,-1,0]))
