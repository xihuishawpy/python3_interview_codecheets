class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Get precomputed answers with stack
        hm = {}
        stk = []

        for n in nums2:
            while len(stk) and stk[-1]<n:
                hm[stk.pop()] = n
            stk.append(n)

        return [hm.get(n, -1) for n in nums1]