# Mastery Path: Core Machine Learning & Algorithmic Rigor

This repository contains a structured, engineering-first self-study curriculum designed to master foundational and advanced machine learning algorithms. The timeline transitions systematically from parametric optimization to learning theory, non-parametric systems, and reinforcement learning.

## 📅 Roadmap Schedule

### Module 1: Linear Models & Analytic Optimization
**Goal:** Master parametric regression and classification frameworks through iterative and exact mathematical optimization.
- **Topics:** Linear Regression, Ordinary Least Squares (OLS), Batch Gradient Descent, Stochastic Gradient Descent (SGD), Logistic Regression, Newton's Method, and Generalized Linear Models (GLMs).
- **Mathematical Focus:** First-order vector derivatives, Hessian matrices, and Exponential Families.
- **Core Outcome:** Ability to derive the exact analytical global minimum via the Normal Equations and implement highly scaled stochastic optimization loops.

### Module 2: Generative Models & Non-Parametric Frameworks
**Goal:** Shift from modeling boundaries ($P(y|x)$) to modeling data-generating distributions ($P(x|y)$).
- **Topics:** Gaussian Discriminant Analysis (GDA), Naive Bayes (Multinomial & Bernoulli), and Laplace Smoothing.
- **Mathematical Focus:** Multivariate Gaussians, Joint likelihood optimization, and Conditional Independence assumptions.
- **Core Outcome:** Constructing computationally efficient text and classification pipelines that handle high-dimensional conditional probabilities.

### Module 3: Convex Optimization & Kernel Methods
**Goal:** Formulate optimal separation boundaries and map non-linear features into infinite-dimensional spaces.
- **Topics:** Support Vector Machines (SVMs), Functional & Geometric Margins, Lagrange Duality, KKT Conditions, and Kernel Tricks (RBF, Polynomial).
- **Mathematical Focus:** Constrained convex optimization, dual optimization problems, and Mercer’s Theorem.
- **Core Outcome:** Building robust maximum-margin classifiers capable of handling non-linearly separable data spaces without explicit feature mapping.

### Module 4: Learning Theory, Bias/Variance & Model Selection
**Goal:** Establish formal mathematical guarantees for model generalizability and construct disciplined verification pipelines.
- **Topics:** Bias/Variance Trade-off, Union Bound, Hoeffding's Inequality, VC (Vapnik-Chervonenkis) Dimension, Empirical Risk Minimization (ERM), and Regularization ($L_1$/$L_2$).
- **Mathematical Focus:** Sample complexity bounds and structural risk minimization.
- **Core Outcome:** Quantifying empirical vs. generalization error to systematically choose model capacities and prevent overfitting.

### Module 5: Non-Parametric Trees & Non-Linear Parameter Deep Learning
**Goal:** Engineer highly flexible non-linear discriminators, moving from recursive partitioning to neural graph backpropagation.
- **Topics:** Decision Trees (ID3, C4.5, CART), Ensemble Methods (Bagging, Random Forests, Gradient Boosting Machines), Feedforward Neural Networks, and Backpropagation.
- **Mathematical Focus:** Information Gain (Entropy/Gini Index), Matrix Calculus, and the Chain Rule over computational graphs.
- **Core Outcome:** Implementing raw matrix-level backpropagation and designing high-performance gradient-boosted ensembles.

### Module 6: Unsupervised Learning & Latent Variable Models
**Goal:** Uncover structural geometry and identify hidden patterns within unlabeled datasets.
- **Topics:** K-Means Clustering, Principal Component Analysis (PCA), Expectation-Maximization (EM) Algorithm, and Mixture of Gaussians (GMM).
- **Mathematical Focus:** Eigenvalue decomposition, variance maximization, and Jensen's Inequality for optimizing lower bounds.
- **Core Outcome:** Developing dimensionality reduction pipelines and mathematically optimizing models with latent unobserved variables.

### Module 7: Sequential Decision Making & Reinforcement Learning
**Goal:** Train autonomous agents to maximize long-term cumulative rewards within dynamic environments.
- **Topics:** Markov Decision Processes (MDPs), Bellman Equations, Value Iteration, Policy Iteration, and Q-Learning.
- **Mathematical Focus:** Dynamic Programming and contraction mappings over value spaces.
- **Core Outcome:** Engineering control policies for reward-driven agents navigating discrete and continuous state-action graphs.

---

## 🔗 Reference Resources
- **Lecture Repository:** [Stanford Online - CS229 Playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU)
- **Official Course Materials:** [cs229.stanford.edu](https://cs229.stanford.edu/)