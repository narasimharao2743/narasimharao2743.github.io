# Prowesssoft Interview Prep — Narasimharao Bhavirisetty

---

## About Prowesssoft (Prowess Software Services)

| Detail | Info |
|---|---|
| Founded | 2016 (Bootstrapped, profitable) |
| HQ | Hyderabad, India (Kukatpally) |
| Offices | Hyderabad, Bengaluru, Atlanta (USA), Singapore |
| Employees | ~350–400 |
| Revenue | ~₹106 Crore (~$13M USD) as of 2025 |
| Glassdoor Rating | 3.9 / 5 |

**What they do:** Enterprise IT integration — connecting company systems using MuleSoft, Kafka, APIs. They are a **MuleSoft Premier Partner** (top tier, won Partner of the Year 2024 & 2025 in Americas). They serve Finance, Healthcare, Retail, and Logistics clients worldwide (Fortune 500 companies).

### Your Fit vs Their Stack

| Your Skills | Their Stack | Match? |
|---|---|---|
| Kafka | Kafka (Enterprise Event Streaming) | Strong match |
| REST APIs / Flask | API Integration & Management | Good match |
| Python | Java is primary, Python secondary | Partial |
| PyFlink / Stream Processing | Kafka-based event-driven arch | Relevant |
| ClickHouse / Redis | Not their core, but data layer | Partial |
| MuleSoft | Not on your resume | Gap |
| Salesforce | Not on your resume | Gap |

### What to Expect in the Interview

1. **Kafka deep-dive** — consumer groups, offsets, deduplication, fault tolerance
2. **Python OOP & backend** — standard Python questions, REST API design with Flask
3. **System Design** — "Design a real-time data pipeline" (you've built this — Solana/Kafka/ClickHouse)
4. **Why Prowesssoft?** — "I've been working with event-driven architectures and Kafka — integration is the next natural step."

### Company Culture (Glassdoor)
- Pros: Good learning environment, senior engineers accessible, "Great Place to Work" certified
- Cons: Fast-paced, employees handle many responsibilities
- 67% rate interviews as positive

---

## Key Interview Questions Quick Reference

| Question | Answer |
|---|---|
| `list` vs `tuple` | List: mutable, unhashable. Tuple: immutable, hashable (usable as dict key) |
| `==` vs `is` | `==` value equality, `is` identity (same object in memory) |
| `deepcopy` vs `copy` | `copy`: new object but nested refs shared. `deepcopy`: fully independent clone |
| What is GIL? | Mutex allowing only 1 thread to run Python bytecode at a time. Released during I/O. |
| `@classmethod` vs `@staticmethod` | classmethod gets `cls`, staticmethod gets neither. classmethod used for alternate constructors. |
| What is a generator? | Function using `yield`. Lazy — produces values one at a time without storing all in memory. |
| What is a closure? | Inner function that remembers variables from enclosing scope even after outer function returns. |
| `__str__` vs `__repr__` | `__str__`: user-friendly (for print). `__repr__`: developer string (for debugging, unambiguous). |
| How does `dict` work? | Hash table. Average O(1) get/set. Keys must be hashable. |
| `*args` vs `**kwargs` | `*args`: positional → tuple. `**kwargs`: keyword → dict. |
| MRO | C3 linearization algorithm. `Dog.__mro__` shows the order Python looks for methods. |
| `__new__` vs `__init__` | `__new__` creates the instance, `__init__` initializes it. |
| `None` check | Always `if x is None`, never `if x == None` |
| Mutable default argument | Bug trap: `def f(lst=[])` shares same list. Use `def f(lst=None): lst = lst or []` |

---

# Complete Python Brush-Up

---

## 1. Data Types & Variables

```python
# Integers
x = 10
y = 0b1010    # binary = 10
z = 0xFF      # hex = 255
big = 1_000_000  # underscore for readability

# Floats
f = 3.14
f2 = 1.5e3    # 1500.0

# Strings (immutable)
s = "hello"
s3 = """multi
line"""

# Boolean
print(int(True))   # 1
print(int(False))  # 0

# None
x = None
print(x is None)   # True  <- always use 'is' for None

# Type checking
print(type(42))                      # <class 'int'>
print(isinstance(42, int))           # True
print(isinstance(42, (int, float)))  # True — checks multiple types
```

---

## 2. Strings (Deep Dive)

```python
s = "Narasimharao"

# Indexing & Slicing
print(s[0])      # 'N'
print(s[-1])     # 'o'
print(s[0:5])    # 'Naras'
print(s[::2])    # every 2nd char
print(s[::-1])   # reverse

# String methods
print(s.upper())
print(s.lower())
print(s.strip())           # remove whitespace both ends
print(s.replace("Rao", "Kumar"))
print(s.split(","))        # returns list
print(",".join(["a","b","c"]))   # 'a,b,c'
print(s.startswith("Nara"))      # True
print(s.endswith("rao"))         # True
print(s.find("sim"))       # index of first match, -1 if not found
print(s.count("a"))        # count occurrences
print("123".isdigit())     # True
print(s.isalpha())         # True

# Formatting
name = "Rao"
age = 25

# f-string (preferred, Python 3.6+)
print(f"Name: {name}, Age: {age}")
print(f"Price: {3.14159:.2f}")   # 2 decimal places
print(f"{'left':<10}|")          # left-align in width 10
print(f"{'right':>10}|")         # right-align

# .format()
print("Name: {}, Age: {}".format(name, age))

# % formatting (old style, still asked)
print("Name: %s, Age: %d" % (name, age))

# Raw strings
path = r"C:\Users\Rao\file.txt"   # backslash not escaped
```

---

## 3. Lists

```python
lst = [1, 2, 3, 4, 5]

# Modification (lists are MUTABLE)
lst.append(6)          # add to end
lst.insert(0, 0)       # insert at index
lst.extend([7, 8])     # add multiple
lst.remove(3)          # remove first occurrence of value
popped = lst.pop()     # remove & return last
popped = lst.pop(0)    # remove & return at index
lst.clear()            # empty the list

# Searching
lst = [3, 1, 4, 1, 5, 9]
print(3 in lst)        # True
print(lst.index(4))    # 2
print(lst.count(1))    # 2

# Sorting
lst.sort()             # in-place, modifies original
lst.sort(reverse=True)
new = sorted(lst)      # returns new list, original unchanged
lst.reverse()          # in-place reverse

# Copy — IMPORTANT INTERVIEW TOPIC
a = [1, [2, 3], 4]
b = a               # SAME reference, NOT a copy
c = a.copy()        # shallow copy
d = a[:]            # also shallow copy
import copy
e = copy.deepcopy(a)  # deep copy — copies nested objects too

b.append(99)        # modifies a too!
c[1].append(99)     # modifies a[1] too! (shallow)
e[1].append(99)     # does NOT modify a (deep)

# Unpacking
a, b, c = [1, 2, 3]
first, *rest = [1, 2, 3, 4, 5]   # first=1, rest=[2,3,4,5]
*init, last = [1, 2, 3, 4, 5]    # init=[1,2,3,4], last=5
```

---

## 4. Tuples

```python
# Immutable lists
t = (1, 2, 3)
single = (1,)     # MUST have trailing comma for single element

# Can be used as dict keys (because hashable)
d = {(1, 2): "point"}

# Named tuple
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)   # 3 4
print(p[0])       # 3 (index access still works)
```

---

## 5. Dictionaries

```python
d = {"name": "Rao", "age": 25}

# Access
print(d["name"])              # KeyError if missing
print(d.get("name"))          # None if missing
print(d.get("city", "N/A"))   # default if missing

# Modification
d["city"] = "Bangalore"
d.update({"age": 26, "role": "Engineer"})
del d["city"]
removed = d.pop("age")
d.setdefault("score", 0)    # sets only if key doesn't exist

# Iteration
for key in d: pass
for key, value in d.items(): pass
for key in d.keys(): pass
for val in d.values(): pass

# Merging (Python 3.9+)
merged = {"a": 1} | {"b": 2}    # {"a": 1, "b": 2}

# Dict comprehension
squares = {x: x**2 for x in range(5)}
inverted = {v: k for k, v in d.items()}  # swap keys/values

# Nested dict
config = {
    "kafka": {"host": "localhost", "port": 9092},
    "redis": {"host": "localhost", "port": 6379}
}
print(config["kafka"]["port"])  # 9092
```

---

## 6. Sets

```python
s = {1, 2, 3, 4}
empty_set = set()   # NOT {} <- {} creates empty dict!

# Operations
s.add(5)
s.remove(3)         # KeyError if not found
s.discard(99)       # no error if not found

# Set math
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)        # union         {1,2,3,4,5,6}
print(a & b)        # intersection  {3,4}
print(a - b)        # difference    {1,2}
print(a ^ b)        # symmetric diff {1,2,5,6}

# Membership O(1) — much faster than list
print(3 in s)

# frozenset — immutable set, can be dict key
fs = frozenset([1, 2, 3])
```

---

## 7. Control Flow

```python
# Ternary
result = "even" if x % 2 == 0 else "odd"

# enumerate
for i, fruit in enumerate(["apple", "banana"], start=1):
    print(i, fruit)

# zip
for name, age in zip(["Rao","Ram"], [25,30]):
    print(name, age)

# break / continue / else on loop
for i in range(10):
    if i == 3: continue
    if i == 7: break
    print(i)
else:
    print("loop completed without break")  # won't print (we broke)
```

---

## 8. Functions

```python
# Default arguments
def power(base, exp=2):
    return base ** exp

# *args and **kwargs
def func(*args, **kwargs):
    print(args)    # tuple
    print(kwargs)  # dict

func(1, 2, name="Rao")

# Keyword-only arguments (after *)
def connect(host, port, *, timeout=30):
    pass

connect("localhost", 9092, timeout=60)

# Lambda
square = lambda x: x ** 2
data = [{"name": "Rao", "age": 25}, {"name": "Ram", "age": 22}]
data.sort(key=lambda x: x["age"])

nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
doubled = list(map(lambda x: x * 2, nums))

from functools import reduce
product = reduce(lambda x, y: x * y, nums)  # 120

# Unpacking when calling
def total(*args): return sum(args)
print(total(*[1, 2, 3]))         # unpack list as args

config = {"name": "Rao", "age": 25}
# create_user(**config)           # unpack dict as kwargs
```

---

## 9. Scope & Closures

```python
# LEGB Rule: Local -> Enclosing -> Global -> Built-in

# global keyword
count = 0
def increment():
    global count
    count += 1

# nonlocal keyword
def counter():
    n = 0
    def inc():
        nonlocal n
        n += 1
        return n
    return inc

c = counter()
print(c())  # 1
print(c())  # 2  <- closure remembers 'n'

# Closure
def multiplier(factor):
    def multiply(x):
        return x * factor   # 'factor' remembered
    return multiply

double = multiplier(2)
print(double(5))   # 10
```

---

## 10. Comprehensions

```python
# List
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
flat = [x for row in [[1,2],[3,4]] for x in row]  # flatten

# Dict
d = {k: v for k, v in zip("abc", [1,2,3])}
inverted = {v: k for k, v in d.items()}

# Set
unique_squares = {x**2 for x in [-2,-1,0,1,2]}  # {0,1,4}

# Generator expression (lazy — memory efficient)
gen = (x**2 for x in range(1_000_000))  # nothing computed yet
print(next(gen))  # 0
print(next(gen))  # 1
```

---

## 11. Iterators & Generators

```python
# Iterator protocol
class Range:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

for i in Range(1, 4):
    print(i)   # 1 2 3

# Generator function
def countdown(n):
    while n > 0:
        yield n         # pause here, return n
        n -= 1          # resume from here next time

# yield from
def chain(*iterables):
    for it in iterables:
        yield from it

print(list(chain([1,2], [3,4])))  # [1,2,3,4]

# Practical: read large file line-by-line
def read_large_file(filepath):
    with open(filepath) as f:
        for line in f:
            yield line.strip()

# Generator with send()
def accumulator():
    total = 0
    while True:
        value = yield total
        total += value

gen = accumulator()
next(gen)           # prime the generator
print(gen.send(10)) # 10
print(gen.send(20)) # 30
```

---

## 12. Decorators

```python
import functools

# Basic decorator
def my_decorator(func):
    @functools.wraps(func)    # preserves __name__, __doc__
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Decorator with arguments
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet():
    print("Hi!")

# Timer decorator
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} ran in {time.perf_counter()-start:.4f}s")
        return result
    return wrapper

# Retry decorator
def retry(times=3, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == times - 1:
                        raise
                    print(f"Retry {attempt+1}/{times}: {e}")
        return wrapper
    return decorator

@retry(times=3, exceptions=(ConnectionError,))
def call_api():
    pass

# Stacking decorators
@timer
@retry(times=3)
def my_func():
    pass
# Applied bottom-up: retry wraps my_func first, then timer wraps retry
```

---

## 13. Context Managers

```python
# Class-based
class DatabaseConnection:
    def __init__(self, url):
        self.url = url

    def __enter__(self):
        # self.conn = connect(self.url)
        return self  # this is what 'as' gets

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.conn.close()
        return False   # False = don't suppress exceptions

with DatabaseConnection("localhost") as conn:
    pass

# Generator-based (simpler)
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    try:
        yield
    finally:
        print(f"Took {time.time()-start:.3f}s")

with timer():
    import time
    time.sleep(0.1)

# Multiple context managers
with open("in.txt", "w") as fin, open("out.txt", "w") as fout:
    fout.write("hello")

# suppress — ignore specific exceptions
from contextlib import suppress
import os
with suppress(FileNotFoundError):
    os.remove("nonexistent.txt")
```

---

## 14. OOP — Complete

```python
class Animal:
    species_count = 0   # class variable (shared across all instances)

    def __init__(self, name, age):
        self.name = name    # instance variable
        self.age = age
        Animal.species_count += 1

    def speak(self):
        raise NotImplementedError("Subclass must implement")

    @classmethod
    def get_count(cls):
        return cls.species_count

    @staticmethod
    def is_valid_age(age):
        return 0 <= age <= 150

    @property
    def info(self):
        return f"{self.name} ({self.age})"

    # Dunder methods
    def __str__(self):
        return f"Animal: {self.name}"

    def __repr__(self):
        return f"Animal(name={self.name!r}, age={self.age!r})"

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.age < other.age

    def __len__(self):
        return self.age


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# Polymorphism
animals = [Dog("Rex", 3, "Lab"), Cat("Whiskers", 5)]
for animal in animals:
    print(animal.speak())

# isinstance vs type
dog = Dog("Rex", 3, "Lab")
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True (inherits)
print(type(dog) == Dog)         # True
print(type(dog) == Animal)      # False (type is exact)

# Multiple Inheritance & MRO
class A:
    def method(self): print("A")

class B(A):
    def method(self):
        print("B")
        super().method()

class C(A):
    def method(self):
        print("C")
        super().method()

class D(B, C):
    def method(self):
        print("D")
        super().method()

D().method()      # D -> B -> C -> A
print(D.__mro__)
```

---

## 15. Abstract Classes

```python
from abc import ABC, abstractmethod

class Pipeline(ABC):
    @abstractmethod
    def process(self, event: dict) -> dict:
        pass

    @abstractmethod
    def validate(self, event: dict) -> bool:
        pass

    def run(self, event):
        if self.validate(event):
            return self.process(event)
        raise ValueError("Invalid event")

class TradePipeline(Pipeline):
    def process(self, event):
        return {"processed": True, **event}

    def validate(self, event):
        return "symbol" in event and "price" in event
```

---

## 16. Exception Handling

```python
# Exception hierarchy
# BaseException
#   SystemExit, KeyboardInterrupt
#   Exception
#     ValueError, TypeError, KeyError, IndexError,
#     AttributeError, NameError, RuntimeError, IOError, StopIteration

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Math error: {e}")
except (ValueError, TypeError) as e:
    print(f"Value/Type error: {e}")
except Exception as e:
    print(f"Unexpected: {e}")
    raise              # re-raise same exception
else:
    print("No exception occurred")
finally:
    print("Always runs")

# Custom exceptions
class PipelineError(Exception):
    def __init__(self, message, event_id=None, retry=False):
        super().__init__(message)
        self.event_id = event_id
        self.retry = retry

class ValidationError(PipelineError):
    pass

# Exception chaining
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("Failed to parse config") from e
```

---

## 17. File I/O

```python
# Writing
with open("data.txt", "w") as f:   # 'w' overwrites
    f.write("Hello\n")
    f.writelines(["line1\n", "line2\n"])

with open("data.txt", "a") as f:   # 'a' appends
    f.write("New line\n")

# Reading
with open("data.txt") as f:
    content = f.read()          # entire file as string

with open("data.txt") as f:
    for line in f:              # memory efficient
        print(line.strip())

# JSON
import json
data = {"name": "Rao", "events": [1, 2, 3]}

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data.json") as f:
    loaded = json.load(f)

json_str = json.dumps(data)     # dict -> string
parsed = json.loads(json_str)   # string -> dict

# pathlib
from pathlib import Path
p = Path("data/output.txt")
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text("content")
content = p.read_text()
print(p.exists(), p.suffix, p.stem, p.name)
files = list(Path(".").glob("*.py"))
```

---

## 18. Collections Module

```python
from collections import defaultdict, Counter, deque, namedtuple

# defaultdict — no KeyError
word_groups = defaultdict(list)
for word in ["apple", "ant", "banana", "bear"]:
    word_groups[word[0]].append(word)

count_map = defaultdict(int)
for char in "abracadabra":
    count_map[char] += 1

# Counter
c = Counter("abracadabra")
print(c.most_common(3))     # [('a', 5), ('b', 2), ('r', 2)]
print(c["z"])               # 0 (no KeyError!)

c1 = Counter(a=3, b=2)
c2 = Counter(a=1, b=4)
print(c1 + c2)   # Counter({'b': 6, 'a': 4})
print(c1 - c2)   # Counter({'a': 2})

# deque — O(1) on both sides
dq = deque([1, 2, 3])
dq.append(4)        # right
dq.appendleft(0)    # left
dq.pop()
dq.popleft()
dq.rotate(1)

dq = deque(maxlen=3)    # fixed size, drops oldest
dq.extend([1,2,3,4])    # [2,3,4]

# namedtuple
Trade = namedtuple("Trade", ["symbol", "price", "volume"])
t = Trade("BTC", 50000.0, 100)
print(t.symbol, t.price)
print(t._asdict())
t2 = t._replace(price=51000.0)
```

---

## 19. functools Module

```python
from functools import lru_cache, partial, reduce, total_ordering

# lru_cache — memoization
@lru_cache(maxsize=128)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

print(fib(50))
print(fib.cache_info())
fib.cache_clear()

# partial — pre-fill arguments
def multiply(x, y):
    return x * y

double = partial(multiply, y=2)
print(double(5))  # 10

# reduce
product = reduce(lambda x, y: x * y, [1,2,3,4,5])  # 120

# total_ordering
@total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age
    # Now >, >=, <= automatically work!
```

---

## 20. itertools Module

```python
import itertools

# chain — combine iterables
combined = list(itertools.chain([1,2], [3,4], [5,6]))

# islice — slice any iterable (including generators)
gen = (x**2 for x in range(1000))
first_five = list(itertools.islice(gen, 5))  # [0,1,4,9,16]

# combinations & permutations
list(itertools.combinations([1,2,3], 2))
# [(1,2),(1,3),(2,3)]

list(itertools.permutations([1,2,3], 2))
# [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]

# product — cartesian product
list(itertools.product([0,1], repeat=3))   # binary 000-111

# groupby
data = [("a",1),("a",2),("b",3),("b",4)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))

# cycle
colors = itertools.cycle(["red", "green", "blue"])
for _ in range(6):
    print(next(colors))
```

---

## 21. Concurrency — Full

```python
# ===== THREADING =====
import threading

results = []
lock = threading.Lock()

def worker(n):
    with lock:
        results.append(n * 2)

threads = [threading.Thread(target=worker, args=(i,)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()

# Thread-safe queue
from queue import Queue
q = Queue()

def producer():
    for i in range(5):
        q.put(i)
    q.put(None)   # sentinel

def consumer():
    while True:
        item = q.get()
        if item is None: break
        print(f"Processing {item}")

# ===== MULTIPROCESSING =====
from multiprocessing import Pool

def cpu_task(n):
    return sum(i**2 for i in range(n))

with Pool(processes=4) as pool:
    results = pool.map(cpu_task, [10000, 20000, 30000])

# ===== ASYNCIO =====
import asyncio

async def fetch(url):
    await asyncio.sleep(0.5)   # simulate network call
    return f"data from {url}"

async def main():
    urls = ["url1", "url2", "url3"]
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)   # run concurrently
    return results

results = asyncio.run(main())

# Async generator
async def event_stream():
    for i in range(10):
        await asyncio.sleep(0.1)
        yield i

async def consume():
    async for event in event_stream():
        print(event)

# GIL Summary:
# - Only 1 thread runs Python bytecode at a time
# - GIL is RELEASED during I/O (file, network, sleep)
# - Threading  : good for I/O-bound
# - Multiprocess: good for CPU-bound (separate process = separate GIL)
# - asyncio    : best for high-concurrency I/O (single thread, cooperative)
```

---

## 22. Type Hints & Dataclasses

```python
from typing import List, Dict, Optional, Union, Any, Callable, TypeVar
from dataclasses import dataclass, field
import time

# Type hints in functions
def process(events: List[Dict[str, Any]]) -> Optional[Dict]:
    pass

def transform(data: Union[str, bytes]) -> str:
    pass

# Callable type hint
def apply(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)

# TypeVar — generic functions
T = TypeVar("T")
def first(items: List[T]) -> Optional[T]:
    return items[0] if items else None

# Dataclass
@dataclass
class TradeEvent:
    symbol: str
    price: float
    volume: int
    timestamp: float = field(default_factory=lambda: time.time())
    tags: List[str] = field(default_factory=list)
    metadata: Optional[Dict] = None

    def __post_init__(self):
        if self.price <= 0:
            raise ValueError(f"Price must be positive, got {self.price}")
        self.symbol = self.symbol.upper()

@dataclass(frozen=True)   # immutable, hashable
class Point:
    x: float
    y: float

@dataclass(order=True)    # auto-generates comparison methods
class Item:
    priority: int
    name: str
```

---

## 23. Memory Management & GIL

```python
import sys, gc

x = [1, 2, 3]
print(sys.getrefcount(x))    # reference count
print(sys.getsizeof([]))     # 56 bytes
print(sys.getsizeof("hello"))

# del removes reference
y = x
del x     # y still holds it, memory not freed yet

gc.collect()   # force garbage collection

# __slots__ — reduces memory in classes
class WithSlots:
    __slots__ = ["x", "y"]   # no __dict__, less memory
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

---

## 24. Common Interview Patterns

```python
# ===== Two Pointers =====
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# ===== Sliding Window =====
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# ===== HashMap O(1) lookup =====
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# ===== Stack — balanced brackets =====
def is_balanced(s):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0

# ===== BFS =====
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# ===== LRU Cache (manual — common interview question) =====
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# ===== Fibonacci — 4 ways =====
# Recursive (O(2^n)) — slow
def fib_recursive(n):
    if n < 2: return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# Memoized (O(n))
from functools import lru_cache
@lru_cache
def fib_memo(n):
    if n < 2: return n
    return fib_memo(n-1) + fib_memo(n-2)

# Optimized DP (O(n) time, O(1) space)
def fib_optimal(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

# Generator
def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
```

---

## 25. Classic Bug Traps

```python
# BUG 1: Mutable default argument
def add_item_wrong(item, lst=[]):    # WRONG — list shared across calls!
    lst.append(item)
    return lst

def add_item_correct(item, lst=None):  # CORRECT
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# BUG 2: Late binding in closures
funcs_wrong = [lambda: i for i in range(5)]
print([f() for f in funcs_wrong])   # [4,4,4,4,4] — all see last i!

funcs_correct = [lambda i=i: i for i in range(5)]
print([f() for f in funcs_correct]) # [0,1,2,3,4]

# BUG 3: Modifying list while iterating — WRONG
lst = [1, 2, 3, 4, 5]
for item in lst:
    if item % 2 == 0:
        lst.remove(item)   # skips items!

# CORRECT
lst = [item for item in lst if item % 2 != 0]

# BUG 4: is vs == for integers
a = 1000
b = 1000
print(a == b)   # True
print(a is b)   # False (large ints not cached)

x = 5
y = 5
print(x is y)   # True (small ints -5 to 256 are cached!)
```

---

## 26. Sorting Algorithms

```python
# Python built-in sort — Timsort, O(n log n)
lst = [3, 1, 4, 1, 5, 9]
lst.sort()                          # in-place
sorted_lst = sorted(lst)            # new list
sorted_lst = sorted(lst, reverse=True)
sorted_lst = sorted(lst, key=abs)   # custom key

# Sort list of dicts
people = [{"name": "Rao", "age": 25}, {"name": "Ram", "age": 22}]
people.sort(key=lambda x: x["age"])

# Sort by multiple keys
people.sort(key=lambda x: (x["age"], x["name"]))

# Bubble sort (manual)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

import bisect
bisect.bisect_left([1,2,3,5,6], 4)   # 3 (insertion point)
```

---

## 27. STAR Stories for Interview

### Story 1 — Deduplication System (Spizen)
> "At Spizen, I designed PyFlink streaming jobs with tumbling window aggregations to deduplicate high-velocity blockchain trade data across Kafka topics with fault-tolerant checkpointing. This achieved **95% deduplication accuracy** on 50K+ events per day."

**Python angle:** Used generators and streaming patterns to avoid loading all events in memory.

### Story 2 — Data Accuracy (Algonox)
> "At Algonox, I implemented multi-layered business rule validation in Python to clean and reconcile noisy unstructured document data. This boosted extraction accuracy by **40%**."

**Python angle:** Used OOP with abstract base classes for each validation rule, making it extensible.

### Story 3 — Automation (Algonox)
> "Built an automated email notification microservice in Flask and a KPI reporting module that reduced manual QA effort by **20%**."

**Python angle:** Used decorators for logging, context managers for DB connections, scheduled tasks.

---

## 28. Questions to Ask the Interviewer

1. "What does the Python/backend team work on specifically at Prowesssoft?"
2. "What does the integration stack look like — is it primarily MuleSoft or do you also use Kafka-based pipelines?"
3. "What does the onboarding look like for new engineers?"
4. "What's the biggest technical challenge the team is solving right now?"

---

*Prepared: 2026-05-01 | Interview: Prowesssoft (Prowess Software Services)*
