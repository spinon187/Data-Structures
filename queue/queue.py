class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.insert(0, item)
    print(self.storage)
  
  def dequeue(self):
    if len(self.storage) != 0:
      val = self.storage[-1]
      self.storage.pop()
      return val
    else:
      return None

  def len(self):
    return len(self.storage)
