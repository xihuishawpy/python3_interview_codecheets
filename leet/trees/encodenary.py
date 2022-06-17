"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        rtn = []
        def dfs(node):
            if node:
                rtn.append(str(node.val))
                for c in node.children:
                    dfs(c)
            rtn.append('#')
        dfs(root)
        return ' '.join(rtn)


        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        def dfs():
            val = next(vals)
            if val == '#':
                return None
            node = Node(int(val), [])
            while child := dfs():
                node.children.append(child)
            return node
            
        vals = iter(data.split())
        return dfs()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))