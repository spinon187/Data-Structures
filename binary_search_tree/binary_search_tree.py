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
    elif self.left is not None and target < self.value:
      # print(self.left.value)
      # print('left')
      return self.left.contains(target)
    elif self.right is not None and target > self.value:
      # print(self.right.value)
      # print('right')
      return self.right.contains(target)


  def get_max(self):
    pass

  def for_each(self, cb):
    pass