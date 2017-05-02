
class Solution(object):

    def twoSum(self, nums, target):
        if len(nums) < 2:
            return False

        dictResult = {}

        for i in range(len(nums)):
            if nums[i] in dictResult:
                return [dictResult[nums[i]], i]
            else:
                dictResult[target - nums[i]] = i



if __name__ == '__main__':
    nums = [22, 2, 7, 15]
    target = 9

    rest = Solution().twoSum(nums, target)

    print(rest)
