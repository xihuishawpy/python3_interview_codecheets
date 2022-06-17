  def remove_duplicates(self):
    ht = {}
    myNode = self.head 

    if myNode is None:
      return

    while myNode: 
      tmp = myNode.next
      if myNode.data not in ht:
        ht[myNode.data] = True
      else:
        self.delete_node(myNode)
      myNode = tmp
  
  def delete_node(self, node):
    cur = self.head
    while cur:
      if cur == node:
        if cur == self.head:
                # Case 1:
          if not cur.next:
            self.head = None
          else:
            nxt = cur.next
            cur.next = None
            nxt.prev = None
            self.head = nxt
        else:
          prev = cur.prev
                # Case 3:
          if cur.next:
            nxt = cur.next
            prev.next = nxt
            nxt.prev = prev
            cur.next = None
          else:
            prev.next = None
          cur.prev = None
        cur = None
        return

      cur = cur.next