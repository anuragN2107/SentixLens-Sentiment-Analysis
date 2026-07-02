# 👁️ SentixLens: Deep Sentiment Intelligence Framework

SentixLens is an end-to-end Natural Language Processing (NLP) intelligence platform designed to perform granular, context-aware textual evaluation. Rather than assigning a singular, generic polarity metric to an entire document, SentixLens evaluates text multi-dimensionally—enabling structural deep semantic profiling down to specific product features, core business attributes, or granular service aspects.

---

## 🚀 Live Deployment
The application is automatically built, optimized, and continuously deployed to production:
👉 **[SentixLens Live Web Dashboard](https://huggingface.co/spaces/anuragN2107/sentixlens-dashboard)**

---

## 🚀 Core Capabilities & Architecture

The framework targets token streams across distinct operational layers:

### 1. Aspect-Based Sentiment Analysis (ABSA)
Powered by a fine-tuned **DeBERTa-v3 Architecture** (`yangheng/deberta-v3-base-absa-v1.1`), the system isolates individual sub-components within complex sentences to parse independent polarities.
* **The Paradigm:** Traditional sentiment tools grade *"The UI is gorgeous but the response latency is terrible"* as an ambiguous *Neutral*. SentixLens decouples this sentence:
  * Target Aspect: `UI` ──> **Positive**
  * Target Aspect: `latency` ──> **Negative**

### 2. High-Performance Text Normalization
The preprocessing lifecycle relies on native **SentencePiece Tokenization** (`spm.model`). By embedding sub-word segmentation directly into the deployment container, the framework resolves out-of-vocabulary (OOV) tracking and structural string noise without requiring brittle, rule-based text-stripping algorithms.

### 3. Streamlined UI Architecture
Built entirely over a lightweight **Streamlit UI**, the runtime uses resource caching wrappers (`@st.cache_resource`) to store model weights in system memory on initial execution. This limits cold-start download lags and maximizes multi-user execution speeds.

---

## 🛠️ Production Tech Stack

* **Presentation Layer:** Streamlit (v1.35+)
* **Transformer Engine:** Hugging Face `transformers` & `PyTorch`
* **Sub-Word Tokenization Engine:** `sentencepiece` & `protobuf`
* **Deep Learning Runtime Integration:** TensorFlow / `tf-keras`

---

## 💻 Local Workspace Configuration

To spin up this sentiment engine inside a local development environment, execute the following configuration pipeline:

1. **Clone the Version-Controlled Repository:**
   ```bash
   git clone [https://github.com/anuragN2107/SentixLens-Sentiment-Analysis.git](https://github.com/anuragN2107/SentixLens-Sentiment-Analysis.git)
   cd SentixLens-Sentiment-Analysis
