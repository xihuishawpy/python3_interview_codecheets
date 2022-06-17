# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
time: nlgn + nlgn
space: 2n
"""
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        prehead = ListNode()
        heap = []
        for list_ in lists:
            node = list_
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        node = prehead
        while heap:
            val = heapq.heappop(heap)
            node.next = ListNode()
            node = node.next 
            node.val = val
        return prehead.next
