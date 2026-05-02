# 📊 The Foundation of Counting

In probability theory, counting is formalized by analyzing an experiment and determining the number of unique outcomes that satisfy a given event.

---

## 🔢 The Step Rule of Counting (Product Rule)

This rule applies when an experiment can be broken down into a sequence of independent steps.

### 📌 Formula

If an experiment has two steps where:

- Step 1 has **m** possible outcomes  
- Step 2 has **n** possible outcomes  
- The outcome of Step 2 is **independent** of Step 1  

Then:

> **Total Outcomes = m × n**

---

## ✅ Examples

### 🎲 Example 1: Rolling Two Dice

- Step 1 (First die): 6 outcomes  
- Step 2 (Second die): 6 outcomes  

\[
\text{Total} = 6 \times 6 = 36
\]

---

### 🖼️ Example 2: Number of Possible 12-Pixel Images

- Each pixel can have approximately **17 million colors**  
- Based on 8-bit RGB channels:

\[
256 \times 256 \times 256 = 16,777,216 \approx 1.7 \times 10^7
\]
> **256 * 256 * 256 = 16,777,216 \approx 1.7* 10^7**

- For 12 pixels, we have 12 independent steps:

\[
(1.7 \times 10^7)^{12} \approx 5.8 \times 10^{77}
\]
> **(1.7 * 10^7)^12 \approx 5.8* 10^77**

👉 **Total unique images ≈ (5.8 * 10^77)**

---
## ➕ The Sum Rule of Counting

If:

- Outcomes come from set **A** OR set **B**
- The two sets do **not overlap** (i.e., they are *mutually exclusive*)

Then:

>**Total Outcomes = |A| + |B|**


---

### ✅ Example

#### 🧸 Counting Toys

Suppose:

- I have **2 balls** (Set A)  
- I have **3 plush toys** (Set B)  
- No item belongs to both sets  

Then:

**3+2=5**

👉 **Total = 5 toys**

---

## 🔁 Inclusion–Exclusion Principle

What if the sets **do overlap**?

To avoid double-counting, we use the **Inclusion–Exclusion Principle**.

### 📌 Idea

If some elements belong to both sets:

1. Add both sets  
2. Subtract the overlap  

**Total Outcomes = |A| + |B| - |A and B|**


---

### ✅ Example

#### 💻 6-Bit String Validity

Breakdown:

- **Event A**: Strings starting with `01`  
  - Remaining 4 bits → \(2^4 = 16\)

- **Event B**: Strings ending with `10`  
  - Remaining 4 bits → \(2^4 = 16\)

- **Overlap (A ∩ B)**:  
  Strings that start with `01` **and** end with `10`  
  - Remaining 2 bits → \(2^2 = 4\)

Apply the formula:

\[
16 + 16 - 4 = 28
\]

👉 **Total valid strings = 28**

---

## 🔀 Unique Orderings (Permutations)

Permutations are about arranging distinct items.

### 📌 Idea

If there are **n unique items**, then:

- First position → **n choices**  
- Second → **(n - 1)** choices  
- Third → **(n - 2)**  
- ...  

So:

\[
n! = n \times (n-1) \times (n-2) \times \dots \times 1
\]

---

### ✅ Example

#### 🔤 Ordering "ABCD"

Step-by-step:

- Step 1: 4 choices  
- Step 2: 3 choices  
- Step 3: 2 choices  
- Step 4: 1 choice  


**4 * 3 * 2 * 1 = 24**


👉 **Total unique orderings = 24**

---

## 🤔 Further Thought

What if some items are **repeated**?

Examples:

- `"BOBA"`
- `"MISSISSIPPI"`

In these cases, simple permutations will **overcount identical arrangements**.

To fix this, we divide by the factorial of repeated elements:


**n! / (k₁! · k₂! · … )**

---