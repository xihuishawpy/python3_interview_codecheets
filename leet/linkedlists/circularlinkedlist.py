"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        newNode = Node(insertVal)

        if not head:
            newNode.next = newNode
            return newNode

        prev = head
        node = head.next

        while (
            node
            and not (
                prev.val > node.val
                and (insertVal < node.val or insertVal > prev.val)
            )
            and not prev.val <= insertVal <= node.val
            and node != head
        ):
            prev = node
            node = node.next 

        prev.next = newNode
        newNode.next = node

        return head

    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        insertNode = Node(insertVal)

        if head is None:
            insertNode.next = insertNode
            return insertNode

        node = head

        while (
            node
            and not (
                node.next.val < node.val
                and (insertVal <= node.next.val or insertVal > node.val)
            )
            and not (node.val <= insertVal <= node.next.val or node.next == head)
        ):
            node = node.next 

        insertNode.next = node.next
        node.next = insertNode

        return head