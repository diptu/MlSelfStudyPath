# Combinatorics & Permutations Reference

## 1. Distinct 6-Digit Passcodes
### Problem Statement
**Question:** How many unique 6-digit passcodes are possible if a phone password uses each of **six distinct numbers**?

#### Identifying the Constraints
* **Total Digits in Passcode:** 6
* **Available Digits (example):** 6 ({2, 3, 4, 5, 6, 8})
* **Rule:** Each digit is distinct, meaning each of the six identified numbers is used exactly once.

#### The Formula
Since we are arranging n distinct objects in a specific order, we use the formula for **permutations** of n objects:

P(n) = n!
P(6) = 6!

### Final Answer
There are **6! = 720** unique 6-digit passcodes possible under these conditions.

---

## 2. Strings & Permutations (With Repetition)

### Key Concept
When arranging items in a set where some elements are identical, we use the following formula:

Total Arrangements = n! / (n1! * n2! * n3! ...)

**Where:**
* **n** = total number of items
* **n1, n2, ...** = frequencies of each repeated item

### Example 1: BOBA
1. **Count letters:** Total (n) = 4; **B** appears 2 times.
2. **Apply formula:**
   4! / 2! = 24 / 2 = 12
   **12** distinct arrangements

### Example 2: MISSISSIPPI
1. **Count letters:** Total (n) = 11.
   * M = 1
   * I = 4
   * S = 4
   * P = 2
2. **Apply formula:**
   11! / (4! * 4! * 2!) = 39,916,800 / (24 * 24 * 2) = 34,650
   **34,650** distinct arrangements

---

## 3. 6-Digit Passcodes (With One Repetition)

### Problem
How many unique 6-digit passcodes are possible if a phone password uses exactly five distinct digits?

**Analysis:**
* Total positions = 6
* Only 5 distinct digits are used
* This implies **one digit is repeated exactly once** (appearing twice total), while the other four digits appear once.

### Calculation
We are arranging 6 digits where one set of two is identical:

Arrangements for a specific set = 6! / 2!

**Total for a fixed set of 5 digits (where 1 is designated to repeat):**
Total = 5 * (6! / 2!) = 5 * 360 = 1,800

# 📘 Combinations (Choosing People)

🔹 Problem

There are n=20 people.
How many ways can we choose k=5 people to get cake?

Total = 20! / (5!* 15!)=15,504

# The Divider Method
The Divider Method (also known as Stars and Bars) is a technique used to solve combinatorics problems where you need to distribute items into distinct groups.

The number of ways to distribute n indistinct objects into r buckets is equivalent to the number of ways to permute n + r - 1 objects such that:
n are indistinct objects (the "items").

r - 1 are indistinct dividers (the "walls" separating the buckets).

The Formula
The total number of unique distributions is calculated as:

Total = (n + r - 1)! / (n! * (r - 1)!)

This can also be expressed as a combination:
C(n + r - 1, n) or C(n + r - 1, r - 1)

Problem Statement
Question: How many unique hands of 5 cards are there in a 52-card deck?

=52C5
= 52!/(5!-(52-5!))

### 📌 Problem

You have 8 identical candies.How many ways can you distribute them among 3 children if each child can receive zero or more candies?

Candies = identical items → n = 8
Children = groups → r = 3

Total = (n + r - 1)! / (n! × (r - 1)!)
= (8 + 3 - 1)! / (8! × 2!)
= 10! / (8! × 2!)
= (10 × 9) / (2 × 1)
= 45