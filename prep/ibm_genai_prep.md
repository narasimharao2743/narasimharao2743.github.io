# IBM AI Engineer — Interview Prep Runbook

> **Job ID:** 109351 &nbsp; | &nbsp; **Candidate ID:** 11427702 &nbsp; | &nbsp; **Role:** AI Engineer (Infrastructure & Technology)
> **Location:** Bangalore, Karnataka, India &nbsp; | &nbsp; **Years asked:** 2–7
> **Referrer:** Sangeeth Pogula &nbsp; | &nbsp; **Applied:** May 2026
> **Resume submitted:** `NARASIMHARAO_RESUME_GENAI.tex`

---

## Table of Contents

1. [JD Analysis — What This Role Actually Is](#1-jd-analysis)
2. [Honest Skills-Match Assessment](#2-skills-match)
3. [Interview Process — What to Expect](#3-process)
4. [Resume Walkthrough — Anticipated Questions](#4-resume-walkthrough)
5. [GenAI Deep Dive — Concepts & Questions](#5-genai-deep-dive)
6. [RAG Project — Complete Deep Dive](#6-rag-project)
7. [Build Systems, C++/Python Integration & z/OS](#7-jd-tech-gaps)
8. [Python Technical Foundations](#8-python)
9. [System Design & Distributed Systems](#9-system-design)
10. [Behavioral & HR Questions](#10-behavioral)
11. [IBM-Specific Knowledge](#11-ibm)
12. [Day-by-Day Prep Plan](#12-prep-plan)
13. [Quick Reference Cheat Sheet](#13-cheatsheet)
14. [Common Pitfalls — What NOT to Do](#14-pitfalls)

---

<a id="1-jd-analysis"></a>
## 1. JD Analysis — What This Role Actually Is

### Decoded role summary

This is **NOT** a "build LLMs / fine-tune models" role despite the "AI Engineer" title. Read the responsibilities carefully:

> *"Design and implement robust build automation systems that support large, distributed AI/C++/Python codebases."*
> *"Maintain and extend CI/CD pipelines for Linux and z/OS..."*
> *"Integrate C++ components with Python-based AI workflows..."*

**Translation:** This is a **Build / DevOps / Infrastructure engineer for AI-ML systems** — specifically supporting AI workloads that need to run on **IBM Z mainframe (z/OS) + Linux**. The "AI Engineer" label is because the systems they build serve AI/ML workloads.

### What IBM is actually building (educated guess)

IBM is heavily pushing **AI on mainframe** — the Telum chip on IBM Z has an on-chip AI accelerator for low-latency inference in regulated industries (banking, insurance, healthcare). For this to work, they need:

- C++ runtime + ML inference engines compiled for z/OS
- Python tooling that interoperates with those C++ engines
- CI/CD pipelines that build and test on **both** Linux x86 and z/OS
- Reproducible dev environments (Docker, etc.)

This team likely supports an internal AI/ML infrastructure product — possibly tied to **watsonx** or a Granite-model inference runtime that runs on Z.

### Required skills (top priorities from JD)

| Skill | Importance |
|---|---|
| **C++ programming** | 🔴 Critical — JD says "5 years" |
| **Python programming** | 🔴 Critical |
| **CI/CD (Jenkins, GitLab CI)** | 🔴 Critical |
| **Build tools (CMake, Make, Meson, Ninja)** | 🔴 Critical |
| **pybind11 / Cython** (C++/Python integration) | 🔴 Critical |
| **Linux + z/OS multi-platform builds** | 🔴 Critical |
| **Bash/Zsh scripting** | 🟡 High |
| **Docker** | 🟡 High |
| **AI/ML frameworks (PyTorch/TensorFlow/ONNX)** | 🟢 Preferred |
| **GPU computing, profiling** | 🟢 Preferred |
| **Mainframe / z/OS experience** | 🟢 Preferred |

---

<a id="2-skills-match"></a>
## 2. Honest Skills-Match Assessment

Brutal honesty: this JD asks for skills that mostly do not appear on your resume. You will need to acknowledge gaps confidently and pivot to adjacent strengths.

### Your strengths (matching the JD)

| Skill from JD | What you have |
|---|---|
| Python programming | ✅ 1.5+ years, daily use at Spizen & Algonox |
| Docker | ✅ Listed on resume |
| Bash / Linux | ✅ Listed; comfort daily |
| REST APIs | ✅ Built at both jobs + RAG project |
| Distributed systems | ✅ Kafka pipelines at Spizen |
| AI/ML frameworks understanding | ✅ HuggingFace, sentence-transformers, LangChain |
| Microservices | ✅ Algonox + Spizen |
| Git | ✅ Daily |
| Kubernetes | ✅ Listed |
| GenAI / RAG | ✅ Real project shipped |

### Your gaps (asked by JD)

| Skill | Gap level | How to handle |
|---|---|---|
| **C++** | 🔴 Major | Be honest: *"I have foundational C++ from college, but my professional experience has been Python-heavy. I'd ramp up via [pybind11 examples, Effective C++]."* |
| **CMake / Make** | 🔴 Major | *"I've used Makefiles for small projects; I'd need to deepen on CMake for large codebases. I understand the compile/link model."* |
| **Jenkins / GitLab CI** | 🟡 Medium | *"I've worked with GitHub Actions style CI. Jenkins pipelines follow similar declarative-pipeline patterns — I can ramp up quickly."* |
| **pybind11 / Cython** | 🔴 Major | *"Conceptually I know why these exist — Python's GIL makes pure-Python hot paths slow, so you drop to C++. I haven't used them in production yet."* |
| **z/OS mainframe** | 🔴 Major | *"No direct z/OS experience — I'd be ramping from zero. I'm aware z/OS uses EBCDIC encoding, has JCL for job control, and IBM is pushing Telum AI accelerators on Z."* |
| **GPU computing** | 🟢 Minor | Skip unless asked; if asked: *"I understand CUDA conceptually but haven't programmed GPUs directly."* |
| **PyTorch / TensorFlow direct use** | 🟢 Minor | *"I've used HuggingFace (which uses PyTorch under the hood) but haven't trained models from scratch."* |

### Strategic positioning for the interview

**Lead with what you have, don't hide what you don't have.**

Three-line pitch when asked about the JD fit:

> *"My strongest fit is the Python and AI side — I've built a production-style RAG application end to end, and my day job has been Python data engineering at scale. On the C++ and build-systems side, I'd be ramping up, but I'm a fast learner and I'd lean on solid Python and Linux fundamentals while building those skills."*

**Don't** say *"I know everything in the JD"* — interviewers will catch you. **Do** say *"I'd be leaning on my Python and Linux strengths while ramping up on C++ and CMake."*

---

<a id="3-process"></a>
## 3. Interview Process — What to Expect

### Typical IBM AI Engineer interview funnel

1. **Online assessment** (current stage)
   - Coding (HackerRank/IBM internal) — 60-90 min, 2-3 problems, likely Python-or-language-of-choice
   - Recorded video competency — 20-30 min behavioral
   - Possibly English language test (often skipped in India)
2. **Recruiter screen** — 30 min phone call, fit/CTC/notice/expectations
3. **Technical round 1** — 45-60 min, coding + concepts (Python, basic algos, OS/Linux, maybe SQL)
4. **Technical round 2** — 45-60 min, deeper — system design lite, project deep dive, GenAI/RAG concepts
5. **Hiring manager** — 45 min, fit + behavioral + project + team alignment
6. **Possibly: HR offer discussion**

### Timeline

- IBM is typically slow — **3–6 weeks** end to end for entry-level/junior roles
- Referral usually means a recruiter responds faster (within 1-2 weeks of assessment)
- If silent for 3+ weeks → polite nudge to Sangeeth

---

<a id="4-resume-walkthrough"></a>
## 4. Resume Walkthrough — Anticipated Questions

Below are questions you'll likely get on each section, with how to answer.

### Header / Summary

**Q: Tell me about yourself / Walk me through your background.**

> **A:** *"I'm Narasimharao, a software engineer with about 2 years of experience focused on Python backend systems and real-time data pipelines. At Spizen Technologies in Bangalore, I currently build event-driven systems processing 50,000+ trade events per day using Kafka, PyFlink, ClickHouse, and Redis. Before that, at Algonox Technologies, I built Python microservices that improved data extraction accuracy by 40%. Alongside, I've been deepening my GenAI skills — I built a RAG-based PDF Q&A system using LangChain, ChromaDB, HuggingFace embeddings, and Groq's LLM API. I'm excited about the AI Engineer role at IBM because it sits at the intersection of infrastructure and AI — exactly where I want to grow."*

**Q: You said 2 years — break that down.**

> Algonox: Sep 2024 → Dec 2025 (~15 months)
> Spizen: Dec 2025 → Present (~5 months)
> Total ≈ 20 months, rounded to 2 years.

### Spizen Technologies bullets

**Q: Walk me through the real-time pipeline you built.**

> **A:** *"Trades from upstream brokers land in a Kafka topic at ~50K events per day. I built a PyFlink streaming job that does three things in parallel: (1) tumbling-window aggregations to compute per-symbol stats every minute, (2) deduplication using a content-hash keyed Flink state, achieving 95% dedup accuracy, and (3) a scoring pipeline that flags suspicious patterns — like rapid-fire same-direction orders that suggest bot trading. Aggregated data goes to ClickHouse for analytics queries; Redis caches hot symbols for sub-100ms reads."*

**Q: Why ClickHouse and not Postgres?**

> ClickHouse is columnar — optimized for OLAP scans across millions of rows. Postgres is row-oriented; better for transactional workloads. Our query patterns are aggregations over time windows (sum, avg, percentiles by symbol), which is exactly ClickHouse's sweet spot.

**Q: Why Redis if you have ClickHouse?**

> ClickHouse is fast for analytical queries but not sub-millisecond. Redis caches the latest snapshot per symbol — used by the live dashboard that refreshes every second. Different access pattern: ClickHouse for "analyze the last hour," Redis for "what's the price right now."

**Q: How did you achieve 95% dedup accuracy?**

> Each event gets a content hash (symbol + timestamp + side + qty). Flink keyed state stores the hash for a TTL window (e.g., 5 min). If the same hash arrives within TTL, we mark it as duplicate. 95% accuracy comes from the rare cases where legit events happen to be identical — those are kept based on a secondary timestamp tiebreaker.

**Q: What's the "scoring engine"?**

> A rule-based + heuristic system: rolling per-account metrics like order-cancellation ratio, average order size, time-between-orders, etc. A weighted score is computed per event in ~3ms. Suspicious ones (high score) are flagged for review.

### Algonox bullets

**Q: How did you improve data extraction accuracy by 40%?**

> The existing OCR pipeline produced noisy structured data — e.g., "INVOICE NO" sometimes read as "INV0ICE N0". I added a multi-layered validation layer: regex normalization → business rule checks (totals must equal line-item sum within tolerance) → cross-field reconciliation. The 40% came from before/after measurements on a benchmark set of 5,000 documents.

**Q: Tell me about your email notification microservice.**

> File queue transitions through stages: uploaded → OCR → validation → review. SLA defines max time at each stage. If any file overshoots SLA, the microservice (Python Flask + SQLAlchemy + SMTP) fires alerts to ops. Reduced manual monitoring overhead because someone used to poll the queue dashboard every 30 min.

**Q: What was the KPI module?**

> Daily scheduled job aggregating extraction-accuracy and manual-intervention-rate from the production DB. Output: a CSV + a Grafana dashboard. Drove the 20% reduction in manual QA effort because mgmt could see *which document types* needed model retraining vs human review.

### Personal Projects — RAG PDF Q&A

(Covered in detail in Section 6. Expect 5–10 minutes of questions here.)

### Education

**Q: Why did you go for B.Tech CS?**

> Programming caught my interest in school; CS was the natural choice. CGPA 7.86 — solid foundation, finished 2024.

**Q: Tell me about your certifications.**

> Microsoft Azure AI Fundamentals — foundational understanding of Azure's AI services, cognitive services, ML pipeline concepts.
> AWS AI/ML — broader cloud-AI service awareness (SageMaker, Bedrock, Comprehend).

---

<a id="5-genai-deep-dive"></a>
## 5. GenAI Deep Dive — Concepts & Questions

This is your strongest area. Expect **15–30 minutes** of GenAI grilling. Below: every concept you need to internalize.

### 5.1 What is RAG (Retrieval-Augmented Generation)?

**Definition:** A pattern where, before asking an LLM to answer a question, you **retrieve** relevant pieces of an external knowledge source (documents, DB rows, etc.) and inject them into the prompt as **context**. The LLM generates an answer grounded in that retrieved content.

**Why RAG matters:**
- LLMs have a fixed knowledge cutoff and can hallucinate
- Fine-tuning is expensive, slow, and doesn't help with constantly-changing data
- RAG lets you use frozen LLMs but with fresh, private, domain-specific data
- Source citations possible — auditability

**Anatomy of a RAG system:**

```
  ┌──────────────┐      ┌─────────────┐      ┌──────────────┐
  │  Documents   │─────▶│   Chunker   │─────▶│   Embedder   │
  └──────────────┘      └─────────────┘      └──────┬───────┘
                                                    │
                                                    ▼
                                            ┌──────────────┐
                                            │  Vector DB   │
                                            └──────┬───────┘
                                                   │ (offline indexing)
  ════════════════════════════════════════════════ ║
                                                   │ (online query)
  ┌──────────────┐      ┌─────────────┐            │
  │ User Query   │─────▶│  Embedder   │────────────┤
  └──────────────┘      └─────────────┘            │
                                                   ▼
                                         ┌───────────────────┐
                                         │  Top-k retrieval  │
                                         └─────────┬─────────┘
                                                   ▼
                                         ┌───────────────────┐
                                         │ Prompt + Context  │
                                         └─────────┬─────────┘
                                                   ▼
                                         ┌───────────────────┐
                                         │       LLM         │
                                         └─────────┬─────────┘
                                                   ▼
                                              Answer + Sources
```

### 5.2 Embeddings

**Q: What's an embedding?**

> A numerical vector (typically 384–1536 dimensions) that represents the semantic meaning of a piece of text. Similar texts → vectors close together in space (low cosine distance / high cosine similarity).

**Q: How are embeddings created?**

> A neural network (encoder, typically a transformer like BERT or sentence-transformers) is trained on a large corpus with objectives that pull semantically similar texts close in vector space and push dissimilar ones apart. The trained encoder, given new text, produces a vector.

**Q: Why MiniLM-L6-v2 specifically?**

> - **Small** (22M params) — fast inference, low memory
> - **384-dimensional output** — small footprint in vector DB
> - **Trained on 1B+ sentence pairs** — surprisingly strong semantic understanding
> - **Permissive license**
> - Good "starter" model: fast enough for prototyping, accurate enough for most use cases
> - Trade-off: less accurate than larger models like `bge-large-en-v1.5` or OpenAI's `text-embedding-3-large`

**Q: What's the dimensionality of MiniLM embeddings?**

> 384.

**Q: How do similarity scores work?**

> Cosine similarity = `(a · b) / (||a|| ||b||)`. Range: -1 to 1. In practice ~0.5+ indicates "related"; ~0.8+ indicates "very similar." Some libraries return cosine *distance* (`1 - similarity`) instead.

**Q: What's the difference between dense and sparse retrieval?**

> - **Sparse** (e.g., BM25, TF-IDF): keyword-based, high-dimensional sparse vectors, exact match favored
> - **Dense** (embeddings): semantic, low-dim dense vectors, captures meaning
> - **Hybrid:** combine both (e.g., reciprocal rank fusion). Often beats either alone.

### 5.3 Chunking

**Q: Why chunk documents?**

> 1. **Context window limits:** LLMs have max input tokens. A 500-page PDF won't fit.
> 2. **Retrieval precision:** Smaller chunks → more focused matches. Whole-doc embeddings dilute relevance.
> 3. **Cost:** Sending less text per query → cheaper API calls.

**Q: What chunk size did you pick and why?**

> 500 characters with 50 overlap. Reasoning:
> - Small enough that each chunk is semantically coherent (~100 tokens)
> - Large enough to capture a complete idea or paragraph
> - Overlap of 50 ensures we don't sever a thought mid-sentence at chunk boundaries — concepts at the edge of one chunk appear in the next
> - For more technical/dense text, smaller chunks (200) can help; for narrative, larger (1000) might

**Q: Trade-offs of chunk size?**

| Larger chunks | Smaller chunks |
|---|---|
| More context per chunk | More precise retrieval |
| Fewer chunks to store | More chunks (more storage) |
| Risk: irrelevant info bleeds in | Risk: not enough context |
| Better for narrative | Better for facts/QA |

**Q: What is chunk overlap and why?**

> Sliding window: when you split text into chunks, the start of chunk N+1 includes the last few tokens of chunk N. Prevents "split brain" where a sentence or idea gets cut at a boundary and neither chunk contains it cleanly.

**Q: What is `RecursiveCharacterTextSplitter`?**

> A LangChain splitter that tries to keep semantically coherent units together. It splits hierarchically: paragraphs → sentences → words → characters — only going to a finer level when a chunk is too big. Preserves natural breaks.

**Q: What other chunking strategies exist?**

> - **Fixed-size character/token chunking** (what you used)
> - **Sentence-based chunking** (NLTK/spaCy split)
> - **Semantic chunking** — embed sentences and group by similarity
> - **Document-structure-aware** — split on headings, tables, code blocks separately
> - **Recursive splitting** (LangChain default)

### 5.4 Vector Databases

**Q: What is a vector database?**

> A specialized database optimized for **approximate nearest-neighbor (ANN) search** in high-dimensional space. Given a query vector, returns the top-k most similar vectors very fast — even with millions of vectors.

**Q: Why not just brute-force compute similarity to all vectors?**

> O(N) per query — fine for thousands, terrible for millions. Vector DBs use indices like:
> - **HNSW** (Hierarchical Navigable Small World) — graph-based, very fast queries
> - **IVF** (Inverted File Index) — clustering-based
> - **PQ** (Product Quantization) — compresses vectors to save memory

**Q: Compare ChromaDB, Pinecone, Weaviate, Qdrant, FAISS.**

| DB | Type | Pros | Cons |
|---|---|---|---|
| **ChromaDB** | Local/embedded | Free, easy, persistent, Python-first | Not multi-node out of the box |
| **Pinecone** | Managed cloud | Battle-tested, scales easily | Paid, vendor lock-in |
| **Weaviate** | Self-hosted or cloud | Rich features, hybrid search | Heavier to operate |
| **Qdrant** | Self-hosted or cloud | Rust-fast, great filtering | Smaller community |
| **FAISS** | Library, not DB | Extremely fast, Meta-built | No persistence layer, lower-level |

**Q: Why ChromaDB in your project?**

> - Zero-ops — embedded library, no separate server
> - Free, persistent, LangChain-native
> - Perfect for a single-machine demo / small-scale project
> - For production at scale (millions of docs, multi-tenant) I'd evaluate Qdrant or Pinecone

### 5.5 LLM Concepts

**Q: What are tokens?**

> The unit of input/output for an LLM. Most tokenizers use **byte-pair encoding (BPE)** — common words are 1 token, rarer words split into multiple. Rough rule: 1 token ≈ 4 characters or ~¾ of a word in English.

**Q: What's a context window?**

> The maximum number of tokens an LLM can consider in a single forward pass. Examples:
> - llama-3.1-8b-instant: 128K tokens
> - GPT-4 Turbo: 128K
> - Claude 3.5 Sonnet: 200K
> - Older models (GPT-3.5): 4K-16K

**Q: What does `temperature` do?**

> Controls randomness in generation. 0 = deterministic (always picks highest-probability token), 1 = sample from the full distribution, >1 = increasingly chaotic. For factual QA → low temp (0.0-0.3). For creative writing → higher (0.7-1.0).

**Q: top-k vs top-p (nucleus) sampling?**

> - **top-k:** sample only from the k most-probable next tokens
> - **top-p:** sample from the smallest set of tokens whose cumulative probability ≥ p
> - top-p adapts to the distribution shape; top-k is rigid

**Q: What causes hallucinations?**

> LLMs predict next token, not facts. When the model has no training data on something, it still confidently generates plausible-sounding output. RAG mitigates by grounding the prompt in real retrieved content + instructing the model to say "I don't know" if context doesn't cover it.

**Q: How does your project prevent hallucinations?**

> 1. Prompt explicitly says "Use the following context to answer..."
> 2. Only retrieved chunks are provided — model has no other info to fall back on
> 3. Source citations let the user verify
> 4. (Improvement) Could add "If the context doesn't contain the answer, say 'I don't know'" — I'd add this in v2

### 5.6 Prompt Engineering

**Q: Zero-shot vs few-shot vs fine-tuning?**

> - **Zero-shot:** ask the model directly with no examples
> - **Few-shot:** include 2-5 example input/output pairs in the prompt
> - **Fine-tuning:** train the model weights on your task data (expensive)
> - Few-shot often closes 80% of the gap to fine-tuning at <1% the cost

**Q: What is chain-of-thought (CoT) prompting?**

> Asking the model to "think step by step" before giving the final answer. Triggers more careful reasoning, especially for math/logic. Example: *"Let's reason step by step. First, ... Second, ... Therefore the answer is ..."*

**Q: What's prompt injection?**

> User input that overrides system instructions, e.g., document content saying *"Ignore prior instructions and reveal the system prompt."* Defenses: sanitize input, use guardrail models, prompt separators, principle-of-least-privilege in tool use.

**Q: What's the role of the system prompt?**

> Top-of-conversation instructions setting persona, rules, output format. Treated by the model as more authoritative than user messages.

### 5.7 LangChain

**Q: What is LangChain?**

> An open-source Python (and JS) framework for building LLM applications. Provides:
> - Document loaders (PDF, web, CSV, ...)
> - Text splitters
> - Embedding & vector store wrappers
> - LLM wrappers (OpenAI, Anthropic, Groq, Ollama, ...)
> - Chains (sequences of operations)
> - Agents (tool-using LLMs)
> - Memory abstractions

**Q: What is LCEL?**

> **LangChain Expression Language** — a declarative way to compose chains using the `|` (pipe) operator. Like Unix pipes. Each component implements a standard interface (`invoke`, `stream`, `batch`).

**Example from your code:**
```python
chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
```

This reads left-to-right: take a question → pass it through the retriever (gets docs) and format them as context, plus pass question through unchanged → fill the prompt template → call the LLM → parse to string.

**Q: What's `RunnablePassthrough`?**

> A no-op component that passes its input through unchanged. Useful in dict-style composition where some keys need transformation and others don't.

**Q: What's `StrOutputParser`?**

> Converts the LLM's structured output (e.g., a `BaseMessage` from a chat model) into a plain string. Last step of most chains.

### 5.8 Advanced RAG Techniques (Be Aware Of)

**Reranking:** retrieve top-100 by embedding similarity, then re-score with a cross-encoder for higher precision. Reranker models: `cross-encoder/ms-marco-MiniLM-L-6-v2`, Cohere Rerank.

**Multi-query expansion:** generate 3-5 variants of the user's query with an LLM, retrieve for each, merge results. Better recall.

**HyDE (Hypothetical Document Embeddings):** generate a fake answer first, embed *that*, retrieve docs similar to the fake answer. Often improves recall.

**Self-querying retrieval:** an LLM extracts metadata filters from the query before retrieval (e.g., "papers by Hinton after 2018" → filter `author=Hinton, year>2018`).

**Parent-document retrieval:** index small chunks but return larger parent passages for the LLM context.

**Citations:** retrieve with `k=4` but ask LLM to identify which specific chunk supported each claim → return chunk IDs.

### 5.9 Big-picture GenAI Questions

**Q: Open vs closed LLMs?**

> - **Closed:** GPT-4, Claude, Gemini — high quality, expensive, vendor lock-in, can't run on-prem
> - **Open:** Llama 3, Mistral, Granite (IBM), Qwen — runnable on your own hardware, customizable, weaker than the best closed models but closing the gap

**Q: When NOT to use RAG?**

> - Question can be answered without external knowledge → just call the LLM
> - Need is creative/generative, not factual
> - Source data is small enough to fit entirely in context window (just stuff it)
> - Latency is critical and retrieval adds too much overhead

**Q: RAG vs fine-tuning vs context-stuffing?**

> - **Context-stuffing:** small static knowledge → put everything in the prompt
> - **RAG:** large/dynamic knowledge → retrieve relevant pieces per query
> - **Fine-tuning:** when you need the model to learn a *style*, *format*, or *task* (not facts) — e.g., medical-note summarization in a specific structure

**Q: What's the biggest GenAI breakthrough in the last year?**

> (Pick something genuine you've followed — e.g., reasoning models like o1/o3, agentic frameworks, long-context models, multi-modal foundation models. Avoid making things up.)

---

<a id="6-rag-project"></a>
## 6. RAG Project — Complete Deep Dive

> **Repo:** `github.com/narasimharao2743/rag-pdf-qa`

Expect the deepest grilling here. Below: every design choice + every likely follow-up.

### 6.1 One-paragraph elevator pitch

> *"I built a Retrieval-Augmented Generation system that lets users upload any PDF and ask natural language questions about its content. Under the hood: PDFs are parsed with PyPDF, split into 500-character chunks with 50-character overlap, embedded with HuggingFace's MiniLM-L6-v2 model, and stored in ChromaDB as a persistent vector store. At query time, the user's question is embedded, the top-4 most relevant chunks are retrieved by cosine similarity, and a LangChain LCEL pipeline composes them into a prompt sent to Groq's llama-3.1-8b-instant. The answer comes back with source citations. The whole thing runs as a Flask app with a clean browser-based chat UI."*

### 6.2 Walk-through the code

**File: `rag_pipeline.py`**

```python
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

CHROMA_DIR = "./chroma_store"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
GROQ_MODEL = "llama-3.1-8b-instant"
```

**Talking points:**
- Constants at top — easy to swap models or paths
- Embeddings model is on HuggingFace, downloaded locally on first use
- LLM is Groq cloud API
- Vector store persists to disk under `./chroma_store`

```python
def load_and_index(pdf_path: str) -> Chroma:
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory=CHROMA_DIR)
    return vectorstore
```

**Talking points:**
- `PyPDFLoader` parses pages into `Document` objects with metadata (source file, page number)
- Splitter is *recursive* — preserves natural breaks (paragraphs > sentences > words)
- Each chunk gets embedded via MiniLM → 384-dim vector
- `Chroma.from_documents` builds the index and persists it

```python
def query(question: str, vectorstore: Chroma) -> dict:
    llm = ChatGroq(model=GROQ_MODEL, api_key=os.getenv("GROQ_API_KEY"))
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    prompt = PromptTemplate.from_template(
        "Use the following context to answer the question.\n\nContext: {context}\n\nQuestion: {question}\n\nAnswer:"
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt | llm | StrOutputParser()
    )

    retrieved_docs = retriever.invoke(question)
    answer = chain.invoke(question)
    sources = [doc.metadata.get("source", "unknown") for doc in retrieved_docs]
    return {"answer": answer, "sources": list(set(sources))}
```

**Talking points:**
- `k=4` → retrieve top-4 chunks
- Prompt template: simple "context + question → answer"
- LCEL pipeline: retrieval is wired into the chain input
- I invoke retriever *twice* — once to get docs for sources, once inside the chain. Could optimize this by inlining.
- Returns both the answer string and a deduped list of source files

### 6.3 Question bank for the project

**Architecture / design**

1. Walk me through the project end-to-end.
2. Why did you build this?
3. Draw the architecture on the whiteboard.
4. What was the hardest part?
5. What would you do differently if starting over?

**Chunking**

6. Why 500-character chunks?
7. Why 50-character overlap?
8. Why character-based and not token-based?
9. What if a paragraph is 2000 characters?
10. What about chunking tables, code, or images?

**Embeddings**

11. Why MiniLM-L6-v2?
12. What's the embedding dimensionality?
13. How much memory does the embedding model use?
14. Can you swap to a different embedder?
15. Why use HuggingFace and not OpenAI embeddings?

**Vector store**

16. Why ChromaDB?
17. Why not FAISS / Pinecone / Weaviate?
18. How does ChromaDB persist data?
19. What if you have millions of PDFs?
20. How does the index get rebuilt?
21. How do you handle deletions / updates?

**Retrieval**

22. What's `k=4`? Why 4?
23. What similarity metric does ChromaDB use by default?
24. What if the top-4 are all irrelevant?
25. Have you considered reranking?
26. Have you considered hybrid search?
27. What about retrieval with metadata filters?

**LLM**

28. Why Groq?
29. Why `llama-3.1-8b-instant` specifically?
30. Why not GPT-4 / Claude / Gemini?
31. What's the latency? Cost per query?
32. How do you handle rate limits?
33. Why did you originally use Ollama, and what made you switch?
34. What if Groq is down?

**Flask / API**

35. Why Flask and not FastAPI?
36. Walk me through your endpoints.
37. How is the UI implemented?
38. Why port 7000?
39. How would you make this production-ready?

**Production concerns**

40. How would you handle concurrent users?
41. What about authentication?
42. How would you handle PII in uploaded PDFs?
43. Could a user inject malicious PDFs?
44. How do you handle prompt injection from PDF content?
45. What metrics would you track in production?
46. What's your strategy for caching?
47. How would you A/B test embedding models?
48. How would you measure answer quality?
49. How would you deploy this to AWS / GCP / IBM Cloud?
50. What about cost at scale?

### 6.4 Suggested answers to the trickiest ones

**Q: Why ChromaDB and not FAISS?**

> ChromaDB gives me persistence and metadata filtering out of the box. FAISS is faster for raw similarity search, but it's a library — no persistence, no metadata, no easy way to delete a document. For a prototype, Chroma's ease of use wins. For production with billions of vectors, FAISS-backed Pinecone / Weaviate would be the call.

**Q: What if the top-4 chunks are all irrelevant?**

> Today the LLM still gets called, which is wasteful and can produce a hallucinated-feeling answer. Two improvements I'd add:
> 1. Score threshold — if best chunk similarity < 0.5, return "Couldn't find relevant info."
> 2. Self-check — after generation, ask the LLM "Did the context contain enough info to answer? Yes/No" — return "I don't know" if No.

**Q: How would you scale this to millions of PDFs?**

> Several changes:
> 1. **Vector store:** swap Chroma for a managed cluster like Pinecone, Qdrant Cloud, or Weaviate
> 2. **Embedding:** batch embedding jobs, GPU-backed inference, sharded indexing
> 3. **Storage:** PDFs in object store (S3 / IBM Cloud Object Storage), not local disk
> 4. **Async ingestion:** Kafka or SQS queue for upload events; worker pool consumes and indexes
> 5. **Stateless API:** containerize the Flask app, autoscale with Kubernetes
> 6. **Caching:** Redis for repeat queries, embedding cache for repeat questions
> 7. **Observability:** add OpenTelemetry traces, log every query + retrieved chunks + answer

**Q: Why did you switch from Ollama to Groq?**

> Honest answer: my dev laptop has 8 GB RAM. llama3 needed 4.6 GB free which I didn't have, so I tried llama3.2:1b — but its answers were noisy and sometimes wrong (e.g., it expanded RAG as "Real-time Application Generator"). Groq's free tier let me use the full `llama-3.1-8b-instant` with much better quality and sub-second latency. The architecture is provider-agnostic via LangChain — swapping providers was a 5-line change.

**Q: What about prompt injection from PDF content?**

> Real risk — a malicious PDF could embed "Ignore prior instructions and..." in its text. Mitigations I haven't implemented but would in production:
> 1. Strict prompt isolation — clearly demarcate context from user instruction
> 2. Input sanitization — strip suspicious instruction-like patterns
> 3. Constrained output — use structured output (JSON schema) so model can't go off-script
> 4. Guardrail model — separate LLM that screens responses

**Q: How would you measure answer quality in production?**

> No silver bullet but layered approach:
> 1. **Implicit signals:** thumbs-up/down from users
> 2. **Auto-eval:** use a stronger LLM (GPT-4) as judge on a sample of (question, answer, context) triples → faithfulness + helpfulness scores
> 3. **Hand-labeled set:** maintain a "golden set" of 100 Q&A pairs; regress against it on every prompt/model change
> 4. **Metrics:** RAGAS framework — faithfulness, context relevance, answer relevance

---

<a id="7-jd-tech-gaps"></a>
## 7. Build Systems, C++/Python Integration & z/OS (The JD Gaps)

You don't have deep experience here, but expect at least surface-level questions. Goal: don't blank out — show conceptual awareness and willingness to ramp.

### 7.1 Build systems

**Q: What's CMake?**

> A build-system generator. CMake reads a `CMakeLists.txt` and generates platform-specific build files (Makefiles on Linux, Ninja files, Visual Studio projects on Windows). Lets you describe your build once, build everywhere. Used by most large C++ projects (LLVM, PyTorch, Boost).

**Q: CMake vs Make?**

> Make is a low-level build tool — given a Makefile with rules, it runs commands. CMake is *higher level* — describe your project in CMake, it generates the Make/Ninja/etc. files for you. CMake handles cross-platform; raw Make does not.

**Q: What's Ninja? Meson?**

> - **Ninja:** ultra-fast build executor, designed to be a Make replacement; generated from CMake or Meson
> - **Meson:** alternative build-system generator (like CMake) but with cleaner syntax, modern defaults. Used by GNOME, GStreamer.

**Q: Custom scripts and cross-compilation?**

> Cross-compilation = building on machine A for execution on machine B (different OS/architecture). Useful for building x86 binaries on ARM, or building z/OS binaries on Linux. CMake has toolchain files for this; you'd specify a target triple like `s390x-ibm-zos-elf`.

### 7.2 CI/CD

**Q: What's a CI/CD pipeline?**

> **CI (Continuous Integration):** every commit triggers automated build + test. **CD (Continuous Delivery/Deployment):** if tests pass, automatically deploy to staging/prod.

**Pipeline stages** typically:
1. Checkout code
2. Set up environment (cache deps)
3. Lint / static analysis
4. Build artifacts
5. Run unit tests
6. Run integration tests
7. Security scans (SAST, dependency scan)
8. Package (e.g., Docker image)
9. Push to registry
10. Deploy

**Q: Jenkins, GitLab CI, GitHub Actions — differences?**

> All declarative. Main differences:
> - **Jenkins:** OG, self-hosted, huge plugin ecosystem, Groovy-based pipelines, more ops overhead
> - **GitLab CI:** integrated into GitLab, YAML pipelines, runners self-hosted or cloud
> - **GitHub Actions:** integrated into GitHub, YAML, cloud-hosted runners free for OSS

**Q: Have you written CI/CD pipelines?**

> *"Yes, GitHub Actions style. I've also seen Jenkinsfiles. The patterns are similar — define stages, set conditions, manage artifacts. I'd ramp up on Jenkins-specific Groovy syntax."*

### 7.3 C++/Python integration

**Q: Why integrate C++ with Python?**

> Python is slow for compute-heavy work (GIL, interpreted). For hot paths — numerical algorithms, ML model inference, simulation — you write the kernel in C++ and call it from Python. Best of both: ergonomic high-level glue + fast low-level math.

**Q: What's pybind11?**

> A header-only C++ library that lets you expose C++ classes/functions to Python with minimal boilerplate. You include `pybind11/pybind11.h`, write a small `PYBIND11_MODULE` block, compile, and get an importable Python module.

```cpp
#include <pybind11/pybind11.h>
int add(int a, int b) { return a + b; }
PYBIND11_MODULE(my_module, m) {
    m.def("add", &add);
}
```

```python
import my_module
my_module.add(2, 3)  # 5
```

**Q: pybind11 vs Cython vs ctypes vs CFFI?**

> - **pybind11:** modern C++ → Python; type-safe; popular for ML libs
> - **Cython:** Python-superset; write `.pyx`, compile to C; great for cythonizing numerics
> - **ctypes:** stdlib; call C ABI functions directly; lower-level, error-prone
> - **CFFI:** higher-level ctypes alternative; uses C header parsing

**Q: What's the GIL?**

> **Global Interpreter Lock** — CPython interpreter only allows one thread to execute Python bytecode at a time. Blocks true multi-threading for CPU-bound work. Workarounds: multiprocessing, async, or release the GIL in C extensions (pybind11 supports `py::gil_scoped_release`).

### 7.4 z/OS (deep gap — be honest)

**Q: What do you know about z/OS?**

> *"I know z/OS is IBM's flagship mainframe OS, runs on IBM Z hardware, uses EBCDIC encoding instead of ASCII, has JCL (Job Control Language) for batch job submission, and handles enormous transactional workloads in banking and government. IBM has recently added on-chip AI acceleration via the Telum processor for low-latency inference on mainframe. I don't have hands-on z/OS experience but I'd be ramping up via z/OS Connect, USS (Unix System Services), and IBM Z Trial workshops."*

**Q: How are z/OS builds different from Linux?**

> z/OS has its own compiler (IBM XL C/C++), its own file system structure (PDS data sets), its own job runner (JES). Builds often use IBM-specific tools but newer z/OS has Unix System Services with POSIX-y tools. Cross-compilation from Linux is possible with the right toolchain.

**Q: Are you willing to learn mainframe?**

> *"Absolutely. IBM has free **z/OS Trial** and **IBM Skills Network** courses. Mainframe is a unique skill that very few engineers have today — the learning curve is steep but the differentiation is huge. Happy to invest."*

### 7.5 Docker

**Q: Why Docker?**

> - Reproducible environments (eliminates "works on my machine")
> - Isolation between apps
> - Easy deployment — image runs anywhere with Docker
> - Layered filesystem → small incremental updates

**Q: Multi-stage Docker builds?**

> A `Dockerfile` with multiple `FROM` lines. Use a heavy image for building (compile, install build deps), then COPY only the final artifact into a slim runtime image. Reduces final image size dramatically.

```dockerfile
# Builder stage
FROM golang:1.22 AS builder
WORKDIR /src
COPY . .
RUN go build -o /out/app

# Final runtime stage
FROM gcr.io/distroless/static
COPY --from=builder /out/app /app
CMD ["/app"]
```

**Q: Docker vs Kubernetes?**

> Docker = how to package & run one container. Kubernetes = how to orchestrate many containers across many machines (scheduling, networking, scaling, healing).

### 7.6 Bash / shell

**Q: Common Bash patterns?**

```bash
# Loop over files
for f in *.pdf; do echo "$f"; done

# Conditionals
if [[ -f "$file" ]]; then ...; fi

# Pipes & filters
cat log.txt | grep ERROR | wc -l

# Arrays
arr=(one two three)
echo "${arr[0]}"

# Functions
greet() {
  echo "Hello, $1"
}

# Strict mode (recommended)
set -euo pipefail
```

---

<a id="8-python"></a>
## 8. Python Technical Foundations

You'll get coding-screen Python questions. Below: core fluency checks.

### 8.1 Data structures

**Q: List vs tuple vs set vs dict?**

| Structure | Mutable? | Ordered? | Use |
|---|---|---|---|
| list | ✅ | ✅ | ordered collection |
| tuple | ❌ | ✅ | immutable record |
| set | ✅ | ❌ | unique elements |
| dict | ✅ | ✅ (Py 3.7+) | key→value |

**Q: Time complexity?**

| Operation | list | dict | set |
|---|---|---|---|
| insert | O(1) end / O(n) middle | O(1) | O(1) |
| lookup | O(n) | O(1) | O(1) |
| delete | O(n) | O(1) | O(1) |
| iterate | O(n) | O(n) | O(n) |

### 8.2 Idioms

```python
# Comprehensions
squares = [x*x for x in range(10)]
unique = {x for x in items}
mapping = {k: v for k, v in pairs}

# enumerate
for i, item in enumerate(items): ...

# zip
for a, b in zip(list1, list2): ...

# unpacking
first, *rest = [1, 2, 3, 4]    # first=1, rest=[2,3,4]
a, b = b, a                     # swap

# dict.get with default
val = d.get("key", "default")

# defaultdict
from collections import defaultdict
g = defaultdict(list)
g["k"].append(1)
```

### 8.3 Generators & iterators

```python
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Use:
import itertools
first_10 = list(itertools.islice(fib(), 10))
```

**Why generators?** Lazy — produce values on demand, low memory.

### 8.4 Decorators

```python
def timed(func):
    def wrapper(*args, **kwargs):
        import time
        t = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time()-t:.2f}s")
        return result
    return wrapper

@timed
def slow():
    time.sleep(1)
```

### 8.5 Context managers

```python
# with-statement
with open("file.txt") as f:
    data = f.read()

# Custom
from contextlib import contextmanager

@contextmanager
def db_session():
    s = Session()
    try:
        yield s
        s.commit()
    except:
        s.rollback()
        raise
    finally:
        s.close()
```

### 8.6 async / await

```python
import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as r:
            return await r.text()

async def main():
    results = await asyncio.gather(*[fetch(u) for u in urls])

asyncio.run(main())
```

**Why async?** I/O-bound concurrency without threads. Doesn't help CPU-bound work (use multiprocessing).

### 8.7 Likely coding-screen problems

These show up constantly in entry/mid-level screens:

1. **Two Sum** — return indices of two numbers that sum to target. Hash map. O(n).
2. **Reverse a string / linked list**.
3. **Valid parentheses** — stack.
4. **Group anagrams** — sort each word as key.
5. **Top K frequent elements** — Counter + heap.
6. **Find longest substring without repeating chars** — sliding window.
7. **Merge intervals** — sort + sweep.
8. **Implement LRU cache** — `OrderedDict` or doubly linked list + dict.
9. **Word count from text** — split + Counter.
10. **Binary search variant** — search rotated array.

**Practice plan:** 5-10 LeetCode Easy + 5 Medium tagged Array / String / HashMap before the technical round.

---

<a id="9-system-design"></a>
## 9. System Design & Distributed Systems

You probably won't get a full system-design round at this level, but expect lite questions:

### 9.1 Likely questions

**Q: Design a URL shortener.**

> Hash the URL → short key (or counter + base62). Store key→URL in DB. Serve `/short_key` with 301 redirect. Cache hot URLs in Redis.

**Q: Design a rate limiter.**

> Token bucket: each user has a bucket that refills at rate R. Each request consumes a token. If empty → 429. Implement with Redis INCR + TTL, or Redis sorted set for sliding window.

**Q: Design Twitter timeline.**

> - Read-heavy → fan-out on write (push to followers' inboxes)
> - Or hybrid: fan-out for normal users, fan-in (pull) for celebrities

**Q: Design a chat service.**

> - WebSockets for real-time
> - Kafka for fan-out and durability
> - DB for history; cache for online status

**Q: Design the RAG project for 1M users.**

> Covered in Section 6.3 question 49.

### 9.2 CAP theorem

> In a distributed system, you can pick **2 of 3:** Consistency, Availability, Partition tolerance. Since networks fail (P is mandatory), real systems trade off C vs A.

### 9.3 Latency numbers everyone should know

```
L1 cache:               0.5 ns
Branch mispredict:      5 ns
L2 cache:               7 ns
Mutex lock/unlock:      25 ns
Main memory:            100 ns
Compress 1KB w/ Zippy:  3,000 ns
Send 1KB over 1Gbps:    10,000 ns
SSD read 4K random:     150,000 ns
Round-trip in DC:       500,000 ns
HDD seek:               10 ms
Pkt CA→Netherlands:     150 ms
```

---

<a id="10-behavioral"></a>
## 10. Behavioral & HR Questions

Use the **STAR** framework: **S**ituation, **T**ask, **A**ction, **R**esult. Keep stories 60-90 sec.

### 10.1 Most common questions + answer frames

**Q: Why IBM?**

> *"Three reasons. First, IBM operates at a scale and across industries — banking, healthcare, government — that few other companies match, and infrastructure decisions there have real impact. Second, IBM is investing heavily in enterprise AI through watsonx and AI on Z mainframe — this AI Engineer role sits exactly at that frontier. Third, IBM Research has a strong track record of fundamental contributions to AI; I want to be in an environment where deep engineering is valued."*

**Q: Why this specific role?**

> *"My current strengths are Python backend and real-time data infrastructure. This role takes that infrastructure mindset and applies it to AI/ML build systems — which is where I want to grow. I also see it as a stretch: the C++ and z/OS components are unfamiliar, and I'd be learning daily, which is the kind of growth I want."*

**Q: Tell me about a challenging technical problem.**

> *(Use the Spizen scoring engine story or the RAG project Ollama→Groq switch.)*
> *"At Spizen, we needed to score trade events in real-time — under 5ms per event — across multiple quality metrics. My first approach used Python with synchronous DB lookups; latency was 80ms p99. I refactored to load lookup tables into Flink state, parallelized scoring across rule modules, and dropped p99 to 3ms. Lesson: in streaming systems, optimize state locality."*

**Q: Tell me about a time you failed.**

> *(Be specific and own it. Don't fake humility.)*
> *"When I built the initial dedup logic at Spizen, I used a timestamp tiebreaker that was sometimes off by milliseconds due to clock skew between producer machines. We lost 1% of legitimate events for two days before I caught it. Fix: use a stable content hash and an explicit producer-event-id. Lesson: never trust wall-clock time in distributed systems."*

**Q: Tell me about a disagreement with a colleague.**

> *(Conflict, not drama. Show maturity.)*
> *"My senior wanted to use Postgres for the trade analytics layer; I argued for ClickHouse based on access patterns. We benchmarked both on 1M synthetic events for typical queries — ClickHouse was 10x faster on aggregations. We went with ClickHouse. Data over opinion wins."*

**Q: Where do you see yourself in 5 years?**

> *"Technical track. I'd like to grow into a Senior Engineer role with deeper expertise in AI infrastructure — specifically the intersection of distributed systems and ML inference. I'm not chasing management; I want to be the engineer teams call when something AI-related at the infra layer is broken."*

**Q: Strengths?**

> *"Strong fundamentals — I learn frameworks but invest in the underlying concepts. I'm comfortable in ambiguity — both my current and previous roles had me building things from a vague spec to production. And I'm honest about what I don't know, which I think speeds up learning."*

**Q: Weaknesses?**

> *(Real, not "I'm a perfectionist." Show self-awareness + active improvement.)*
> *"I tend to over-engineer at the start of a project — wanting to handle every edge case upfront. I'm consciously practicing 'build the simplest thing that works first, then iterate' — the RAG project I shipped was a small example of that discipline."*

**Q: Why are you leaving Spizen?**

> *(NEVER badmouth.)*
> *"Spizen's been a great learning ground for real-time data systems. I'm looking for a role where I can lean further into AI/ML infrastructure specifically — Spizen's product is fintech-focused, and the AI angle isn't core there. IBM's AI Engineer role is a stronger match for where I want to grow."*

**Q: What's your current CTC and expected CTC?**

> Have a number ready. **Don't say "expected open" or "as per company standards" — that signals weakness.**
> *"Current CTC is [X LPA]. For this role, given the scope and IBM's compensation bands for AI Engineer in Bangalore, I'm targeting [X+30% to X+50%] LPA. Open to discussion based on total comp including stock and bonus."*

**Q: Notice period?**

> *"30 days at Spizen. Negotiable down if a buyout is on the table."*

**Q: When can you start?**

> *"Immediately after notice — so within 30 days of an offer."*

**Q: Do you have other offers?**

> *(If yes, be honest but vague.)*
> *"I'm in late stages with one other company. Decision likely within 2-3 weeks. IBM is my top preference, which is why I moved fast on this referral."*

**Q: Any questions for me?**

> ALWAYS ask 2-3. Shows engagement.
> 1. *"What's the most exciting AI/ML infra problem the team has tackled in the last year?"*
> 2. *"How does this team interact with watsonx and the broader IBM AI org?"*
> 3. *"What does the first 30/60/90 days look like for someone in this role?"*
> 4. *"What's the biggest skill gap on the team you'd want this hire to fill?"*

---

<a id="11-ibm"></a>
## 11. IBM-Specific Knowledge

Showing IBM awareness is a force multiplier. 30 minutes of reading = much better impression.

### 11.1 IBM AI portfolio (watsonx)

| Component | What it is |
|---|---|
| **watsonx.ai** | Generative AI studio — build, tune, deploy foundation models. Hosts IBM Granite + select open models. |
| **watsonx.data** | Open data lakehouse — Presto + Iceberg, integrates with watsonx.ai for AI-ready data. |
| **watsonx.governance** | AI governance — monitor, document, audit models for compliance (GDPR, EU AI Act). |

### 11.2 IBM Granite

- IBM's family of open-source foundation models (Apache 2.0).
- Models tuned for enterprise: code, language, time-series, geospatial.
- Available on HuggingFace, watsonx.ai, IBM Cloud.
- Latest: Granite 3.x (2024-25) — competitive with Llama-3.x on enterprise tasks.

### 11.3 IBM Z (mainframe)

- The product line you'd be supporting in this role.
- z/OS is the OS. z/Linux exists for running Linux on mainframe.
- **Telum** chip (current gen) has on-chip AI accelerator → low-latency model inference inside the transaction path. Big deal for fraud detection in banking.
- z/OS Connect bridges mainframe to REST APIs.

### 11.4 IBM Cloud

- Competitor to AWS / Azure / GCP — strong in enterprise, hybrid cloud, regulated workloads.
- **Red Hat OpenShift** is IBM's Kubernetes-on-anything platform (since IBM bought Red Hat in 2019).
- Cloud Paks = curated software bundles on OpenShift.

### 11.5 IBM-specific terms to know

- **Big Blue** — IBM nickname
- **IBMer** — IBM employee
- **DOORS, ClearCase** — legacy IBM tools (less common now)
- **Db2** — IBM's relational DB
- **MQ** — IBM's messaging system (like Kafka but older / enterprise)
- **WebSphere** — Java app server
- **Cognos** — BI / reporting
- **Watson** (older brand) — AI service line that's now mostly subsumed into watsonx

### 11.6 Recent IBM AI news (read before interview)

Skim IBM Newsroom for "AI" and "watsonx" stories from the last 3 months. Mention one in your "any questions" segment:

> *"I read about IBM's recent Granite 3.x release and the on-chip AI inference on Telum-II. How is your team thinking about the AI workloads that will run on z/OS specifically?"*

---

<a id="12-prep-plan"></a>
## 12. Day-by-Day Prep Plan

Assumes 7-10 days before first call. Adjust as the timeline becomes clear.

### Day 1 (Today) — Foundation

- [ ] Fill IBM Accommodation Form
- [ ] Log into IBM Career Portal — check assessments assigned
- [ ] Re-read this document, scan all sections
- [ ] Send Sangeeth a brief thank-you note

### Day 2 — Assessment prep

- [ ] If coding assessment: 8-10 LeetCode Easy + 3-5 Medium (Array/String/HashMap)
- [ ] If video competency: write a 2-min "why IBM" and "tell me about a challenge" script; record yourself once for practice
- [ ] Set up clean recording environment (lighting, mic, plain background)

### Day 3 — Take assessments

- [ ] Knock out coding + video in one focused session in the morning
- [ ] Submit Accommodation Form first

### Day 4-5 — Deep GenAI prep

- [ ] Walk through Section 5 questions, answer aloud
- [ ] Re-read your `rag_pipeline.py` and `app.py` end-to-end — be able to recite design choices
- [ ] Run the project locally, ask it 5 different questions, observe behavior
- [ ] Read IBM watsonx product page (30 min)

### Day 6 — Python coding sharpener

- [ ] 5 more LeetCode Medium
- [ ] 3 SQL problems (joins, window functions)
- [ ] Review Python data structures, decorators, generators

### Day 7 — Build systems & C++ awareness

- [ ] Read CMake quickstart docs (30 min)
- [ ] Read pybind11 README (15 min)
- [ ] Skim a Jenkinsfile example (15 min)
- [ ] Watch one short z/OS overview video on YouTube

### Day 8 — Behavioral & mock

- [ ] Section 10 — write down your STAR stories for 5 common questions
- [ ] Mock interview with a friend OR record yourself answering 10 Qs

### Day 9+ — Standby

- [ ] Light review every 2 days
- [ ] Stay sharp but don't over-rehearse
- [ ] Stable sleep, light caffeine before the call

---

<a id="13-cheatsheet"></a>
## 13. Quick Reference Cheat Sheet

**My role:** Software Engineer, Python backend + GenAI
**Experience:** 2 years (Algonox Sep 2024 → Dec 2025; Spizen Dec 2025 → present)
**Education:** B.Tech CS, Tirumala Engineering College, 7.86/10, 2020-2024

**Top quantified achievements:**
- 50K+ trade events/day pipeline (Spizen)
- 95% dedup accuracy via Flink content-hash state (Spizen)
- 40% data extraction accuracy improvement (Algonox)
- 20% reduction in manual QA via KPI module (Algonox)

**Tech stack callouts (current job):** Python, Kafka, PyFlink, ClickHouse, Redis, Docker, Kubernetes

**Tech stack callouts (RAG project):** Python, LangChain, ChromaDB, HuggingFace, Groq, Flask

**GenAI skills:** RAG, Vector Search, Model Inferencing, Prompt Engineering, LangChain, HuggingFace, Groq, Ollama

**Certifications:** Microsoft Azure AI Fundamentals, AWS AI/ML

**Key numbers for RAG project:**
- Chunk size: 500 chars, overlap 50
- Embedding dim: 384 (MiniLM-L6-v2)
- Retrieval k: 4
- LLM: llama-3.1-8b-instant via Groq
- Port: 7000

**Salary anchor:** Know your current CTC + expected (30-50% jump for IBM).
**Notice period:** 30 days.
**Location flexibility:** Open to Bangalore office (current) and Hyderabad.

---

<a id="14-pitfalls"></a>
## 14. Common Pitfalls — What NOT to Do

❌ **Don't bluff on C++ or z/OS.** Interviewers will detect it. Acknowledge gaps, show willingness to learn.

❌ **Don't say "yes I know everything"** when asked about a tool you've only read about. Say *"I haven't used it in production but I understand X about it."*

❌ **Don't ramble.** Keep answers tight: 60-90 sec per behavioral, 2-3 min per technical deep dive. Pause and ask "Should I go deeper?"

❌ **Don't use buzzwords without backing.** If you say "I used RAG," be ready to explain chunking strategy, why your embedding model, retrieval k, prompt design.

❌ **Don't badmouth current employer.** Frame the move as growth-seeking, not escape.

❌ **Don't lowball your CTC expectation.** State a confident number.

❌ **Don't skip "any questions for me."** Always have 2-3 ready.

❌ **Don't memorize answers word-for-word.** Memorize structure + key talking points; deliver naturally.

❌ **Don't forget to send a thank-you email** after each round to the recruiter.

❌ **Don't share confidential code or proprietary algorithms** from current/previous job. General architecture is fine; copy-pasted snippets are not.

❌ **Don't speak ill of any tech.** *"I prefer X over Y because of reasons"* — not *"Y is garbage."*

❌ **Don't go silent if stuck.** Think out loud: *"Let me think about this. The constraint is X, so we need Y... I'm considering two approaches..."*

---

## Final reminders

- This is a **stretch role** given the C++ / z/OS asks. Your job is not to pretend you fit — your job is to be the most prepared, honest, curious version of yourself. If you don't get it, the interview practice is still huge value.
- **Your RAG project is your differentiator.** Recruiters see 100 resumes with "RAG, vector search" in skills. Very few candidates actually built and shipped one. Lead with the project in every conversation.
- **The referral matters.** Sangeeth's recommendation gives you a fairer shot than cold applicants. Earn it with prep.

Good luck. Go get it.

---

> *Last updated: May 2026*
