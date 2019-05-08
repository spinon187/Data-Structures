class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    if len(self.storage) == 1:
      return self.storage.pop()
    elif len(self.storage) > 1:
      max_i = self.storage[0]
      self.storage[0] = self.storage.pop()
      self._sift_down(0)
      return max_i

  def get_max(self):
    if len(self.storage) > 0:
      return self.storage[0]
    else:
      return None

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, i):
    while i > 0:
      parent = (i - 1) // 2
      if self.storage[i] > self.storage[parent]:
        self.storage[i], self.storage[parent] = self.storage[parent], self.storage[i]
        i = parent
      else:
        break

  def _sift_down(self, i):
    left = i * 2 + 1
    right = i * 2 + 2
    size = len(self.storage)
    if left < size and right < size:
      if self.storage[left] > self.storage[right]:
        max_i = left
      else:
        max_i = right
    elif left < size:
      max_i = left
    else:
      max_i = right
    if max_i >= size:
      return
    if self.storage[i] < self.storage[max_i]:
      self.storage[i], self.storage[max_i] = self.storage[max_i], self.storage[i]
      self._sift_down(max_i)
