class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # combinar as listar de maneira ordenada (metodo mergesort)
        ordened_list = nums1 + nums2
        ordened_list.sort()
        mid = len(ordened_list) // 2
        if len(ordened_list) % 2 == 0:
            # par
            return (float(ordened_list[mid]) + float(ordened_list[mid - 1])) / 2
        else:
            # impar
            return float(ordened_list[mid])

s = Solution()
print(s.findMedianSortedArrays([1,2], [3, 4]))