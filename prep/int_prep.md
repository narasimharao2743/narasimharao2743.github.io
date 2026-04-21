# Interview Preparation Guide
**Based on:** Narasimharao Bhavirisetty — Software Engineer Resume  
**Experience:** 1.6+ years — Spizen Technologies + Algonox Technologies  
**Focus:** Python, Kafka, PyFlink, ClickHouse, Redis, Flask, REST APIs, Data Pipelines

---

## HOW TO USE THIS GUIDE

Every section maps directly to something on your resume. Interviewers will ask:
1. "Walk me through your resume" — use the self-introduction
2. "Tell me about your work at Spizen/Algonox" — use the project explanations
3. "Technical questions" on each technology you listed
4. "Behavioral questions" — STAR format answers
5. "HR questions" at the end

---

## PART 1: SELF INTRODUCTION

**Prepare a 90-second answer for "Tell me about yourself":**

> "I'm Narasimharao, a Software Engineer with 1.6 years of experience. I currently work at Spizen Technologies where I build real-time data pipelines for a Solana blockchain intelligence platform. My core work involves processing 50,000+ trade events per day using Apache Kafka, PyFlink, ClickHouse, and Redis — building streaming jobs, classification systems, and scoring engines.
>
> Before this, at Algonox Technologies, I worked on backend automation — I built data cleaning systems, automated reporting, and user lifecycle management modules in Python, improving data extraction accuracy by 40%.
>
> My strongest skills are Python, Kafka-based event streaming, and building production backend systems. I'm looking for a role where I can continue working on backend/data engineering challenges."

**Key rules:**
- Keep it under 2 minutes
- Always end with what you're looking for
- Don't read — practice until it flows naturally

---

## PART 2: PROJECT EXPLANATIONS

### Spizen Technologies — What You Built

**If asked "What did you do at Spizen?"**

> "At Spizen I built a Solana blockchain intelligence platform. The platform monitors live token trading activity on Solana and generates real-time investment signals.
>
> I built multiple streaming pipeline jobs. The core pipeline ingests raw trade events from Solana — things like buy/sell transactions on Pump.fun — through a Kafka topic. These events then go through PyFlink jobs that deduplicate and aggregate them using tumbling windows, and the results are stored in ClickHouse for analytics and Redis for fast real-time lookups.
>
> I also built a wallet classification system that analyzes trading behavior patterns to detect bot wallets — accounts doing wash trading or suspicious activity. And a composite scoring engine that combines wallet quality, token quality, and market density signals to generate live investment signals."

**Follow-up questions they will ask:**

**Q: What is a tumbling window in PyFlink?**
> A tumbling window is a fixed-size, non-overlapping time window. For example, a 1-minute tumbling window groups all events in that 1-minute interval together, closes, and a new window starts. We used it to aggregate trade data — summing volume, counting trades, calculating price — for each token in fixed time periods. No two windows overlap, so every event belongs to exactly one window.

**Q: Why did you use Kafka?**
> Kafka is a distributed event streaming platform. We chose it because it handles high throughput — thousands of trade events per second from the Solana blockchain. It's fault-tolerant (data is persisted on disk), supports multiple consumers reading the same topic independently, and allows replaying events if something goes wrong. It acts as the backbone between our data ingestion and processing layers.

**Q: Why ClickHouse and not MySQL or PostgreSQL?**
> ClickHouse is a columnar database optimized for analytical queries on large datasets. MySQL and PostgreSQL are row-oriented — good for transactional (OLTP) workloads. We needed to run aggregation queries (sum, count, avg) over millions of trade records very fast. ClickHouse handles that in milliseconds because it stores data column by column — so when you query only 3 columns out of 20, it only reads those 3. MySQL would read the entire row. For our use case — analytics on streaming trade data — ClickHouse was the right choice.

**Q: Why Redis?**
> Redis is an in-memory key-value store. We used it for fast real-time lookups — things like checking the current state of a coin (is it graduated, dead, active?) without hitting ClickHouse on every event. Redis operations are microsecond-level. It also stores intermediate pipeline state and pub/sub signals. The tradeoff is it's in-memory so it's not for permanent storage — that's what ClickHouse is for.

**Q: What is fault-tolerant checkpointing in PyFlink?**
> Checkpointing is PyFlink's mechanism for fault tolerance. Periodically, Flink takes a snapshot of the entire job state — including Kafka offsets and in-flight aggregation windows — and saves it to a durable store. If the job crashes, it restarts from the last checkpoint rather than from scratch. This means no data loss and no double-counting. We configured checkpointing every few minutes so in case of a failure, we'd only reprocess a small window of events.

**Q: How does your wallet bot classification work?**
> We analyze behavioral patterns of wallets — things like trade frequency, timing between trades, whether a wallet always buys and sells within a very short window (wash trading), whether it only interacts with a specific set of tokens repeatedly. Based on these behavioral signals we assign a bot score. Wallets above a threshold are classified as bots and their trades are downweighted or excluded from investment signals.

---

### Algonox Technologies — What You Built

**If asked "What did you do at Algonox?"**

> "At Algonox I worked on backend automation and data processing. The main product was a document processing platform.
>
> My key contribution was improving data extraction accuracy by 40% — I implemented multi-layered business rule validation to clean and reconcile noisy input data. The raw data coming in had inconsistencies, missing fields, wrong formats — I wrote Python logic to detect and fix these programmatically.
>
> I also built an automated email notification system for SLA alerts, a KPI reporting module that tracked extraction accuracy over time, and a User Dormancy Management Module that automatically transitioned user accounts based on inactivity — for security and access control."

**Follow-up questions:**

**Q: How did you achieve 40% improvement in data extraction accuracy?**
> The raw input data was messy — inconsistent formats, missing mandatory fields, wrong data types, duplicate records. I analyzed the error patterns and wrote Python rule-based validators. For example: if a field was blank, check if it could be derived from another field. If a date was in the wrong format, normalize it. If there were duplicate entries, keep the most recent. I also added pre-processing steps to standardize input before extraction. The combination of these rules reduced extraction failures significantly.

**Q: What is the User Dormancy Management Module?**
> It's a scheduled Python job that runs periodically. It checks all user accounts and their last activity timestamp. If a user hasn't logged in or performed any action for a configurable number of days, the system automatically transitions their account to a "dormant" state — restricting access. If they stay dormant longer, the account is deactivated. This is a security best practice — inactive accounts are a security risk. I used scheduled tasks (like cron-based triggers) to run these checks automatically.

---

## PART 3: TECHNICAL QUESTIONS BY SKILL

---

### PYTHON

**Q: What are the key features of Python?**
> Interpreted, dynamically typed, object-oriented, high-level. Key features: readable syntax, extensive standard library, supports multiple paradigms (OOP, functional), memory management via garbage collection, large ecosystem (pip packages).

**Q: What is the difference between a list and a tuple?**
> List is mutable (can be modified), tuple is immutable (cannot be modified after creation). Lists use `[]`, tuples use `()`. Tuples are faster and can be used as dictionary keys. Use tuples for fixed data, lists for data that changes.

**Q: What is a decorator? Can you write one?**
```python
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time()-start:.4f}s")
        return result
    return wrapper

@timer
def process():
    return sum(range(1000000))
```
> A decorator wraps a function to add behavior without modifying the original code.

**Q: What is a generator?**
> A function that uses `yield` to produce values one at a time. Memory efficient — doesn't store all values in memory. Used for streaming large datasets.
```python
def read_events(topic):
    for event in kafka_consumer:
        yield event   # processes one at a time
```

**Q: What is GIL?**
> Global Interpreter Lock — allows only one thread to execute Python bytecode at a time. For CPU-bound tasks, use multiprocessing. For I/O-bound tasks (network, file), threading still helps because GIL is released during I/O waits.

**Q: Difference between `deepcopy` and `copy`?**
> `copy.copy()` — shallow copy, new outer object but inner objects are shared. `copy.deepcopy()` — completely independent copy. Modifying deep copy doesn't affect original.

**Q: What is `*args` and `**kwargs`?**
> `*args` — variable positional arguments collected as tuple. `**kwargs` — variable keyword arguments collected as dict.

**Q: OOP concepts — explain with example from your work.**
> I used OOP heavily at Spizen. For example, the `TradeUpdater` class encapsulated all logic for processing trade events — methods for price calculation, state checking, write operations. Inheritance was used in the base job class that all streaming jobs extended. Each job overrode the `process()` method — polymorphism. Encapsulation meant internal state like the `finalized_cache` set was managed inside the class.

---

### KAFKA

**Q: What is Kafka? Explain the architecture.**
> Kafka is a distributed event streaming platform. Architecture:
> - **Producer** — publishes messages to topics
> - **Topic** — named stream of records
> - **Partition** — topic is split into partitions for parallelism. Each partition is an ordered, immutable sequence
> - **Broker** — Kafka server that stores data
> - **Consumer** — reads messages from topics
> - **Consumer Group** — multiple consumers sharing work. Each partition assigned to exactly one consumer in the group
> - **Offset** — position of a message in a partition. Consumers track offsets to know where they left off
> - **Zookeeper/KRaft** — manages broker metadata and leader election

**Q: What is a consumer group? Why is it important?**
> A consumer group allows multiple consumers to share the load of reading a topic. Each partition is assigned to exactly one consumer in the group — so work is parallelized. If one consumer crashes, Kafka rebalances and reassigns its partitions to other consumers in the group. This is how we scaled our pipeline — multiple consumers in a group to process events in parallel.

**Q: What is the difference between at-least-once and exactly-once delivery?**
> - **At-most-once** — message might be lost, never duplicated. Commit before processing.
> - **At-least-once** — message never lost, might be duplicated. Commit after processing. Most common.
> - **Exactly-once** — never lost, never duplicated. Requires Kafka transactions. Complex to implement.
> We used at-least-once — commit offsets only after successful processing of the entire batch. If processing fails, we reprocess from last committed offset.

**Q: What is `auto.offset.reset` — earliest vs latest?**
> - `earliest` — start reading from the beginning of the topic (all historical messages)
> - `latest` — start reading only new messages arriving after consumer starts
> We used `earliest` so that on restart or new deployment, we don't miss any historical events.

**Q: What happens if a consumer doesn't commit offsets?**
> It will reprocess messages from the last committed offset on restart. This is why we use manual commit (`enable.auto.commit=False`) and commit only after successful processing — guarantees at-least-once delivery.

**Q: What is a Kafka partition key?**
> A key that determines which partition a message goes to. Messages with the same key always go to the same partition — ensuring ordering for that key. For example, if we use `mint` (token address) as the key, all trades for the same token go to the same partition — so they're processed in order.

---

### PYFLINK

**Q: What is Apache Flink / PyFlink?**
> Apache Flink is a distributed stream processing framework. PyFlink is the Python API for Flink. It processes unbounded (never-ending) data streams in real-time. Key features: event-time processing, windowing, stateful computation, fault-tolerant checkpointing, exactly-once semantics.

**Q: What is a tumbling window? Difference from sliding window?**
> - **Tumbling window** — fixed size, non-overlapping. Each event belongs to exactly one window. Example: 1-minute tumbling window groups events 0:00-1:00, 1:00-2:00, etc.
> - **Sliding window** — fixed size, overlapping. Window slides by a step. Example: 1-minute window sliding every 30 seconds — events can belong to multiple windows.
> - **Session window** — gaps-based. Window closes after a period of inactivity.
> We used tumbling windows to aggregate trade data per time period without double-counting.

**Q: What is checkpointing in Flink?**
> Checkpointing takes a consistent snapshot of all job state (including Kafka offsets, window state, accumulators) and saves to durable storage. On failure, job restarts from last checkpoint — no data loss. It's the mechanism for fault tolerance in Flink.

**Q: What is watermark in Flink?**
> A watermark is a signal that tells Flink "all events with timestamp ≤ T have arrived." It handles out-of-order events. Flink waits for the watermark before closing a time window and computing results. Without watermarks, late-arriving events would be dropped or cause incorrect results.

---

### CLICKHOUSE

**Q: What is ClickHouse? Why use it?**
> ClickHouse is an open-source columnar database management system designed for OLAP (Online Analytical Processing). It's optimized for read-heavy analytical workloads — aggregations over billions of rows in milliseconds. We used it to store and query trade events, coin metrics, and wallet data.

**Q: What is a columnar database vs row-oriented?**
> - **Row-oriented (MySQL, PostgreSQL)** — stores all columns of a row together. Fast for reading entire rows (OLTP — transactions, inserts, updates).
> - **Columnar (ClickHouse)** — stores each column separately. Fast for reading specific columns across millions of rows (OLAP — aggregations, analytics). When you `SELECT sum(volume)`, it only reads the volume column, not all columns.

**Q: What is the MergeTree engine in ClickHouse?**
> MergeTree is ClickHouse's primary table engine. Data is written in sorted chunks ("parts") and periodically merged in the background. It supports primary keys, partitioning, and ordering. Variants: ReplacingMergeTree (deduplication), AggregatingMergeTree (pre-aggregation), SummingMergeTree (auto-summation).

**Q: How do you handle updates in ClickHouse?**
> ClickHouse is designed for inserts, not updates. Updates are done via `ALTER TABLE ... UPDATE` which is an async operation — it rewrites data parts in the background. For real-time updates, we used `ReplacingMergeTree` which keeps only the latest version of a row based on a version column during merges. In our pipeline we used `ALTER UPDATE` for updating coin states.

---

### REDIS

**Q: What is Redis? What data structures does it support?**
> Redis is an in-memory data structure store used as a database, cache, and message broker. Data structures: String, List, Hash, Set, Sorted Set, Pub/Sub, Streams, HyperLogLog.

**Q: When would you use Redis vs a regular database?**
> Redis for: sub-millisecond lookups, caching, session storage, real-time leaderboards, pub/sub messaging, rate limiting. Regular DB for: permanent storage, complex queries, relationships, large data that doesn't fit in memory.

**Q: What is Redis TTL?**
> TTL (Time To Live) — sets an expiry time on a key. After TTL expires, the key is automatically deleted. Used for caching (invalidate stale data), session management, rate limiting windows.

**Q: What is Redis pub/sub?**
> Publisher-Subscriber pattern. Publishers send messages to channels. Subscribers listen to channels and receive messages. It's fire-and-forget — no persistence, no acknowledgment. We used it for real-time signal broadcasting in the pipeline.

**Q: How did you use Redis in your project?**
> Redis served as our fast lookup layer. When a new trade event arrived, instead of querying ClickHouse (slower) to check the current state of a coin (active/graduated/dead), we first checked Redis. Redis cached coin states, wallet scores, and pipeline metadata. This reduced ClickHouse load significantly and kept latency low.

---

### FLASK / REST APIs

**Q: What is Flask?**
> Flask is a lightweight Python web framework for building web apps and REST APIs. It's minimal — provides routing, request handling, response formatting. No ORM, no admin panel built-in (unlike Django). You add only what you need.

**Q: What is REST?**
> Representational State Transfer — architectural style for APIs using HTTP. Key principles: stateless, resources identified by URLs, HTTP methods for CRUD (GET=read, POST=create, PUT=update, DELETE=remove), returns JSON/XML.

**Q: What are HTTP status codes?**
> 200 OK, 201 Created, 204 No Content, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 500 Internal Server Error.

**Q: What is the difference between PUT and PATCH?**
> PUT replaces the entire resource. PATCH partially updates a resource. Example: PUT sends all fields, PATCH sends only changed fields.

**Q: How do you secure a REST API?**
> API Keys (simple, server-to-server), JWT tokens (stateless auth, scalable), OAuth2 (delegated auth). Validate all inputs, use HTTPS, rate limiting, proper error messages that don't expose internals.

---

### SQL / MySQL

**Q: What is the difference between WHERE and HAVING?**
> WHERE filters rows before aggregation. HAVING filters groups after aggregation.
```sql
SELECT dept, COUNT(*) FROM employees
WHERE salary > 50000          -- filter rows first
GROUP BY dept
HAVING COUNT(*) > 5           -- filter groups after
```

**Q: What are indexes? When to use them?**
> An index is a data structure that speeds up data retrieval. Without an index, database scans every row (full table scan). With an index, it jumps directly to matching rows. Use on columns frequently used in WHERE, JOIN, ORDER BY. Downside: slows down INSERT/UPDATE because index must be updated.

**Q: What is a JOIN? Types?**
> INNER JOIN — only matching rows from both tables. LEFT JOIN — all rows from left, matching from right (NULL if no match). RIGHT JOIN — opposite. FULL OUTER JOIN — all rows from both.

**Q: What is a subquery?**
> A query nested inside another query.
```sql
SELECT name FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
```

**Q: What is normalization?**
> Organizing database to reduce redundancy. 1NF — atomic values, no repeating groups. 2NF — no partial dependency. 3NF — no transitive dependency. Goal: each piece of data stored once.

---

### GIT

**Q: What is Git? What is the difference between Git and GitHub?**
> Git is a distributed version control system — tracks changes in code. GitHub is a hosting platform for Git repositories with collaboration features (PRs, issues, actions).

**Q: What is the difference between `git merge` and `git rebase`?**
> `git merge` — combines two branches, creates a merge commit. Preserves history. `git rebase` — moves commits from one branch onto another, rewrites history. Cleaner linear history but rewrites commits — don't rebase shared branches.

**Q: What is `git stash`?**
> Temporarily saves uncommitted changes so you can switch branches. `git stash` saves, `git stash pop` restores.

**Q: What is a pull request?**
> A request to merge code from one branch to another. Allows team members to review code before merging. Includes diff view, comments, approvals.

**Q: What commands do you use daily?**
> `git status`, `git add`, `git commit`, `git push`, `git pull`, `git branch`, `git checkout`, `git log`, `git diff`, `git stash`

---

### PROTOBUF

**Q: What is Protobuf?**
> Protocol Buffers — Google's language-neutral, platform-neutral serialization format. More efficient than JSON — smaller binary size, faster serialization/deserialization. You define a schema in a `.proto` file, generate code, and serialize/deserialize objects using that schema.

**Q: Why use Protobuf instead of JSON?**
> JSON is human-readable but verbose and slow to parse. Protobuf is binary — 3-10x smaller, 5-10x faster to serialize. For high-throughput systems like ours (50K+ events/day through Kafka), this difference matters. The downside is it's not human-readable — you need the schema to decode.

**Q: How did you use Protobuf?**
> Solana trade events arriving in Kafka were serialized as Protobuf binary messages. We had `.proto` files defining the `TradeEntry` message schema — fields like `mint`, `virtual_sol_reserves`, `virtual_token_reserves`, `slot`. We used `ParseFromString()` to deserialize incoming Kafka messages into Python objects.

---

## PART 4: BEHAVIORAL QUESTIONS (STAR FORMAT)

**STAR = Situation, Task, Action, Result**

---

**Q: Tell me about a challenging problem you solved.**

> **Situation:** At Spizen, we were getting duplicate trade records in our ClickHouse analytics because the same trade event was being processed multiple times during Kafka consumer restarts.
> **Task:** I needed to ensure each trade event was processed exactly once.
> **Action:** I implemented deduplication logic using PyFlink tumbling windows with fault-tolerant checkpointing. Within each window, I grouped events by trade ID and kept only unique records. Also configured Kafka consumer to commit offsets only after successful batch processing.
> **Result:** Reduced duplicate records by approximately 95%, ensuring data integrity for downstream analytics and investment signals.

---

**Q: Tell me about a time you improved system performance.**

> **Situation:** At Algonox, the document data extraction system had a high error rate — around 40% of extractions were failing or producing incorrect output.
> **Task:** Improve extraction accuracy.
> **Action:** I analyzed patterns in the failed extractions. Most failures were due to inconsistent input data — wrong formats, missing fields, duplicates. I implemented multi-layered validation rules in Python: format normalization, missing field derivation, duplicate removal, and pre-processing standardization.
> **Result:** Improved extraction accuracy by 40%, significantly reducing manual correction work and improving SLA compliance.

---

**Q: Tell me about a time you worked under pressure.**

> **Situation:** At Spizen, a production pipeline job crashed during peak trading hours — live investment signals stopped being generated.
> **Task:** Diagnose and fix the issue as quickly as possible.
> **Action:** I checked Kafka consumer lag metrics to understand how far behind we were. Found the issue — a null pointer in the price calculation when `virtual_token_reserves` was zero for certain edge case tokens. Added validation to skip such tokens. Redeployed the fix.
> **Result:** Pipeline was back online within the hour. Added the validation to prevent recurrence. Also added monitoring alerts for similar failures.

---

**Q: Tell me about a time you learned something new quickly.**

> **Situation:** When I joined Spizen, I had no prior experience with PyFlink or Solana blockchain.
> **Task:** Get productive quickly on a complex real-time streaming system.
> **Action:** I started by reading PyFlink documentation and running small local examples. For Solana/blockchain, I studied the Pump.fun trading model to understand what the events meant. I read the existing codebase carefully before touching anything. Asked senior engineers specific questions rather than broad ones.
> **Result:** Within the first month I was contributing independently to the streaming jobs and eventually designed and built new jobs from scratch.

---

**Q: Describe a time you disagreed with a decision.**

> **Situation:** At Algonox, the initial approach was to manually fix data errors case-by-case rather than building automated validation.
> **Task:** I believed a systematic automated solution would be more effective long-term.
> **Action:** I documented the patterns I found in failed extractions, estimated the time saved by automating vs manual fixing, and presented it to my lead. I proposed building a rule-based validation layer.
> **Action:** My lead agreed and gave me time to implement it.
> **Result:** The automated solution handled the majority of cases without manual intervention, saving the team significant time and improving accuracy by 40%.

---

## PART 5: HR QUESTIONS

**Q: Why are you looking for a new job?**
> "I've learned a lot at Spizen — building real-time streaming systems at scale has been great experience. I'm looking for a role where I can continue growing, work on larger systems, and be part of a bigger team where I can learn from experienced engineers."

**Q: What is your expected salary?**
> Research market rate first. For 1.6 years Python/data engineering in Hyderabad/Bangalore: ₹6-10 LPA is realistic. Say: "I'm expecting between ₹X and ₹Y based on the role and responsibilities. I'm open to discussion."

**Q: Where do you see yourself in 5 years?**
> "I want to deepen my expertise in backend and data engineering — working on distributed systems, large-scale pipelines, and eventually taking on technical leadership responsibilities. I want to grow into a senior engineer who can design systems end-to-end."

**Q: Why do you want to join this company?**
> Research the company before the interview. Mention something specific about their tech stack, product, or growth. Never say "for the salary" or "I just need a job."

**Q: What are your strengths?**
> "My strongest skill is Python — I've used it across data pipelines, automation, and backend systems. I'm also good at debugging production systems and understanding how distributed systems work. I pick up new technologies quickly — I learned PyFlink and Kafka on the job at Spizen."

**Q: What are your weaknesses?**
> "I sometimes spend too long trying to solve a problem independently before asking for help. I've been working on recognizing earlier when it's better to ask rather than debug alone for too long."

**Q: Are you open to relocation?**
> Be honest. If you're open to Hyderabad/Bangalore, say yes. If not, say which cities you prefer.

---

## PART 6: QUESTIONS TO ASK THE INTERVIEWER

Always ask 2-3 questions at the end — shows interest and preparation.

- "What does the typical day look like for this role?"
- "What tech stack does the team use?"
- "What are the biggest technical challenges the team is currently working on?"
- "How does the onboarding process work?"
- "What does growth look like for this role?"

---

## PART 7: PRE-INTERVIEW CHECKLIST

**1 day before:**
- [ ] Re-read your resume — know every word on it
- [ ] Practice self-introduction out loud — time it
- [ ] Review Kafka concepts (consumer group, offset, partition)
- [ ] Review PyFlink (tumbling window, checkpointing)
- [ ] Review Python basics (OOP, decorators, generators, GIL)
- [ ] Review SQL basics (JOIN, GROUP BY, INDEX)
- [ ] Prepare STAR stories for 3-4 behavioral questions
- [ ] Research the company

**Day of interview:**
- [ ] Check internet connection (for online interviews)
- [ ] Keep resume PDF open
- [ ] Have a glass of water nearby
- [ ] Log in 5 minutes early
- [ ] Keep this prep guide nearby for quick reference

---

## PART 8: COMMON MISTAKES TO AVOID

- **Don't memorize answers** — understand concepts, explain in your own words
- **Don't say "I don't know" and stop** — say "I'm not sure about the exact details but my understanding is..." and give your best answer
- **Don't exaggerate** — if you only have basic knowledge of something, say "I have basic exposure to X, I've used it for Y"
- **Don't bad-mouth previous employers** — always frame negatives positively
- **Don't rush** — take a breath before answering. Silence for 2-3 seconds is fine
- **Don't forget to ask about next steps** at the end of the interview

---

*Last updated: April 2026*
