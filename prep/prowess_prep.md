# Prowesssoft Interview Prep — Narasimharao Bhavirisetty

---

## PART 1: About Prowesssoft

### Company at a Glance

| Detail | Info |
|---|---|
| Founded | 2016 (Bootstrapped, profitable) |
| HQ | Hyderabad, India (Kukatpally) |
| Offices | Hyderabad, Bengaluru, Atlanta (USA), Singapore |
| Employees | ~350–400 |
| Revenue | ~₹106 Crore (~$13M USD) as of 2025 |
| Glassdoor Rating | 3.9 / 5 |

**What they do:** Enterprise IT integration — connecting company systems using MuleSoft, Kafka, APIs. They are a **MuleSoft Premier Partner** (top tier, won Partner of the Year 2024 & 2025 in Americas). They serve Finance, Healthcare, Retail, and Logistics clients worldwide (Fortune 500 companies).

### Technologies They Use

| Category | Technologies |
|---|---|
| Primary Platform | MuleSoft Anypoint Platform |
| iPaaS & Integration | Boomi, TIBCO, WSO2, IBM IIB, WebMethods, BizTalk |
| API Gateways | Kong, AWS API Gateway, Azure Logic Apps, Apigee |
| Messaging/Streaming | Apache Kafka |
| CRM | Salesforce (Summit Partner) |
| AI | Salesforce Agentforce, CurieTech AI, Parabola9 |
| Cloud | AWS, Azure |

### Your Fit vs Their Stack

| Your Skills | Their Stack | Match? |
|---|---|---|
| Kafka | Kafka (Enterprise Event Streaming) | Strong match |
| REST APIs / Flask | API Integration & Management | Good match |
| Python | Java is primary, Python secondary | Partial |
| PyFlink / Stream Processing | Kafka-based event-driven arch | Relevant |
| ClickHouse / Redis | Not their core, but data layer | Partial |
| MuleSoft | Not on your resume | Gap |

### Culture (Glassdoor)
- Pros: Good learning environment, senior engineers accessible, certified "Great Place to Work"
- Cons: Fast-paced, employees handle many responsibilities
- 67% rate interviews as positive

### What to Expect in the Interview
1. **Kafka deep-dive** — consumer groups, offsets, deduplication, fault tolerance, checkpointing
2. **Python OOP & backend** — standard Python, REST API design with Flask
3. **System Design** — "Design a real-time data pipeline" — you've built this, talk through Solana/Kafka/ClickHouse
4. **Why Prowesssoft?** — "I've been working with event-driven architectures and Kafka — integration is the next natural step."

### Quick Prep Checklist
- [ ] Explain your Kafka pipeline end-to-end (50K events/day, dedup, scoring)
- [ ] Revisit Python decorators, OOP, generators
- [ ] Prepare 2–3 STAR stories from Spizen & Algonox
- [ ] Know what MuleSoft is (enterprise integration platform by Salesforce)
- [ ] Ask them: "What does the Python/backend team work on specifically?"

---

## PART 2: Complete Python Brush-Up

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
s2 = 'world'
s3 = """multi
line"""

# Boolean
t = True
f = False
print(int(True))   # 1
print(int(False))  # 0

# None
x = None
print(x is None)   # True  ← always use 'is' for None

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
print(s.strip())          # remove whitespace both ends
print(s.lstrip())         # left only
print(s.rstrip())         # right only
print(s.replace("Rao", "Kumar"))
print(s.split(","))       # returns list
print(",".join(["a","b","c"]))   # 'a,b,c'
print(s.startswith("Nara"))      # True
print(s.endswith("rao"))         # True
print(s.find("sim"))      # index of first match, -1 if not found
print(s.count("a"))       # count occurrences
print(s.isdigit())        # False
print("123".isdigit())    # True
print(s.isalpha())        # True

# Formatting
name = "Rao"
age = 25

# f-string (preferred, Python 3.6+)
print(f"Name: {name}, Age: {age}")
print(f"Price: {3.14159:.2f}")    # 2 decimal places
print(f"{'left':<10}|")           # left-align in width 10
print(f"{'right':>10}|")          # right-align

# .format()
print("Name: {}, Age: {}".format(name, age))

# % formatting (old style)
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
lst.sort()             # in-place
lst.sort(reverse=True)
new = sorted(lst)      # returns new list, original unchanged
lst.reverse()          # in-place reverse

# Copy (important interview topic!)
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
t = (1, 2, 3)
t2 = 1, 2, 3      # parentheses optional
single = (1,)     # MUST have trailing comma for single element
empty = ()

# Can be used as dict keys (because hashable)
d = {(1, 2): "point"}

# Unpacking
x, y, z = t

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
print(d["name"])             # KeyError if missing
print(d.get("name"))         # None if missing
print(d.get("city", "N/A")) # default if missing

# Modification
d["city"] = "Bangalore"
d.update({"age": 26, "role": "Engineer"})
del d["city"]
removed = d.pop("age")
d.setdefault("score", 0)    # sets only if key doesn't exist

# Iteration
for key in d: print(key)
for key, value in d.items(): print(key, value)
for key in d.keys(): pass
for val in d.values(): pass

# Checking
print("name" in d)          # True

# Merging (Python 3.9+)
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2            # {"a":1, "b":2}

# Dict comprehension
squares = {x: x**2 for x in range(5)}

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
empty_set = set()   # NOT {} — that creates empty dict!

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

# frozenset — immutable, usable as dict key
fs = frozenset([1, 2, 3])
```

---

## 7. Control Flow

```python
# if / elif / else
x = 10
if x > 10:
    print("big")
elif x == 10:
    print("ten")
else:
    print("small")

# Ternary
result = "even" if x % 2 == 0 else "odd"

# for loop
for i in range(5): print(i)         # 0 1 2 3 4
for i in range(2, 10, 2): print(i)  # 2 4 6 8

# enumerate
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

# zip
names = ["Rao", "Ram", "Raj"]
ages = [25, 30, 22]
for name, age in zip(names, ages):
    print(name, age)

# while
n = 5
while n > 0:
    print(n)
    n -= 1

# break, continue, else
for i in range(10):
    if i == 3: continue
    if i == 7: break
    print(i)
else:
    print("done")  # only if loop completed without break
```

---

## 8. Functions

```python
# Default arguments
def power(base, exp=2):
    return base ** exp

# *args — variable positional (tuple)
def total(*args):
    return sum(args)

# **kwargs — variable keyword (dict)
def display(**kwargs):
    for key, val in kwargs.items():
        print(f"{key}: {val}")

# Combining all
def func(a, b, *args, keyword_only, **kwargs):
    pass

# Unpacking when calling
nums = [1, 2, 3]
print(total(*nums))

config = {"name": "Rao", "age": 25}
display(**config)

# Lambda
square = lambda x: x ** 2
add = lambda x, y: x + y

# map, filter, sorted with lambda
data = [{"name": "Rao", "age": 25}, {"name": "Ram", "age": 30}]
data.sort(key=lambda x: x["age"])

nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
doubled = list(map(lambda x: x * 2, nums))

from functools import reduce
product = reduce(lambda x, y: x * y, nums)  # 120
```

---

## 9. Scope & Closures

```python
# LEGB Rule: Local → Enclosing → Global → Built-in

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
print(c())  # 2
print(c())  # 3  ← closure remembers 'n'

# Closures
def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = multiplier(2)
triple = multiplier(3)
print(double(5))   # 10
print(triple(5))   # 15
```

---

## 10. Comprehensions

```python
# List
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
flat = [x for row in [[1,2],[3,4]] for x in row]  # flatten

# Dict
d = {k: v for k, v in zip("abcde", range(5))}
inverted = {v: k for k, v in d.items()}

# Set
unique_squares = {x**2 for x in [-2, -1, 0, 1, 2]}  # {0, 1, 4}

# Generator expression (lazy — no memory used until iterated)
gen = (x**2 for x in range(1_000_000))
print(next(gen))  # 0

# Nested
matrix = [[1,2,3],[4,5,6],[7,8,9]]
transposed = [[row[i] for row in matrix] for i in range(3)]
```

---

## 11. Iterators & Generators

```python
# Iterator protocol: __iter__ and __next__
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
        yield n
        n -= 1

for i in countdown(5):
    print(i)

# Generator with send()
def accumulator():
    total = 0
    while True:
        value = yield total
        total += value

gen = accumulator()
next(gen)            # prime the generator
print(gen.send(10))  # 10
print(gen.send(20))  # 30
print(gen.send(5))   # 35

# yield from
def chain(*iterables):
    for it in iterables:
        yield from it

print(list(chain([1,2], [3,4], [5,6])))  # [1,2,3,4,5,6]

# Practical: reading large files line by line
def read_large_file(filepath):
    with open(filepath) as f:
        for line in f:
            yield line.strip()
```

---

## 12. Decorators

```python
import functools

# Basic decorator
def my_decorator(func):
    @functools.wraps(func)
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

# Class-based decorator
class Cache:
    def __init__(self, func):
        self.func = func
        self.cache = {}
        functools.update_wrapper(self, func)

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

@Cache
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)

# Stacking decorators (applied bottom-up)
@timer
@retry(times=3)
def my_func():
    pass
```

---

## 13. Context Managers

```python
# Class-based
class DatabaseConnection:
    def __init__(self, url):
        self.url = url

    def __enter__(self):
        self.conn = connect(self.url)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        return False   # False = don't suppress exceptions

with DatabaseConnection("localhost") as conn:
    conn.execute("SELECT 1")

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
    time.sleep(1)

# Multiple context managers
with open("in.txt") as fin, open("out.txt", "w") as fout:
    fout.write(fin.read())

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
    species_count = 0   # class variable (shared across ALL instances)

    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age
        Animal.species_count += 1

    def speak(self):
        raise NotImplementedError("Subclass must implement")

    @classmethod
    def get_count(cls):       # receives class, not instance
        return cls.species_count

    @staticmethod
    def is_valid_age(age):    # no access to class or instance
        return 0 <= age <= 150

    @property
    def info(self):
        return f"{self.name} ({self.age})"

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

    def __contains__(self, item):
        return item in self.name


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
print(type(dog) == Animal)      # False (exact type)

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

D().method()       # D → B → C → A
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

# Pipeline()       # TypeError: Can't instantiate abstract class
TradePipeline()    # Works
```

---

## 16. Exception Handling

```python
# Exception hierarchy
# BaseException
#   ├── SystemExit
#   ├── KeyboardInterrupt
#   └── Exception
#       ├── ValueError
#       ├── TypeError
#       ├── KeyError
#       ├── IndexError
#       ├── AttributeError
#       ├── NameError
#       ├── RuntimeError
#       ├── IOError / OSError
#       └── StopIteration

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Math error: {e}")
except (ValueError, TypeError) as e:
    print(f"Value/Type error: {e}")
except Exception as e:
    print(f"Unexpected: {e}")
    raise                      # re-raise same exception
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

class ProcessingError(PipelineError):
    pass

# Exception chaining
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("Failed to parse config") from e

# Suppress original
try:
    int("abc")
except ValueError:
    raise RuntimeError("Config error") from None
```

---

## 17. File I/O

```python
# Writing
with open("data.txt", "w") as f:
    f.write("Hello\n")
    f.writelines(["line1\n", "line2\n"])

with open("data.txt", "a") as f:   # append
    f.write("New line\n")

# Reading
with open("data.txt") as f:
    content = f.read()          # entire file as string

with open("data.txt") as f:
    lines = f.readlines()       # list of lines

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

json_str = json.dumps(data)     # dict → string
parsed = json.loads(json_str)   # string → dict

# CSV
import csv
with open("data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "Rao", "age": 25})

with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# pathlib
from pathlib import Path
p = Path("data/files/output.txt")
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text("content")
content = p.read_text()
print(p.exists(), p.suffix, p.stem, p.name)
files = list(Path(".").glob("*.py"))
```

---

## 18. Modules & Packages

```python
import os
from os import path, getcwd
from os.path import join, exists
import numpy as np

# __name__ guard
if __name__ == "__main__":
    # Only runs when executed directly, not when imported
    main()

# Relative imports (inside packages)
from . import utils           # same package
from ..models import Trade    # parent package

# Dynamic imports
import importlib
module = importlib.import_module("mypackage.utils")
```

---

## 19. Collections Module

```python
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple

# defaultdict — no KeyError
word_groups = defaultdict(list)
for word in ["apple", "ant", "banana", "bear", "cat"]:
    word_groups[word[0]].append(word)

count_map = defaultdict(int)
for char in "abracadabra":
    count_map[char] += 1

# Counter
c = Counter("abracadabra")
print(c)                    # Counter({'a': 5, 'b': 2, ...})
print(c.most_common(3))     # [('a', 5), ('b', 2), ('r', 2)]
print(c["z"])               # 0 — no KeyError!

c1 = Counter(a=3, b=2)
c2 = Counter(a=1, b=4)
print(c1 + c2)   # Counter({'b': 6, 'a': 4})
print(c1 - c2)   # Counter({'a': 2})

# deque — O(1) append/pop from both ends
dq = deque([1, 2, 3])
dq.append(4)           # right
dq.appendleft(0)       # left
dq.pop()               # remove right
dq.popleft()           # remove left
dq.rotate(1)           # rotate right

dq = deque(maxlen=3)   # fixed size, auto-drops oldest
dq.extend([1,2,3,4])   # [2,3,4]

# namedtuple
Trade = namedtuple("Trade", ["symbol", "price", "volume"])
t = Trade("BTC", 50000.0, 100)
print(t.symbol, t.price)
print(t._asdict())
t2 = t._replace(price=51000.0)
```

---

## 20. functools Module

```python
from functools import lru_cache, cache, partial, reduce, wraps, total_ordering

# lru_cache — memoization
@lru_cache(maxsize=128)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

print(fib(50))
print(fib.cache_info())
fib.cache_clear()

# cache (Python 3.9+) — unlimited lru_cache
@cache
def expensive(n):
    return n ** 2

# partial — fix some arguments
def multiply(x, y):
    return x * y

double = partial(multiply, y=2)
triple = partial(multiply, y=3)
print(double(5))   # 10

# reduce
nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)   # 120
total = reduce(lambda x, y: x + y, nums, 0)  # 15

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
    # >, >=, <= automatically work now!
```

---

## 21. Itertools Module

```python
import itertools

# count — infinite counter
for i in itertools.count(10, 2):
    if i > 20: break

# cycle — infinite cycle
colors = itertools.cycle(["red", "green", "blue"])
for _ in range(6):
    print(next(colors))

# chain
combined = list(itertools.chain([1,2], [3,4], [5,6]))

# islice — slice any iterable
gen = (x**2 for x in range(1000))
first_five = list(itertools.islice(gen, 5))   # [0,1,4,9,16]

# combinations & permutations
print(list(itertools.combinations([1,2,3], 2)))
# [(1,2),(1,3),(2,3)]

print(list(itertools.permutations([1,2,3], 2)))
# [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]

# product — cartesian product
print(list(itertools.product([0,1], repeat=3)))   # binary 000-111

# groupby
data = [("a",1),("a",2),("b",3),("b",4),("a",5)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))
```

---

## 22. Concurrency — Full

```python
# ===== THREADING =====
import threading

def worker(n, results, lock):
    import time
    time.sleep(0.1)
    with lock:
        results.append(n * 2)

results = []
lock = threading.Lock()
threads = [threading.Thread(target=worker, args=(i, results, lock)) for i in range(5)]
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

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start(); t2.start()
t1.join(); t2.join()

# ===== MULTIPROCESSING =====
from multiprocessing import Pool

def cpu_task(n):
    return sum(i**2 for i in range(n))

with Pool(processes=4) as pool:
    results = pool.map(cpu_task, [10000, 20000, 30000, 40000])

# ===== ASYNCIO =====
import asyncio

async def fetch(url):
    await asyncio.sleep(0.5)   # simulate I/O
    return f"data from {url}"

async def main():
    urls = ["url1", "url2", "url3"]
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)   # run concurrently
    return results

results = asyncio.run(main())

# Async context manager
class AsyncDBConn:
    async def __aenter__(self):
        self.conn = await connect_async()
        return self.conn

    async def __aexit__(self, *args):
        await self.conn.close()

# Async generator
async def event_stream():
    for i in range(10):
        await asyncio.sleep(0.1)
        yield i

async def consume():
    async for event in event_stream():
        print(event)

# asyncio.wait vs gather
async def main():
    tasks = [asyncio.create_task(fetch(url)) for url in ["url1","url2"]]

    # gather — simple, one failure = all fail (by default)
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # wait — more control
    done, pending = await asyncio.wait(tasks, timeout=5.0)
```

### GIL — Global Interpreter Lock

```
- Only 1 thread executes Python bytecode at a time
- GIL is RELEASED during I/O operations (network, file, sleep)
- GIL is NOT released during pure Python computation

Decision table:
┌─────────────────┬──────────────────────────┐
│ Task type       │ Best tool                │
├─────────────────┼──────────────────────────┤
│ I/O-bound       │ asyncio or threading     │
│ CPU-bound       │ multiprocessing          │
│ High-concurrency│ asyncio                  │
│ Kafka consumers │ asyncio or threading     │
└─────────────────┴──────────────────────────┘
```

---

## 23. Type Hints & Dataclasses

```python
from typing import List, Dict, Tuple, Set, Optional, Union, Any, Callable, TypeVar
from dataclasses import dataclass, field
import time

# Type hints
def process(events: List[Dict[str, Any]]) -> Optional[Dict]:
    pass

def transform(data: Union[str, bytes]) -> str:
    pass

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

## 24. Memory Management

```python
import sys

x = [1, 2, 3]
print(sys.getrefcount(x))       # reference count

print(sys.getsizeof([]))         # 56 bytes
print(sys.getsizeof([1,2,3]))    # 88 bytes

import gc
gc.collect()   # force garbage collection

# __slots__ — reduces memory in classes with many instances
class WithSlots:
    __slots__ = ["x", "y"]    # no __dict__, saves memory
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

---

## 25. Common Interview Patterns

```python
# PATTERN 1: Two Pointers
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# PATTERN 2: Sliding Window
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# PATTERN 3: HashMap for O(1) lookup
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# PATTERN 4: Stack for balanced brackets
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

# PATTERN 5: BFS
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

# PATTERN 6: LRU Cache (manual)
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

# PATTERN 7: Fibonacci — 4 ways
# 1. Recursive (slow, O(2^n))
def fib_recursive(n):
    if n < 2: return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# 2. Memoized
from functools import lru_cache
@lru_cache
def fib_memo(n):
    if n < 2: return n
    return fib_memo(n-1) + fib_memo(n-2)

# 3. DP iterative
def fib_dp(n):
    dp = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 4. Optimized O(1) space
def fib_optimal(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a
```

---

## 26. Classic Bug — Mutable Default Argument

```python
# WRONG
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))   # [1]
print(add_item(2))   # [1, 2]  ← BUG! same list reused!
print(add_item(3))   # [1, 2, 3]

# CORRECT
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

---

## 27. Quick Reference — Most-Asked Interview Answers

| Question | Answer |
|---|---|
| `list` vs `tuple` | List: mutable, unhashable. Tuple: immutable, hashable (usable as dict key) |
| `==` vs `is` | `==` value equality, `is` identity (same object in memory) |
| `deepcopy` vs `copy` | `copy`: new object, nested refs shared. `deepcopy`: fully independent clone |
| What is GIL? | Mutex allowing only 1 thread to run Python bytecode at a time. Released during I/O. |
| `@classmethod` vs `@staticmethod` | classmethod gets `cls`, staticmethod gets neither. classmethod used for alternate constructors. |
| What is a generator? | Function using `yield`. Lazy — produces values one at a time without storing all in memory. |
| What is a closure? | Inner function that remembers variables from enclosing scope after outer function returns. |
| `__str__` vs `__repr__` | `__str__`: user-friendly (for print). `__repr__`: developer string (for debugging). |
| How does `dict` work? | Hash table. Average O(1) get/set. Keys must be hashable. |
| `*args` vs `**kwargs` | `*args`: positional → tuple. `**kwargs`: keyword → dict. |
| `map` vs list comprehension | Both equivalent. List comprehension is more Pythonic. |
| MRO | C3 linearization. `Dog.__mro__` shows order Python looks up methods. |
| `__new__` vs `__init__` | `__new__` creates the instance. `__init__` initializes it. |
| `None` check | Always `if x is None`, never `if x == None` |
| Mutable default arg | `def f(lst=[])` — all calls share same list. Use `def f(lst=None): lst = lst or []` |

---

## 28. Leverage Your Real Experience

When answering, connect to your actual work:

- **Generators** → "In my PyFlink pipeline, I used generators to process 50K trade events daily without loading all into memory at once."
- **defaultdict** → "I used defaultdict when grouping trade events by token symbol across Kafka topics."
- **Retry decorator** → "I implemented a retry decorator for Kafka consumer failures with exponential backoff."
- **Context managers** → "I used context managers to handle ClickHouse and Redis connections cleanly in the pipeline."
- **asyncio** → "My streaming jobs used async patterns to handle high-concurrency event consumption from multiple Kafka topics."
- **OOP / Abstract classes** → "I designed the pipeline as an abstract base class so each stream processing job inherits process() and validate() and is interchangeable."

---

*Good luck tomorrow, Narasimharao! Lead with Kafka and stream processing — that's your strongest card.*
