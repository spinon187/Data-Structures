class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    pass

  def get_max(self):
    if (len(self.storage) != 0):
      return self.storage[0]

  def get_size(self):
    pass

  def _bubble_up(self, i):
    while i > 0:
      parent = (i - 1) // 2
      if self.storage[i] > self.storage[parent]:
        self.storage[i], self.storage[parent] = self.storage[parent], self.storage[i]
        i = parent
      else:
        break

  def _sift_down(self, index):
    pass
