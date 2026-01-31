# AI Engineering Questions

## 1. Easy

**What is the difference between an ML engineer and an AI engineer in practice?**

ML Engineer is more focused on building ML models, data cleaning, training, monitoring the performance.

AI Engineer is more focused on building application based on ai models. Productionizing it for users.

---

## 2. Easy–Medium

**What are embeddings, and why are they central to modern AI systems (LLMs, search, recommendations)?**

Embeddings are numerical representations of information, usually called as vectors stored in vector database in 
such a way that these embedding has semantic meaning to it.

in AI systems LLMs, search can't understand text directly but numbers, so the embeddings are the essential part to 
make the llms understand what users are looking for.

---

## 3. Medium

**Explain the difference between inference latency and throughput. Why do they often trade off in production systems?**



---

## 4. Medium–Hard

**You are deploying an LLM-powered application. What techniques would you use to reduce cost and latency without significantly hurting quality?**



---

## 5. Hard

**Design an end-to-end architecture for a production AI system that uses an LLM with retrieval (RAG). How do you handle data ingestion, indexing, inference, monitoring, and model updates?**

# ANSWERS

Below are **clear, production-grade expected answers** for the AI engineer questions. These are the depth and framing interviewers typically expect.

---

## 1. Difference between an ML engineer and an AI engineer

An **ML engineer** primarily focuses on training, evaluating, and deploying traditional machine learning models (e.g., classifiers, regressors, recommenders).

An **AI engineer** owns **end-to-end intelligent systems**, often centered around foundation models (LLMs, vision models), and is responsible for:

* Model integration (APIs, SDKs, orchestration)
* Prompting, RAG, tool use
* Inference optimization (latency, cost)
* System reliability, monitoring, and safety

In short: ML engineers optimize models; AI engineers optimize **systems built around models**.

---

## 2. What are embeddings and why are they important?

Embeddings are **dense vector representations** of data (text, images, audio) that capture semantic meaning.

They are central because they:

* Enable semantic similarity search
* Power retrieval-augmented generation (RAG)
* Support clustering, recommendation, and deduplication
* Provide a common representation space across modalities

Modern AI systems rely on embeddings to move from keyword matching to **meaning-based reasoning**.

---

## 3. Inference latency vs throughput

* **Latency:** Time to generate a single response.
* **Throughput:** Number of requests processed per unit time.

They trade off because:

* Batching increases throughput but adds waiting time, increasing latency.
* Parallelism improves throughput but competes for compute resources.
* Larger models improve quality but slow inference.

Production systems must balance user experience (latency) with infrastructure efficiency (throughput).

---

## 4. Reducing cost and latency in LLM systems

Key techniques:

* **Prompt optimization:** Shorter prompts, structured outputs
* **Caching:** Prompt-response and embedding cache
* **Batching:** Group inference requests
* **Model selection:** Smaller or distilled models for simpler tasks
* **Quantization:** INT8 / FP16 inference
* **RAG:** Retrieve relevant context instead of passing long prompts
* **Asynchronous workflows:** Stream results or defer non-critical steps

The goal is to spend compute **only where it adds value**.

---

## 5. End-to-end RAG system design

**Architecture overview:**

1. **Data ingestion**

   * Collect documents from sources (DBs, APIs, files)
   * Clean, chunk, and version data

2. **Indexing**

   * Generate embeddings
   * Store in a vector database
   * Periodically refresh or incrementally update

3. **Inference**

   * User query → embedding
   * Retrieve top-k relevant chunks
   * Construct prompt with retrieved context
   * Call LLM for generation

4. **Monitoring**

   * Track latency, cost, retrieval quality
   * Log prompts, responses, and failures
   * Detect drift and hallucinations

5. **Model & data updates**

   * Re-embed when data changes
   * A/B test prompt and model versions
   * Roll back safely on regressions

**Key failure modes**

* Stale or low-quality retrieval
* Prompt injection
* Latency spikes
* Silent quality degradation

A strong AI engineer designs for **observability, scalability, and safety from day one**.

---

If you want, I can:

* Turn these into **system-design interview drills**
* Add **follow-up questions interviewers ask**
* Grade your answers line-by-line again
