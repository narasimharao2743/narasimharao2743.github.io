# Python + AI/ML Interview Preparation Guide
**Target:** Prowesssoft (API Integration, Kafka, Cloud) + General Python roles  
**Profile:** 1.5 years exp — Kafka, PyFlink, ClickHouse, Redis, Protobuf, Flask  
**Goal:** Brush up Python basics → advanced + AI/ML fundamentals

---

## STUDY PLAN (4 Weeks)

| Week | Focus |
|------|-------|
| Week 1 | Python Basics + OOP |
| Week 2 | Intermediate Python + APIs |
| Week 3 | Advanced Python + Concurrency |
| Week 4 | AI/ML Basics + Mock Interview |

---

# PART 1: PYTHON

---

## WEEK 1 — BASICS + OOP

### 1.1 Data Types

```python
# Primitive types
x = 10          # int
y = 3.14        # float
name = "Nara"   # str
flag = True     # bool
nothing = None  # NoneType

# Type casting
int("42")       # 42
float("3.14")   # 3.14
str(100)        # "100"
bool(0)         # False — 0, "", [], {}, None are all falsy
```

**Key interview points:**
- `is` checks identity (same memory), `==` checks value
- Strings are immutable — every operation creates a new string
- `None` is a singleton — always compare with `is None`, not `== None`

---

### 1.2 Strings

```python
s = "  Hello World  "

s.strip()           # "Hello World"
s.lower()           # "  hello world  "
s.upper()           # "  HELLO WORLD  "
s.replace("o", "0") # "  Hell0 W0rld  "
s.split(" ")        # ['', '', 'Hello', 'World', '', '']
s.startswith("  H") # True
s.find("World")     # 8
",".join(["a","b"]) # "a,b"

# f-strings (Python 3.6+)
name = "Nara"
age = 25
f"Name: {name}, Age: {age}"  # "Name: Nara, Age: 25"
f"{3.14159:.2f}"              # "3.14"
```

---

### 1.3 Collections

```python
# LIST — ordered, mutable, allows duplicates
fruits = ["apple", "banana", "apple"]
fruits.append("mango")
fruits.remove("apple")   # removes first occurrence
fruits.pop()             # removes last
fruits[0]                # indexing
fruits[-1]               # last element
fruits[1:3]              # slicing
fruits.sort()
fruits.reverse()
len(fruits)

# TUPLE — ordered, immutable
point = (10, 20)
x, y = point             # unpacking

# SET — unordered, no duplicates
s = {1, 2, 3, 2}         # {1, 2, 3}
s.add(4)
s.discard(1)
s1 | s2                  # union
s1 & s2                  # intersection
s1 - s2                  # difference

# DICT — key-value pairs
person = {"name": "Nara", "age": 25}
person["name"]            # "Nara"
person.get("city", "N/A") # safe get with default
person["city"] = "Hyd"    # add/update
del person["age"]
person.keys()
person.values()
person.items()            # [(key, val), ...]

# Comprehensions
squares = [x**2 for x in range(10)]
even_sq = [x**2 for x in range(10) if x % 2 == 0]
sq_dict = {x: x**2 for x in range(5)}
sq_set  = {x**2 for x in range(5)}
```

**When to use what:**
| Structure | Use when |
|-----------|----------|
| List | ordered collection, duplicates needed |
| Tuple | fixed data, dict keys, unpacking |
| Set | uniqueness, membership test O(1) |
| Dict | key-value lookup O(1) |

---

### 1.4 Functions

```python
# Basic
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

greet("Nara")             # "Hello, Nara"
greet("Nara", "Hi")       # "Hi, Nara"

# *args — variable positional arguments (tuple)
def add(*args):
    return sum(args)
add(1, 2, 3)              # 6

# **kwargs — variable keyword arguments (dict)
def info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")
info(name="Nara", age=25)

# Lambda — anonymous one-liner function
square = lambda x: x**2
square(5)                 # 25

# Used with map/filter/sorted
nums = [3, 1, 4, 1, 5]
list(map(lambda x: x*2, nums))       # [6,2,8,2,10]
list(filter(lambda x: x>2, nums))    # [3,4,5]
sorted(nums, key=lambda x: -x)       # [5,4,3,1,1]
```

---

### 1.5 OOP (Most Important for Interviews)

```python
class Animal:
    species = "Animal"          # class variable (shared)

    def __init__(self, name, age):
        self.name = name        # instance variable
        self.age = age

    def speak(self):
        return f"{self.name} makes a sound"

    def __str__(self):
        return f"Animal({self.name}, {self.age})"

    def __repr__(self):
        return f"Animal(name={self.name!r}, age={self.age!r})"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    @classmethod
    def create(cls, name):      # works on class, not instance
        return cls(name, 0)

    @staticmethod
    def is_valid_age(age):      # no access to class or instance
        return age >= 0


class Dog(Animal):              # Inheritance
    def __init__(self, name, age, breed):
        super().__init__(name, age)   # call parent __init__
        self.breed = breed

    def speak(self):            # Overriding (polymorphism)
        return f"{self.name} barks"


# Usage
d = Dog("Rex", 3, "Labrador")
print(d.speak())               # "Rex barks"
print(isinstance(d, Animal))   # True
print(isinstance(d, Dog))      # True
```

**4 Pillars of OOP:**
| Pillar | Meaning | Example |
|--------|---------|---------|
| Encapsulation | Hide internal state | `_private`, `__name` mangling |
| Inheritance | Reuse parent class | `class Dog(Animal)` |
| Polymorphism | Same method, different behavior | `speak()` override |
| Abstraction | Hide complexity, show interface | Abstract base classes |

```python
# Abstraction with ABC
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r ** 2
```

---

### 1.6 Error Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError) as e:
    print(f"Type/Value error: {e}")
else:
    print("No error occurred")    # runs only if no exception
finally:
    print("Always runs")          # cleanup goes here

# Custom exception
class InsufficientFundsError(Exception):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(f"Insufficient funds: need {amount} more")

raise InsufficientFundsError(500)
```

---

## WEEK 2 — INTERMEDIATE + APIs

### 2.1 Decorators

```python
import functools

# Basic decorator
def my_decorator(func):
    @functools.wraps(func)          # preserves func name/docs
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()
# Before
# Hello
# After

# Decorator with arguments
def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hi():
    print("Hi")

hi()  # prints Hi 3 times

# Practical: timing decorator
import time
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time()-start:.4f}s")
        return result
    return wrapper
```

---

### 2.2 Generators & Iterators

```python
# Iterator protocol
class CountUp:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current

for n in CountUp(3):
    print(n)   # 1 2 3

# Generator — cleaner way using yield
def count_up(limit):
    for i in range(1, limit+1):
        yield i

gen = count_up(3)
next(gen)   # 1
next(gen)   # 2
next(gen)   # 3

# Generator expression (lazy, memory efficient)
squares = (x**2 for x in range(1000000))  # doesn't compute all at once
next(squares)   # 0

# Real use case: reading large files
def read_large_file(path):
    with open(path) as f:
        for line in f:
            yield line.strip()
```

**Generator vs List:**
- List: all values in memory at once
- Generator: one value at a time — use for large data

---

### 2.3 Context Managers

```python
# Using with statement
with open("file.txt", "w") as f:
    f.write("hello")
# file auto-closed here even if exception occurs

# Creating custom context manager
class DBConnection:
    def __enter__(self):
        print("Opening connection")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection")
        return False  # don't suppress exceptions

with DBConnection() as db:
    print("Using db")

# Using contextlib
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield
    print(f"Elapsed: {time.time()-start:.4f}s")

with timer():
    sum(range(1000000))
```

---

### 2.4 Collections Module

```python
from collections import defaultdict, Counter, deque, namedtuple, OrderedDict

# defaultdict — no KeyError on missing keys
dd = defaultdict(list)
dd["a"].append(1)   # works without initializing

dd = defaultdict(int)
for c in "hello":
    dd[c] += 1      # word frequency

# Counter — count occurrences
c = Counter("banana")         # Counter({'a':3,'n':2,'b':1})
c.most_common(2)              # [('a',3), ('n',2)]
c1 + c2                       # add counters

# deque — fast append/pop from both ends
dq = deque([1,2,3])
dq.appendleft(0)              # O(1) — list insert(0) is O(n)
dq.popleft()                  # O(1)
dq.rotate(1)                  # rotate right

# namedtuple — tuple with named fields
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
p.x    # 10
p[0]   # 10 — still indexable
```

---

### 2.5 REST APIs with Flask (Relevant for Prowesssoft)

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory store
users = {}

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(list(users.values()))

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "Not found"}), 404
    return jsonify(user)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "name required"}), 400
    uid = len(users) + 1
    users[uid] = {"id": uid, "name": data["name"]}
    return jsonify(users[uid]), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "Not found"}), 404
    data = request.get_json()
    user.update(data)
    return jsonify(user)

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "Not found"}), 404
    del users[user_id]
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
```

**HTTP Status Codes to know:**
| Code | Meaning |
|------|---------|
| 200 | OK |
| 201 | Created |
| 204 | No Content (delete success) |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

---

### 2.6 File Handling + JSON

```python
import json

# Write JSON
data = {"name": "Nara", "skills": ["Python", "Kafka"]}
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read JSON
with open("data.json") as f:
    loaded = json.load(f)

# String <-> JSON
json_str = json.dumps(data)         # dict to string
parsed = json.loads(json_str)       # string to dict

# CSV
import csv
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Nara", 25])

with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)  # {'name': 'Nara', 'age': '25'}
```

---

## WEEK 3 — ADVANCED PYTHON

### 3.1 Concurrency

```python
# Threading — good for I/O bound (API calls, file read/write)
import threading

def fetch_data(url):
    print(f"Fetching {url}")

threads = []
for url in ["url1", "url2", "url3"]:
    t = threading.Thread(target=fetch_data, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Multiprocessing — good for CPU bound (data processing, calculations)
from multiprocessing import Pool

def process(n):
    return n ** 2

with Pool(4) as p:
    results = p.map(process, range(10))

# asyncio — best for many concurrent I/O operations
import asyncio

async def fetch(url):
    await asyncio.sleep(1)  # simulate async I/O
    return f"Data from {url}"

async def main():
    tasks = [fetch(f"url{i}") for i in range(3)]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
```

**GIL (Global Interpreter Lock):**
- Python's GIL allows only ONE thread to execute Python bytecode at a time
- Threading still helps for I/O (GIL released during I/O waits)
- For CPU parallelism → use `multiprocessing` (separate processes, no GIL)

---

### 3.2 Shallow vs Deep Copy

```python
import copy

original = [[1, 2], [3, 4]]

# Assignment — same object
ref = original
ref[0].append(99)
print(original)     # [[1, 2, 99], [3, 4]] — original changed!

# Shallow copy — new outer, shared inner
shallow = copy.copy(original)
shallow[0].append(99)
print(original)     # [[1, 2, 99], [3, 4]] — inner still shared!

# Deep copy — completely independent
deep = copy.deepcopy(original)
deep[0].append(99)
print(original)     # [[1, 2], [3, 4]] — original safe
```

---

### 3.3 Closures

```python
def make_multiplier(n):
    def multiply(x):
        return x * n      # n is "closed over" from outer scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
double(5)   # 10
triple(5)   # 15

# nonlocal
def counter():
    count = 0
    def increment():
        nonlocal count    # access outer variable
        count += 1
        return count
    return increment

c = counter()
c()  # 1
c()  # 2
```

---

### 3.4 Type Hints

```python
from typing import List, Dict, Optional, Union, Tuple, Any, Callable

def greet(name: str) -> str:
    return f"Hello {name}"

def process(items: List[int]) -> Dict[str, int]:
    return {"sum": sum(items), "count": len(items)}

def find_user(uid: int) -> Optional[str]:  # returns str or None
    return None

def parse(value: Union[int, str]) -> str:  # int OR str
    return str(value)

# Python 3.10+ shorthand
def newer(value: int | str) -> str:
    return str(value)
```

---

### 3.5 Dataclasses

```python
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    age: int
    skills: list = field(default_factory=list)  # mutable default

    def is_senior(self) -> bool:
        return self.age > 30

u = User("Nara", 25)
u.skills.append("Python")
print(u)  # User(name='Nara', age=25, skills=['Python'])

@dataclass(frozen=True)   # immutable like tuple
class Point:
    x: float
    y: float
```

---

### 3.6 Regex

```python
import re

text = "My email is nara@gmail.com and phone is +91 9876543210"

# Search (find first match)
match = re.search(r'\w+@\w+\.\w+', text)
if match:
    print(match.group())   # nara@gmail.com

# Find all
emails = re.findall(r'\w+@\w+\.\w+', text)

# Substitute
clean = re.sub(r'\d+', 'X', text)   # replace numbers with X

# Common patterns
r'\d'      # digit
r'\w'      # word char (letter/digit/_)
r'\s'      # whitespace
r'.'       # any char except newline
r'^'       # start of string
r'$'       # end of string
r'+'       # 1 or more
r'*'       # 0 or more
r'?'       # 0 or 1
r'{3}'     # exactly 3
r'[a-z]'  # char range
```

---

### 3.7 Sorting & Algorithms Basics

```python
# Sorting
nums = [3, 1, 4, 1, 5, 9]
sorted(nums)                         # new sorted list
nums.sort()                          # in-place
sorted(nums, reverse=True)
sorted(words, key=len)               # sort by length
sorted(people, key=lambda p: p.age)  # sort by attribute

# Common interview problems
# 1. Find duplicates
from collections import Counter
def find_duplicates(lst):
    return [k for k, v in Counter(lst).items() if v > 1]

# 2. Flatten nested list
def flatten(lst):
    return [x for sub in lst for x in sub]

# 3. Reverse string
"hello"[::-1]   # "olleh"

# 4. Palindrome check
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# 5. Two sum
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i
```

---

# PART 2: AI / ML BASICS

---

## WEEK 4 — AI/ML FUNDAMENTALS

### 4.1 What is Machine Learning?

**Types of ML:**
| Type | Description | Example |
|------|-------------|---------|
| Supervised | Labeled data, learn input→output | Spam detection, price prediction |
| Unsupervised | No labels, find patterns | Customer clustering, anomaly detection |
| Reinforcement | Agent learns by reward/punishment | Game AI, robotics |

**ML Workflow:**
```
Data Collection → Data Cleaning → EDA → Feature Engineering
→ Model Selection → Training → Evaluation → Deployment
```

---

### 4.2 Key Algorithms

#### Linear Regression
- Predicts continuous values (price, temperature)
- Finds best-fit line: `y = mx + b`
- Loss: Mean Squared Error (MSE)

```python
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1],[2],[3],[4],[5]])
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(X, y)
model.predict([[6]])   # [12]
print(model.coef_)     # slope
print(model.intercept_) # intercept
```

#### Logistic Regression
- Predicts binary class (yes/no, spam/not spam)
- Output is probability 0-1 using sigmoid function
- Threshold at 0.5 → class 0 or 1

#### Decision Tree
- Tree of if/else decisions on features
- Easy to interpret
- Prone to overfitting

#### Random Forest
- Many decision trees + majority voting
- Reduces overfitting
- More accurate than single tree

#### K-Nearest Neighbors (KNN)
- Classify based on K closest data points
- No training, slow at prediction
- Sensitive to scale → always normalize

#### Support Vector Machine (SVM)
- Finds hyperplane that maximally separates classes
- Works well for high-dimensional data
- Kernel trick for non-linear data

---

### 4.3 Data Preprocessing

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder, MinMaxScaler

df = pd.read_csv("data.csv")

# 1. Explore
df.shape           # (rows, cols)
df.info()          # dtypes, nulls
df.describe()      # stats
df.isnull().sum()  # count nulls per column

# 2. Handle missing values
df["age"].fillna(df["age"].mean(), inplace=True)    # fill with mean
df.dropna(inplace=True)                              # drop rows with null

# 3. Encode categorical → numerical
le = LabelEncoder()
df["gender"] = le.fit_transform(df["gender"])       # Male→1, Female→0

# Or one-hot encoding
df = pd.get_dummies(df, columns=["city"])

# 4. Feature scaling
scaler = StandardScaler()
df[["age","salary"]] = scaler.fit_transform(df[["age","salary"]])
# StandardScaler: mean=0, std=1
# MinMaxScaler: scales to 0-1 range

# 5. Train-test split
from sklearn.model_selection import train_test_split
X = df.drop("target", axis=1)
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

---

### 4.4 Model Evaluation

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, mean_squared_error, r2_score
)

# Classification metrics
y_pred = model.predict(X_test)

accuracy_score(y_test, y_pred)      # correct / total
precision_score(y_test, y_pred)     # TP / (TP + FP)
recall_score(y_test, y_pred)        # TP / (TP + FN)
f1_score(y_test, y_pred)            # harmonic mean of precision & recall
confusion_matrix(y_test, y_pred)    # [[TN, FP], [FN, TP]]

# Regression metrics
mean_squared_error(y_test, y_pred)  # avg squared error
r2_score(y_test, y_pred)            # 1.0 = perfect, 0 = as good as mean
```

**When to use which metric:**
| Metric | Use when |
|--------|----------|
| Accuracy | Balanced classes |
| Precision | False positives are costly (spam filter) |
| Recall | False negatives are costly (disease detection) |
| F1 | Imbalanced classes |
| R² | Regression problems |

---

### 4.5 Overfitting vs Underfitting

| Problem | Meaning | Fix |
|---------|---------|-----|
| Overfitting | Model memorizes training data, fails on new data | More data, regularization, simpler model, dropout |
| Underfitting | Model too simple, misses patterns | More features, complex model, more training |
| Good fit | Performs well on both train and test | Target |

**Regularization:**
- L1 (Lasso) — can zero out features (feature selection)
- L2 (Ridge) — shrinks all coefficients, doesn't zero out

---

### 4.6 Neural Networks Basics

```
Input Layer → Hidden Layers → Output Layer

Each connection has a weight.
Each neuron applies: output = activation(sum(weights * inputs) + bias)
```

**Activation Functions:**
| Function | Range | Use |
|----------|-------|-----|
| ReLU | [0, ∞) | Hidden layers (most common) |
| Sigmoid | (0, 1) | Binary output |
| Softmax | (0,1), sum=1 | Multi-class output |
| Tanh | (-1, 1) | Hidden layers |

**Training:**
- Forward pass → compute loss
- Backpropagation → compute gradients
- Gradient descent → update weights

```python
# Simple neural network with sklearn
from sklearn.neural_network import MLPClassifier

model = MLPClassifier(
    hidden_layer_sizes=(100, 50),   # 2 hidden layers
    activation='relu',
    max_iter=300
)
model.fit(X_train, y_train)
```

---

### 4.7 Pandas Quick Reference (Important)

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Nara", "Ram", "Sita"],
    "score": [85, 90, 78],
    "dept": ["IT", "IT", "HR"]
})

# Selection
df["name"]                        # column
df[["name", "score"]]             # multiple columns
df.loc[0]                         # row by label
df.iloc[0]                        # row by index
df[df["score"] > 80]              # filter
df[(df["score"] > 80) & (df["dept"] == "IT")]

# Operations
df["score"].mean()
df["score"].max()
df.groupby("dept")["score"].mean()
df.sort_values("score", ascending=False)
df.drop_duplicates()
df.rename(columns={"name": "Name"})
df.merge(df2, on="id", how="left")
df.pivot_table(values="score", index="dept", aggfunc="mean")
```

---

## INTERVIEW QUESTIONS BANK

### Python Questions

1. **What is the difference between `list`, `tuple`, `set`, `dict`?**
2. **What is GIL and how does it affect threading?**
3. **Explain decorators with an example.**
4. **What is the difference between `@staticmethod` and `@classmethod`?**
5. **What is a generator? How is it different from a list?**
6. **What is shallow copy vs deep copy?**
7. **Explain LEGB scope rule.**
8. **What is `*args` and `**kwargs`?**
9. **What are dunder/magic methods? Give examples.**
10. **How does Python's memory management work? (reference counting, garbage collection)**
11. **What is the difference between `is` and `==`?**
12. **What is a closure?**
13. **Explain `async/await`. When would you use it?**
14. **What is `__init__` vs `__new__`?**
15. **How is `dict` implemented internally in Python? (hash table)**

### AI/ML Questions

1. **What is the difference between supervised and unsupervised learning?**
2. **What is overfitting? How do you prevent it?**
3. **Explain bias-variance tradeoff.**
4. **What is cross-validation?**
5. **Difference between precision and recall?**
6. **When would you use Random Forest over Decision Tree?**
7. **What is gradient descent?**
8. **What is feature engineering?**
9. **What is normalization vs standardization?**
10. **What is a confusion matrix?**

### Prowesssoft-Specific (API + Integration)

1. **How do you design a REST API in Flask?**
2. **What are HTTP methods and when to use each?**
3. **How do you handle authentication in APIs? (JWT, API keys)**
4. **What is Kafka? How does producer-consumer work?**
5. **What is the difference between message queue and event streaming?**
6. **How do you handle API rate limiting?**
7. **What is idempotency in APIs?**

---

## RESOURCES

| Topic | Resource |
|-------|----------|
| Python Practice | leetcode.com (Easy/Medium) |
| Python Docs | docs.python.org |
| ML Basics | scikit-learn.org/stable/tutorial |
| ML Course | fast.ai (free, practical) |
| Pandas | pandas.pydata.org/docs/getting_started |

---

## QUICK REVISION CHECKLIST

### Before the interview:
- [ ] OOP: class, inheritance, polymorphism, dunder methods
- [ ] Decorators: write one from scratch
- [ ] Generators: explain yield, write a generator
- [ ] `*args`, `**kwargs`: explain and use
- [ ] List/dict comprehension
- [ ] `map`, `filter`, `zip`, `enumerate`
- [ ] shallow vs deep copy
- [ ] try/except/finally
- [ ] REST API: write CRUD endpoints in Flask
- [ ] Kafka: explain topic, partition, consumer group (you already know this well)
- [ ] ML: explain overfitting, metrics, train-test split
- [ ] Pandas: groupby, merge, filter

---

*Last updated: April 2026*
