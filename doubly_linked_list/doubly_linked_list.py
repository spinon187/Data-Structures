"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    if not self.head and not self.tail:
      self.head = ListNode(value)
      self.tail = self.head
      self.length += 1
    else:
      self.head.insert_before(value)
      self.head = self.head.prev
      self.length += 1
      return self.head.value

  def remove_from_head(self):
    if self.head is None and self.tail is None:
      return None
    if self.length == 1:
      val = self.head.value
      self.head.delete()
      self.length -= 1
      self.head = None
      self.tail = None
      return val
    else:
      next_head = self.head.next
      self.head.delete()
      self.head = next_head
      self.length -= 1
      return self.head.value

  def add_to_tail(self, value):
    if not self.head and not self.tail:
      self.head = ListNode(value)
      self.tail = self.head
      self.length += 1
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next
      self.length += 1
      return self.tail.value

  def remove_from_tail(self):
    if self.head is None and self.tail is None:
      return None
    elif self.length == 1:
      val = self.tail.value
      self.tail.delete()
      self.length -= 1
      self.head = None
      self.tail = None
      return val
    else:
      next_tail = self.tail.prev
      self.tail.delete()
      self.tail = next_tail
      self.length -= 1
      return self.tail.value

  def move_to_front(self, node):
    stored = node.value
    if self.head == node:
      self.remove_from_tail()
      self.add_to_head(stored)
    else:
      node.delete()
      self.length -= 1
      self.add_to_head(stored)

  def move_to_end(self, node):
    stored = node.value
    if self.head == node:
      self.remove_from_head()
      self.add_to_tail(stored)
    else:
      node.delete()
      self.length -= 1
      self.add_to_tail(stored)

  def delete(self, node):
    if self.head is None and self.tail is None:
      return None
    elif self.length == 1:
      val = node.value
      node.delete()
      self.length -= 1
      self.head = None
      self.tail = None
      return val
    elif self.head == node:
      self.remove_from_head()
    elif self.tail == node:
      self.remove_from_tail()
    else:
      val = node.value
      node.delete()
      self.length -= 1
      return val
    
  def get_max(self):
    if self.head is None and self.tail is None:
      return None
    got_max = self.head.value
    i = self.head
    while i != self.tail:
      next = i.next
      if i.value < next.value:
        got_max = next.value
      i = next
    return got_max
