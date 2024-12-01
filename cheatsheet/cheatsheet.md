
## init
### inf
```python
float('inf')
```
array with 0
```python
row = [0] * n
```
2d array

```python
dp = [[0] * n for _ in range(m)]
```
## Queue
```python
import queue

q = queue.Queue()

q.put(1)
q.get()
```
```python
# faster queue
q = [1]
for a in q: # get
#...
q.append(2) # put
```
### DeQue
```python
q = collections.deque([(beginWord, 1)])

while q:
cur, level = q.popLeft()
#...
q.append(('', 0))
```
## Stack
```python
stack = []

stack.append(1) # push
a = stack.pop()
```
## List
### flat list of list
```python
l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
flat_list = [item for sublist in l for item in sublist]

flat_list
# >>> [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
### Heap
```python
import heapq

nums = []
heapq.heappush(nums, 1) # min heap
heapq.heappush(nums, -1) # max heap

nums[0] # top element
heapq.heappop(nums) # pop first element
```
### Bisect
```python
import bisect
nums = [1, 4, 4, 6, 8]
>>> bisect.bisect_left(nums, 3) # locate the insertion point for x
>>> 1 # insertion point for 3

>>> bisect.bisect_left(nums, 4)
>>> 1

>>> bisect.bisect_right(nums, 4) # gives what after all existing x entries
>>> 3
```
### Sort
```python
a = [(1, 2), (3, 3), (2, 1)]
a.sort(key=lambda x: x[0], reverse=True)

--------------------
def get_key(log):
_id, rest = log.split(" ", maxsplit=1)
return (0, rest, _id) if rest[0].isalpha() else (1, )

return sorted(logs, key=get_key)
```
### Quick Select
```python
nums = [3, 1, 5, 4, 2]

def partition(left, right, pivot):
  pivot_value = nums[pivot]

  nums[pivot], nums[right] = nums[right], nums[pivot]
  i = left
  for j in range(left, right):
    if nums[j] <= nums[pivot]:
      nums[i], nums[j] = nums[j], nums[i]
      i += 1
      nums[i], nums[right] = nums[right], nums[i]
  return i

def quick_select(left, right, k_smallest):
  pivot = random.randint(left, right)
  pivot = partition(left, right, pivot)

  if pivot == k_smallest:
    return pivot
  elif pivot > k_smallest:
    return quick_select(left, pivot-1, k_smallest)
  else:
    return quick_select(pivot+1, right, k_smallest)
```
## Set
```python
visited = set()

visited.add(1)
if 1 not in visited:
# do
```
### Combinations
```python
from itertools import combinations

def combinations(iterable, r):
# combinations('ABCD', 2) --> AB AC AD BC BD CD
# combinations(range(4), 3) --> 012 013 023 123
```
## Dict / Map
## Init
### DefaultDict
```python
from collections import defaultdict
s = 'mississippi'
d = defaultdict(int)
for k in s:
d[k] += 1
d.items()
>>> [('i', 4), ('p', 2), ('s', 4), ('m', 1)]
```
```python
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
d[k].append(v)

d.items()
>>> [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```
### normal dict
```python
dict = { i: set() for i in range(10) }
```
iterate through

```python
for k, v in d.items():
print (f"{k} - {v}")
```
sort by value or number of values

```python
sorted(d.items(), key=lambda x: x[1]).pop(0)[0]
sorted(d.items(), key=lambda x: len(x[1])).pop(0)[0]
```
### OrderedDict (LinkedHashMap)
```python
d = OrderedDict()
d['a'] = 1
d['c'] = 3
- >>> d
OrderedDict([('a', 1), ('c', 3)])
- d.move_to_end('a')
- >>> d
OrderedDict([('c', 3), ('a', 1)])
```
### Counter
```python
nuns = [1, 2, 2, 3, 4, 4, 4, 5]
counts = collections.Counter(nums)
- >>> counts[4]
3
```
## Functional Programming
### map
```python
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

s = 'adf, sdadka;;!'
newStr = ''.join(map(lambda c: c.lower() if c.isalnum() else '', s))
```
### filter
```python
filtered_words = list(filter(lambda word: word != "", raw_words))
```
## String
```python
isalnum() # includes
* isnumeric() # number
* isalpha() # alphabet
* isdecimal() 
* isdigit()

'AA'.lower()
```
## Trie
```python
class Trie:

def __init__(self):
  self.root = {}
  self.END = '_END'
    

def insert(self, word: str) -> None:
  cur = self.root
  for c in word:
    cur = cur.setdefault(c, {})
  cur[self.END] = self.END
    

def search(self, word: str) -> bool:
  cur = self.root
  for c in word:
    if c in cur:
      cur = cur[c]
    else:
      return False

  return self.END in cur       

def startsWith(self, prefix: str) -> bool:
  cur = self.root
  for c in prefix:
    if c in cur:
      cur = cur[c]
    else:
      return False

  return Truedef __init__(self):
self.END = '_end_'

------------------------------------------------------------

def make_trie(self, words: List[str]) -> dict[str, dict]:
root = {}
for word in words:
cur_dict = root
for c in word:
  cur_dict = cur_dict.setdefault(c, {})
cur_dict[self.END] = self.END
return root

def in_trie(self, root: dict[str, dict], c: str):
cur_dict = root
if c not in cur_dict:
return False, False, None
cur_dict = cur_dict[c]
return True, self.END in cur_dict, cur_dict


def remove_word(self, root: dict[str, dict], word: str):
if len(word) == 0:
return

cur_dict = root
if word[0] in cur_dict:
if len(word) == 1 and self.END in cur_dict[word[0]]:
  del cur_dict[word[0]][self.END]
self.remove_word(cur_dict[word[0]], word[1:])
if len(cur_dict[word[0]]) == 0:
  del cur_dict[word[0]]
```
## Longest Increasing Subsequence
```python
def lengthOfLIS(self, nums: List[int]) -> int:
  sub = []
  for num in nums:
    i = bisect_left(sub, num)
    if i == len(sub):
      sub.append(num)
    else:
      sub[i] = num

  return len(sub)
```
## Graph
### Clone Graph
```python
def __init__(self):
self.visited = {}

def cloneGraph(self, node: 'Node') -> 'Node':
  if not node:
    return None

  if node in self.visited:
    return self.visited[node]

  clone = Node(node.val, [])

  self.visited[node] = clone

  for next in node.neighbors:
    clone.neighbors.append(self.cloneGraph(next))

  return clone
```
### Topological Sorting
```python
ingress = Counter()

g = defaultdict(list)

for source, dest in edges:
  g[source].append(dest)
  ingress[dest] += 1

queue = [dest for dest in ingress if ingress[dest] == 0]

ret = []
for x in queue:
  ret.append(x)
  
  for next in g[x]:
    ingress[next] -= 1
    if ingress[next] == 0:
      queue.append(next)

return ret
```