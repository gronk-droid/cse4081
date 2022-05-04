<div class="titlePage">

# CSE4081 Analysis of Algorithms
### Final Exam
##### Grant Butler | gbutler2020@my.fit.edu
</div>

## Table of Contents {ignore=true}

[TOC]

<div class="pageBreak"></div>

# Loops, Counting, and Summations
There are two basic loop types: `for` and `while`.

###### 1. Dot Product For Loop
The syntax for _for_ loops (usually) describe how many times statements in its scope executes. An analysis skill is to be able to use summation notation to countthe number of times instructions executes in a for loop.</br>Here is an example from linear algebra:  Given two vectors

<div class="center">

$\vec{A} = \langle a_1, a_2,..., a_n \rangle$ and $\vec{B} = \langle b_1, b_2,..., a_n \rangle$
</div>

Their _inner_ (dot) product is:

<div class="center">

$\langle a | b \rangle = \sum_{k = n}^{k = 1} \left(a_k \cdot  b_k\right)$
</div>

Write this sum as a _**for**_ loop and state its _big-O_ time complexity.

The summation as c code:
```c
// given vectors a and b
float dot_product = 0.0;
for (int k = 1; i < n; i++) {
    dot_product += a[k] * b[k];
}
```
Since there is only one for loop, the time complexity of the dot product is `O(n)`, because it depends solely on `n`, or the size of the vectors.

###### 2. Matrix Multiplication Nested For Loops

_For_ loops can be nested, giving rise to a sequence of summations with one (perhaps) dependent on previous sums.

Given two _n_ x _n_ matrices A and B, the standard algorithm to compute their product, given as $C = A \times B$,
