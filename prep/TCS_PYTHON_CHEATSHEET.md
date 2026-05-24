# TCS AI Careers — Python Cheat Sheet
**Exam date:** Mon May 25, 2026 (48-hr window) · **Format:** 30 MCQs (30 min) + 1 Medium coding problem (30 min)
**Purpose:** Revise in 30-45 min. Skim once, then re-read flagged sections.

---

## 1. DATA TYPES & TRUTHINESS

```python
# Numbers
x = 10              # int
y = 3.14            # float
z = 1 + 2j          # complex
b = True            # bool (True/False — capital T/F)
n = None            # NoneType (singleton)

# Type checks
type(10)              # <class 'int'>
isinstance(10, int)   # True
isinstance(10, (int, float))   # True

# Casting
int("42"), float("3.14"), str(100), bool(0)
int(3.7)              # 3  (truncates)
int("0x1A", 16)       # 26
```

**Falsy values:** `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None`, `False`. **Everything else truthy.**

**`is` vs `==`:**
- `is` → identity (same object in memory)
- `==` → value equality
- **Always:** `if x is None`, NEVER `if x == None`

**Integer caching:** `a = 256; b = 256; a is b` → `True` (small int cache: -5 to 256).
`a = 257; b = 257; a is b` → `False` in CPython.

---

## 2. STRINGS

**Immutable.** Any "modification" creates a new string.

```python
s = "Hello"
s[0]          # 'H'
s[-1]         # 'o'
s[1:4]        # 'ell'
s[::-1]       # 'olleH'  ← reverse trick
len(s)        # 5

# Methods (return new string)
s.lower(), s.upper(), s.title(), s.capitalize()
s.strip(), s.lstrip(), s.rstrip()
s.replace("l", "L")           # "HeLLo"
s.split(",")                  # split by separator → list
"-".join(["a","b","c"])       # "a-b-c"
s.find("ll")                  # 2 (-1 if not found)
s.startswith("He"), s.endswith("lo")
s.count("l")                  # 2
s.isalpha(), s.isdigit(), s.isalnum(), s.isspace()
ord("A")                      # 65    (char → int)
chr(65)                       # "A"   (int → char)

# F-strings (Py 3.6+)
name = "Nara"; age = 25
f"{name} is {age}"            # "Nara is 25"
f"{3.14159:.2f}"              # "3.14"
f"{42:05d}"                   # "00042"  (zero-padded)
f"{1000000:,}"                # "1,000,000"
f"{0.85:.1%}"                 # "85.0%"
```

---

## 3. LIST — ordered, mutable, allows duplicates

```python
a = [1, 2, 3]
a.append(4)          # [1,2,3,4]              O(1)
a.insert(0, 0)       # [0,1,2,3,4]            O(n)
a.extend([5,6])      # [0,1,2,3,4,5,6]        O(k)
a.pop()              # removes & returns 6    O(1)
a.pop(0)             # removes & returns 0    O(n)
a.remove(2)          # removes first '2'      O(n)
a.index(3)           # index of 3             O(n)
a.count(1)           # count of 1             O(n)
3 in a               # membership             O(n)
a.sort()             # in-place sort          O(n log n)
a.sort(reverse=True, key=lambda x: -x)
sorted(a)            # new sorted list
a.reverse()          # in-place reverse
list(reversed(a))    # new reversed list
a.copy()             # shallow copy
del a[0]             # delete by index

# Slicing
a[2:5], a[:3], a[3:], a[::2], a[::-1]

# List comprehension
[x*2 for x in range(10)]
[x for x in range(10) if x % 2 == 0]
[(i,j) for i in range(3) for j in range(3)]    # nested
```

---

## 4. TUPLE — ordered, IMMUTABLE

```python
t = (1, 2, 3)
t = 1, 2, 3                # parens optional
single = (5,)              # single-element tuple needs comma!
empty = ()

# Unpacking
a, b, c = (1, 2, 3)
x, *rest = (1, 2, 3, 4)    # x=1, rest=[2,3,4]
*init, last = (1, 2, 3, 4) # init=[1,2,3], last=4
a, b = b, a                # swap

# Why tuples?
# - Faster than lists
# - Can be dict keys (lists can't — unhashable)
# - Function returning multiple values returns tuple
```

---

## 5. SET — unordered, unique, hashable elements

```python
s = {1, 2, 3, 2}     # {1,2,3} — duplicates removed
s = set([1,2,3])
empty = set()        # NOT {} (that's a dict)

s.add(4)
s.remove(1)          # KeyError if not present
s.discard(1)         # no error if not present
s.pop()              # remove arbitrary element
1 in s               # O(1)

# Set operations
a = {1,2,3}; b = {2,3,4}
a | b       # {1,2,3,4}  union
a & b       # {2,3}      intersection
a - b       # {1}        difference
a ^ b       # {1,4}      symmetric difference
a <= b      # subset?
```

---

## 6. DICT — key-value, O(1) avg lookup

```python
d = {"a": 1, "b": 2}
d = dict(a=1, b=2)

d["a"]                  # 1, KeyError if missing
d.get("c")              # None (safe)
d.get("c", 0)           # 0 (default)
d["c"] = 3              # add / update
del d["a"]              # delete key
"b" in d                # True (checks keys)
len(d)                  # 2

d.keys(), d.values(), d.items()

# Iterating
for k in d: ...
for k, v in d.items(): ...

# Merging
d.update({"x": 10})
{**d, **{"y": 20}}      # merge into new dict

# Comprehension
{k: v*2 for k, v in d.items()}
{x: x**2 for x in range(5)}

# Dict ordered since Python 3.7 (insertion order)
```

---

## 7. COLLECTIONS MODULE — MUST KNOW

```python
from collections import defaultdict, Counter, deque, namedtuple, OrderedDict

# defaultdict — auto-default for missing keys
dd = defaultdict(int)
for ch in "banana": dd[ch] += 1     # {'b':1,'a':3,'n':2}

dd = defaultdict(list)
dd["k"].append(1)                   # no KeyError

# Counter — count occurrences
c = Counter("banana")               # {'a':3,'n':2,'b':1}
c.most_common(2)                    # [('a',3),('n',2)]
c1 + c2, c1 - c2                    # arithmetic
c.elements()                        # iterator of all elements

# deque — O(1) appends/pops from BOTH ends
dq = deque([1,2,3])
dq.append(4); dq.appendleft(0)
dq.pop(); dq.popleft()              # all O(1)
dq.rotate(1)
deque(maxlen=5)                     # bounded queue

# namedtuple
Point = namedtuple("Point", ["x","y"])
p = Point(1, 2)
p.x, p[0]                           # both work
```

---

## 8. FUNCTIONS — args, kwargs, lambda

```python
def f(a, b=10, *args, **kwargs):
    pass

# *args  → collects extra positional into tuple
# **kwargs → collects extra keyword into dict

def add(*args):
    return sum(args)
add(1,2,3,4)                        # 10

def info(**kwargs):
    for k,v in kwargs.items(): print(k,v)

# Unpacking call
nums = [1,2,3]
add(*nums)                          # add(1,2,3)
d = {"a":1,"b":2}
f(**d)                              # f(a=1,b=2)

# Lambda — single expression only
square = lambda x: x**2
sorted(items, key=lambda x: x[1])

# Higher-order
list(map(lambda x: x*2, [1,2,3]))      # [2,4,6]
list(filter(lambda x: x>0, [-1,0,1]))  # [1]
from functools import reduce
reduce(lambda a,b: a+b, [1,2,3,4])     # 10
```

### ⚠️ MUTABLE DEFAULT ARGS — CLASSIC TRAP

```python
def bad(lst=[]):     # ← BAD: shared across calls!
    lst.append(1)
    return lst
bad()  # [1]
bad()  # [1,1]   ← surprise

def good(lst=None):
    lst = lst or []
    lst.append(1)
    return lst
```

---

## 9. OOP — heavy MCQ area

```python
class Animal:
    species = "Animal"              # CLASS variable (shared)

    def __init__(self, name, age):
        self.name = name            # instance variable
        self.age = age

    def speak(self):
        return f"{self.name} makes a sound"

    # Dunder methods
    def __str__(self):  return f"Animal({self.name})"
    def __repr__(self): return f"Animal(name={self.name!r})"
    def __eq__(self, other): return self.name == other.name
    def __hash__(self): return hash(self.name)
    def __len__(self): return self.age
    def __lt__(self, other): return self.age < other.age
    def __add__(self, other): return Animal(self.name + other.name, ...)

    @classmethod
    def from_string(cls, s):        # alternative constructor
        return cls(s, 0)

    @staticmethod
    def is_valid_age(age):
        return age >= 0


# Inheritance
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):                # override (polymorphism)
        return f"{self.name} barks"


# Multiple Inheritance + MRO
class A:
    def hi(self): return "A"
class B(A):
    def hi(self): return "B"
class C(A):
    def hi(self): return "C"
class D(B, C): pass

D().hi()        # "B" — follows MRO
D.__mro__       # (D, B, C, A, object)


# Encapsulation
class Account:
    def __init__(self, b):
        self._balance = b           # convention: protected
        self.__secret = "x"         # name-mangled (truly private-ish)
                                    # access via acc._Account__secret

    @property                       # getter
    def balance(self): return self._balance

    @balance.setter                 # setter with validation
    def balance(self, v):
        if v < 0: raise ValueError
        self._balance = v


# Abstract Base Class
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r**2

# Shape()       # TypeError — can't instantiate abstract
```

### ⚠️ Key OOP MCQ facts

- **`__init__`** initializes; **`__new__`** creates. `__new__` runs first.
- **`@classmethod`** receives `cls`; **`@staticmethod`** receives neither.
- **MRO** uses C3 linearization (left-to-right depth-first, but ensures consistency).
- **`super()`** calls parent's method.
- **Multiple inheritance** — use `super()` to follow MRO properly.
- **Class vs Instance variables:** modifying `cls.var` affects all; modifying `self.var` creates instance-specific.

---

## 10. DECORATORS — frequent MCQ topic

```python
import functools

def my_decorator(func):
    @functools.wraps(func)          # preserves __name__, __doc__
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper

@my_decorator
def hello(name):
    return f"Hi {name}"

# Equivalent to: hello = my_decorator(hello)


# Decorator with arguments
def repeat(n):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return deco

@repeat(3)
def hi(): print("hi")
```

---

## 11. GENERATORS & ITERATORS

```python
# Generator function — uses 'yield'
def count_up(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up(3)
next(gen)            # 1
next(gen)            # 2
next(gen)            # 3
next(gen)            # raises StopIteration

# Generator expression
sq = (x**2 for x in range(10))      # lazy, low memory

# Iterator protocol — class implementing __iter__ + __next__
class CountUp:
    def __init__(self, n):
        self.n, self.i = n, 0
    def __iter__(self): return self
    def __next__(self):
        if self.i >= self.n: raise StopIteration
        self.i += 1
        return self.i

# Key facts:
# - All iterators are iterables (have __iter__)
# - Generator IS an iterator
# - Generators are LAZY → memory efficient for big sequences
# - Exhausted after one full iteration (can't reuse)
```

---

## 12. EXCEPTION HANDLING

```python
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(e)
except (TypeError, ValueError) as e:     # multiple
    print(e)
except Exception as e:                   # catch-all
    print(e)
else:
    print("no exception")                # runs only if no exception
finally:
    print("always runs")                 # always runs (cleanup)

# Raising
raise ValueError("bad value")
raise                                     # re-raise current
raise NewError("...") from original_err   # chain

# Custom
class MyError(Exception):
    pass

# Common built-ins
# TypeError, ValueError, KeyError, IndexError, AttributeError,
# FileNotFoundError, ZeroDivisionError, NameError, ImportError
```

---

## 13. FILE I/O & JSON

```python
# File
with open("file.txt", "r") as f:          # auto-close
    content = f.read()
    lines = f.readlines()
    for line in f: ...                    # memory-efficient

with open("out.txt", "w") as f:
    f.write("hello\n")
    f.writelines(["a\n", "b\n"])

# Modes: r, w, a, rb, wb, r+ (read+write)

# JSON
import json
json.dumps(obj)              # obj → str
json.loads(s)                # str → obj
json.dump(obj, f)            # obj → file
json.load(f)                 # file → obj
```

---

## 14. COMMON PYTHON IDIOMS

```python
# Swap
a, b = b, a

# Enumerate
for i, x in enumerate(items, start=1): ...

# Zip
for a, b in zip(list1, list2): ...
dict(zip(keys, values))

# Sorting
sorted(items, key=lambda x: x[1])
sorted(items, key=lambda x: (x[0], -x[1]))   # multi-key

# All / any
all([1, 2, 3])      # True (all truthy)
any([0, 0, 1])      # True (at least one truthy)

# Chained comparisons
if 1 < x < 10: ...

# Walrus (Py 3.8+)
if (n := len(data)) > 10:
    print(n)

# Range
range(5)             # 0,1,2,3,4
range(2, 10)         # 2..9
range(0, 10, 2)      # 0,2,4,6,8
range(10, 0, -1)     # 10,9,...,1
```

---

## 15. TIME COMPLEXITY — MCQ MUST-KNOW

| Operation | List | Dict | Set | Tuple |
|---|---|---|---|---|
| Access by index | O(1) | — | — | O(1) |
| Lookup key | — | O(1) avg | O(1) avg | — |
| `in` (membership) | O(n) | O(1) | O(1) | O(n) |
| Append/Add | O(1) | O(1) | O(1) | — |
| Insert at front | O(n) | — | — | — |
| Pop end | O(1) | — | — | — |
| Pop front | O(n) | — | — | — |
| Delete by key/index | O(n) | O(1) | O(1) | — |
| Iterate | O(n) | O(n) | O(n) | O(n) |

| Algorithm | Time |
|---|---|
| Linear search | O(n) |
| Binary search | O(log n) |
| Bubble/selection/insertion sort | O(n²) |
| Merge sort / heap sort | O(n log n) |
| Python's `sort()` (Timsort) | O(n log n) |
| Quick sort (avg / worst) | O(n log n) / O(n²) |

---

## 16. PYTHON GOTCHAS (MCQ TRAPS)

```python
# 1. Mutable default arg (see Section 8)

# 2. Late binding closures
funcs = [lambda x: x*i for i in range(3)]
[f(1) for f in funcs]              # [2,2,2] (NOT [0,1,2])
# Fix: lambda x, i=i: x*i

# 3. Integer caching
a, b = 256, 256
a is b                              # True
a, b = 257, 257
a is b                              # False (but a == b is True)

# 4. String interning
a = "hello"; b = "hello"
a is b                              # usually True (interned)
a = "hello world!"; b = "hello world!"
a is b                              # often False

# 5. Copy
import copy
b = a              # alias (same object)
b = a.copy()       # shallow copy (nested objs still shared)
b = copy.deepcopy(a)   # fully independent

# 6. Tuple of one
(1)        # int
(1,)       # tuple

# 7. List multiplication
a = [[0]*3]*3       # all rows are SAME object!
a[0][0] = 1         # → [[1,0,0],[1,0,0],[1,0,0]]
# Fix: [[0]*3 for _ in range(3)]

# 8. Global vs nonlocal
x = 1
def f():
    x = 2           # local x (shadows global)
def g():
    global x
    x = 2           # modifies global

def outer():
    y = 1
    def inner():
        nonlocal y    # modifies outer's y
        y = 2

# 9. Boolean is subtype of int
True + True         # 2
isinstance(True, int)  # True

# 10. Division
7 / 2               # 3.5 (true division)
7 // 2              # 3   (floor division)
7 % 2               # 1   (modulo)
2 ** 10             # 1024 (power)
```

---

## 17. GIL & CONCURRENCY (MCQ TOPIC)

- **GIL** = Global Interpreter Lock. Only ONE thread executes Python bytecode at a time.
- Threading: good for I/O-bound (GIL released during I/O)
- Multiprocessing: good for CPU-bound (separate processes, each has own GIL)
- asyncio: single-thread cooperative concurrency (event loop)

| Type | Best for | Bypasses GIL? |
|---|---|---|
| `threading` | I/O bound (file, network) | No |
| `multiprocessing` | CPU bound (math) | Yes |
| `asyncio` | Many I/O concurrent | No (cooperative) |

---

## 18. CODING PROBLEM — TEMPLATES TO MEMORIZE

### Pattern 1: HashMap counting
```python
from collections import Counter
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target-x], i]
        seen[x] = i
```

### Pattern 2: Sliding Window
```python
def longest_substring_no_repeat(s):
    seen = {}
    left = best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best
```

### Pattern 3: Two Pointers
```python
def reverse_words(s):
    arr = list(s)
    l, r = 0, len(arr)-1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1; r -= 1
    return "".join(arr)
```

### Pattern 4: Stack (parentheses)
```python
def valid_parens(s):
    pairs = {")":"(", "]":"[", "}":"{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack
```

### Pattern 5: Sort + scan
```python
def merge_intervals(intervals):
    intervals.sort()
    out = []
    for s, e in intervals:
        if out and s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return out
```

### Pattern 6: Counter + heap
```python
import heapq
from collections import Counter
def top_k_frequent(nums, k):
    return [x for x, _ in Counter(nums).most_common(k)]
```

### Pattern 7: BFS (grid / graph)
```python
from collections import deque
def bfs_grid(grid, start):
    rows, cols = len(grid), len(grid[0])
    visited = set([start])
    q = deque([start])
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                visited.add((nr,nc))
                q.append((nr,nc))
    return visited
```

### Pattern 8: Recursion + memoization
```python
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)
```

---

## 19. INPUT/OUTPUT FOR CODING TESTS — CRITICAL

```python
# Single int
n = int(input())

# Space-separated ints on one line
nums = list(map(int, input().split()))

# String
s = input().strip()

# N lines of strings
lines = [input().strip() for _ in range(n)]

# Matrix
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Output
print(result)
print(*arr)                      # space-separated
print("\n".join(map(str, arr)))  # newline-separated
print(f"{a} {b}")
```

⚠️ **TCS coding test gotchas:**
- Trim whitespace: `input().strip()`
- Output EXACTLY what's expected (no extra newlines, no extra spaces)
- Read problem statement TWICE before coding
- Test with public test cases BEFORE submit

---

## 20. EXAM-DAY STRATEGY

### Time allocation per section (105 min total)
| Section | Time | Strategy |
|---|---|---|
| Numerical Aptitude (10 Qs) | 10 min | ~1 min/Q; skip & guess if stuck >45sec |
| Logical Reasoning (10 Qs) | 10 min | Same — speed > perfection |
| Verbal Ability (10 Qs) | 10 min | Same |
| Spoken Communications (2 Qs) | 15 min | Speak full duration; clear + simple sentences |
| Programming MCQ (30 Qs) | 30 min | 1 min/Q max; flag tricky, return at end |
| Coding (1 problem) | 30 min | 5 min understanding → brute force → test → optimize |

### Coding problem flow (30 min)
1. **0-5 min:** Read problem TWICE. Identify input/output format. Note constraints.
2. **5-10 min:** Write brute-force solution mentally / on paper.
3. **10-22 min:** Code it. Use simple `for` loops + dicts/sets. Don't over-engineer.
4. **22-26 min:** Test against PUBLIC test cases. Fix bugs.
5. **26-30 min:** Optimize if needed. Submit.

### Don't do
- ❌ Don't press F5 / refresh
- ❌ Don't switch tabs
- ❌ Don't use Windows key
- ❌ Don't look away from screen for long stretches
- ❌ Don't speak / read aloud during exam
- ❌ Don't leave webcam frame

### Do
- ✅ Keep webcam on, face visible
- ✅ Plain background
- ✅ Phone OFF and AWAY
- ✅ Water nearby (don't leave seat)
- ✅ Stay calm if stuck — move on, return later (within section)

---

## 21. LAST 5 MINUTES BEFORE EXAM

1. ✅ Wash face, hydrate, deep breath
2. ✅ Verify webcam + mic working
3. ✅ Antivirus OFF, firewall OFF
4. ✅ All other apps closed (Slack, Teams, etc.)
5. ✅ Phone silent, face-down, OUT of camera frame
6. ✅ Notepad + pen for rough work (visible to camera!)
7. ✅ Login credentials handy
8. ✅ Browser zoom = 100% (Ctrl+0)

---

## ✅ Final mindset

- This is **not the hardest exam you've ever taken**. You've cleared Stage 1.
- The coding problem is **medium**, not hard. Your RAG project shows you can code.
- **Programming MCQs (30 marks) + Coding (50 marks) = 80 marks** — your strength area.
- Aptitude is **bonus** — don't stress if you guess a few.
- **Spoken English** — speak naturally, you've done this format for IBM SHL test.

**You're prepared. Go take it.**

---

> *Last updated: May 24, 2026 · For TCS AI Careers Stage 2 Python exam · 105 min · 30 MCQ + 1 Coding*
