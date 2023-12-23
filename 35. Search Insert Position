def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 1:
            if target == nums[0]:
                return 0
            elif target > nums[0]:
                return 1
            else:
                return 0


        if target < nums[0]:
            return 0

        elif target > nums[len(nums) - 1]:
            return len(nums)

        elif target == nums[len(nums) - 1]:
            return len(nums) -1

        left = 0
        right = len(nums) - 1
        count = 0
        mid = 0
        while left <= right and nums[left] <= nums[right]:
            mid = (left+right)/2
            count += 1
            print(count, mid)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target: #target is more to the left so change right
                right = mid - 1
            else:#target is more to the right so change left
                left = mid + 1
        
        if nums[mid] < target and target < nums[mid+1]:
            return mid + 1

        elif nums[mid] > target and nums[mid-1] < target:
            return mid
