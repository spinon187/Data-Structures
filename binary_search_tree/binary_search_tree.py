class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    elif self.left is None and self.right is None:
      return False
    elif self.left and target < self.value:
      return self.left.contains(target)
    elif self.right and target > self.value:
      return self.right.contains(target)


  def get_max(self):
    if not self.right:
      return self.value
    else:
      return self.right.get_max()

  def for_each(self, cb):
    cb(self.value)
    if self.right:
      self.right.for_each(cb)
    if self.left:
      self.left.for_each(cb)
