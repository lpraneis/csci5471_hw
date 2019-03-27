# Requirements
# - Num Components
# - Min/average/max cycle length
# - average/max tail length

from hashlib import sha256
from collections import defaultdict

class Graph(object):
  def __init__(self, function, min_val, max_val):
     self._graph = defaultdict(set)
     self.add_connections(function, min_val, max_val)
     self.terminal_points = self.find_indegree_one()
     self.cycle_points = []

  def get_terminal_pts(self):
      return self.terminal_points


  def add_connections(self, function, min_val, max_val):
      for i in range(min_val, max_val + 1):
          self.add(i, function(i))

  def add(self, node1, node2):
      self._graph[node1] = node2

  def __str__(self):
      return '{}({})'.format(self.__class__.__name__, dict(self._graph))

  def find_indegree_one(self):
      input_pts = []
      for k in self._graph.keys():
          if k not in self._graph.values():
              input_pts.append(k)
      return input_pts
  def cycle_register(self, point):
      if point in self.cycle_points:
          return True
      else:
          self.cycle_points.append(point)
          return False

def f(x):
    d = {13:7, 7:3, 5:3, 3:1,  1:4, 12:4, 4:6, 6:9, 9:1, 8:11, 11:10, 10:2, 2:11}
    return d[x]

def hash16(x):
    m = sha256()
    m.update(b"prane001")
    m.update(bytes(x, 'utf-8'))
    return m.digest()[-2:].hex()

def brent_algorithm(f, x0):
    power = cycleLength = 1
    tortoise = x0
    hare = f(x0)  # f(x0) is the element/node next to x0.
    while tortoise != hare:
        if power == cycleLength:  # time to start a new power of two?
            tortoise = hare
            power *= 2
            cycleLength = 0
        hare = f(hare)
        cycleLength += 1
    tailLength = 0
    tortoise = hare = x0
    for i in range(cycleLength):
        hare = f(hare)
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        tailLength += 1
    return cycleLength, tailLength

# inp = input("Enter string: ")
#inp = int(input("Enter string: "))
max_tail = 0
avg_tail = 0
max_cycle = 0
avg_cycle = 0
tailcounter = 0
cyclecounter = 0

min_cycle = float('inf')

test = Graph(f, 1, 13)
for i in test.get_terminal_pts():
    cycleLength, tailLength = brent_algorithm(f, int(i))

    if cycleLength > max_cycle:
        max_cycle= cycleLength
    if cycleLength < min_cycle:
        min_cycle = cycleLength
    if tailLength > max_tail:
        max_tail = tailLength

    avg_tail  += tailLength
    avg_cycle += cycleLength

    if tailLength != 0:
        tailcounter += 1
    cyclecounter +=1

# cycleLength,tailLength = brent_algorithm(f, inp)
print("max tailLength: " , max_tail)
print("max cycleLength: " , max_cycle)
print("avg tailLength: " , avg_tail / tailcounter)
print("avg cycleLength: " , avg_cycle /cyclecounter)
print("min cycleLength: ", min_cycle)
# print("num components: ", 10)




