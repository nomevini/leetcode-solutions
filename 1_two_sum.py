class Solution:
    def twoSum(self, nums, target):
        result = []
        for x in range(len(nums)):
            for y in range(1, len(nums)):
                if nums[x] + nums[y] == target:
                    result.append(x)
                    result.append(y)
                    return result


lista = [3, 3]
s = Solution()
print(s.twoSum(lista, 6))

