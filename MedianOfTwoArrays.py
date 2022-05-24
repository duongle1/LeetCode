#Median of two short array
'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n))'''

#def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = [*nums1, *nums2]
        merged.sort()
        median = (len(merged)/2)
        if len(merged) % 2 == 0: 
            index = int(median)   
            result = (merged[index-1]+merged[index])/2
        else:
            median = int(median)
            result = merged[median]
        
        return result    

        