```
Business Problem Definition
        ↓
Task Framing (classification | NER | sentiment | summarization)
        ↓
Data Collection
 (logs | APIs | databases | documents)
        ↓
Data Inspection & EDA
 (noise | imbalance | language style | domain shift)
        ↓
Data Cleaning & Normalization
 (unicode, casing, emojis, URLs, HTML, duplicates)
        ↓
Annotation / Labeling
 (manual | weak supervision | rules)
        ↓
Train / Validation / Test Split
 (stratified, time-aware if needed)
        ↓
Text Preprocessing
 ├─ Tokenization strategy
 │   ├─ Rule-based (spaCy)
 │   └─ Subword (BPE / WordPiece)
 ├─ Lemmatization (task-dependent)
 └─ Stopword handling (careful for sentiment)
        ↓
Feature Representation
 ├─ Classical (TF-IDF, n-grams)
 └─ Neural (embeddings / transformers)
        ↓
Model Selection
 ├─ Baseline model (logistic, SVM)
 └─ Advanced model (transformer, custom head)
        ↓
Training
 ├─ Loss function
 ├─ Optimization
 └─ Regularization
        ↓
Evaluation
 ├─ Metrics (F1, precision, recall, accuracy)
 ├─ Error analysis
 └─ Bias checks
        ↓
Iteration Loop
 ├─ Improve data
 ├─ Adjust preprocessing
 └─ Tune model
        ↓
Model Validation
 (robustness, edge cases, drift checks)
        ↓
Packaging & Versioning
 (model + tokenizer + config)
        ↓
Deployment
 (batch | real-time | streaming)
        ↓
Monitoring & Feedback
 (performance, drift, failures)
        ↓
Retraining / Model Updates
```