# Machine Learning Questions

## 1. Easy: What is the difference between supervised and unsupervised learning? Give one example of each.

Machine Learning: It is a concept of AI where it can do predictions or actions based on patterns learnt on historical Data.

**Supervised ML**: Algorithms that need labelled data to train,  often called as target variable.
Example: To predict where the batsman will be scoring a century or not in the next match, 
model should need previous matches details and scores. scores are the target var.

**UnSupervised ML**: Algorithms that doesn't need labelled data instead it will learn patterns. 
Example: To perform customer's segmentation in amazon using their purchase history.

## 2. Easy–Medium: What problem does a train/validation/test split solve, and what can go wrong if you skip it?

train data is used to train the algorithm/model, validation data is used to validate the model and further train the model
test data is used to evaluate the model. 

If you skip the train test split the model will be trained butyou cannot evaluate the model or validate, 
You will never know whether the model is working accurately or not.

## 3. Medium: Explain the bias–variance tradeoff. How does it show up in underfitting vs overfitting?

When the data is biased the model tends to underfit, where as if variance then model overfits. In further cases the error rate is high.
you have find a way in between bias and variance so that model is prone to less error.
- if model underfits you need more data to be added to the model
- if model overfits you may need to tune the hyperparameters, feature engineering and so on...

## 4. Medium–Hard: How do regularization techniques like L1 and L2 affect a model’s parameters and feature selection?
Answer: IDK
## 5. Hard: You deploy an ML model and its performance degrades over time. What are the likely causes, how would you detect them, and what concrete steps would you take to fix the issue?

ML model degrades after deployment because there may be data drift/concept drift. Where the data/model assumptions are being violated.
- The drift happens because there may be such an event that might have changed behavior of features.
- To identify data drift you will compare the means of previous data and current data.
- To identify concept drift you may check distribution of data. If it is normal then no change, if there is change then concept drift is likely cause.(KS test, chisquare test)

Steps to resolve
- Retrain the model with latest data
- Add external features that might causing the drift.

---

# Expected answers
Below are **concise, interview-ready expected answers** for each question. These are the level and structure typically expected from a strong ML engineer.

---

## 1. Difference between supervised and unsupervised learning

**Supervised learning** uses labeled data `(X, y)` to learn a mapping from inputs to outputs.
It is used for **classification** and **regression**.

**Example:** Predicting whether a customer will churn (label: churn / no churn).

**Unsupervised learning** uses unlabeled data `(X)` and aims to discover hidden structure or patterns.

**Example:** Customer segmentation using clustering based on purchase behavior.

---

## 2. Purpose of train / validation / test split and risks of skipping it

* **Training set:** Used to learn model parameters.
* **Validation set:** Used for hyperparameter tuning and model selection.
* **Test set:** Used once to estimate final, unbiased generalization performance.

**If skipped:**

* The model may overfit without detection.
* Performance metrics become optimistically biased.
* Data leakage can occur, leading to false confidence in the model.

---

## 3. Bias–variance tradeoff and underfitting vs overfitting

* **Bias** is error from overly simplistic model assumptions.
* **Variance** is error from sensitivity to small changes in training data.

**Underfitting:**

* High bias, low variance
* Model fails to capture patterns
* Training and validation error are both high

**Overfitting:**

* Low bias, high variance
* Model memorizes training data
* Training error low, validation error high

The goal is to find a balance that minimizes total generalization error.

---

## 4. Effect of L1 and L2 regularization

* **L1 regularization (Lasso):**

  * Adds absolute weight penalty
  * Drives some coefficients exactly to zero
  * Performs implicit feature selection
  * Useful when many features are irrelevant

* **L2 regularization (Ridge):**

  * Adds squared weight penalty
  * Shrinks coefficients but rarely to zero
  * Improves numerical stability
  * Works well with correlated features

---

## 5. Model performance degradation after deployment

**Likely causes**

* **Data drift:** Input feature distributions change
* **Concept drift:** Relationship between inputs and labels changes
* Data quality issues, pipeline bugs, or feedback loops

**Detection**

* Monitor feature distributions (KS test, PSI)
* Track prediction confidence and output distributions
* Monitor performance metrics on recent labeled data

**Mitigation**

* Retrain with recent data
* Use sliding windows or online learning
* Add drift-robust features
* Implement continuous monitoring and retraining pipelines

---

If you want, I can also provide:

* **One-line interview answers**
* **Whiteboard-style explanations**
* **Follow-up questions interviewers usually ask next**
