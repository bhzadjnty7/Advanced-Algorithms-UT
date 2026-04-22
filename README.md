# Advanced-Algorithms-UT
Comprehensive theoretical solutions, mathematical proofs, and Python implementations for the Advanced Algorithms course (Spring 2025) at the University of Tehran. Covers Network Flows, Linear Programming, Approximation, and Randomized Algorithms.

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Algorithms](https://img.shields.io/badge/Algorithms-Advanced-orange.svg)
![Data Structures](https://img.shields.io/badge/Data_Structures-Optimized-F37626.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

# 📚 Advanced Algorithms - Course Assignments

An extensive collection of problem-solving reports, mathematical proofs, and Python implementations developed for the **Advanced Algorithms** course at the School of Electrical and Computer Engineering, **University of Tehran**. This repository demonstrates a deep understanding of complex computational paradigms, ranging from deterministic optimization techniques to theoretical computer science proofs, approximation bounds, and randomized approaches.

## 📌 Course Information
- **Course Name:** Advanced Algorithms
- **Instructor:** Dr. Hesham Faili
- **Semester:** Spring 2025 (Bahar 1404)
- **Student:** Behzad Jannati

## 📖 About the Repository

This repository serves as a complete archive of the assignments given throughout the semester. The primary objective of these assignments is to transition from basic algorithmic thinking to advanced problem-solving methodologies. It involves rigorous mathematical modeling, time and space complexity analysis (Big-O notation), and practical coding implementations. 

For every assignment, you will find a dedicated folder containing the original problem statement, a highly detailed PDF report featuring theoretical proofs and code screenshots, and the standalone Python scripts containing the actual code. The implementations strictly adhere to standard Python libraries and follow best coding practices.

## 📂 Repository Structure

The repository is structured into distinct directories (`AA_HW1` to `AA_HW7`), each representing a specific algorithmic paradigm.

```text
.
├── AA_HW1/                 # Divide & Conquer / Amortized Analysis
│   ├── problem_statement.pdf
│   ├── AA_HW1_Solution.pdf
│   └── source_codes/
├── AA_HW2/                 # Dynamic Programming & Greedy Algorithms
│   ├── problem_statement.pdf
│   ├── AA_HW2_Solution.pdf
│   └── source_codes/
├── AA_HW3/                 # Computational Complexity & NP-Completeness
│   ├── problem_statement.pdf
│   ├── AA_HW3_Solution.pdf
│   └── source_codes/
├── AA_HW4/                 # Network Flows and Cut Problems
├── AA_HW5/                 # Linear Programming and Optimization
├── AA_HW6/                 # Approximation Algorithms
└── AA_HW7/                 # Randomized Algorithms
```
## 📝 Assignments Overview
### AA_HW1: Divide & Conquer and Amortized Analysis
This section focuses on breaking down massive computational problems into manageable sub-problems. It includes the theoretical analysis of the Fast Fourier Transform (FFT) and its application in signal processing. Furthermore, it contains a Divide & Conquer approach for predicting friendships in large-scale social networks, spatial data querying using KD-Trees and Splay Trees for closest-pair problems, and the implementation of the Graham Scan algorithm for computing Convex Hulls. It also features a comprehensive amortized analysis of a custom Doubly Linked List-based data structure.

### AA_HW2: Dynamic Programming (DP) & Greedy Algorithms
The second module dives deep into optimization problems. The Dynamic Programming section showcases the identification of optimal substructures, tackling scenarios like maximizing the sum of non-adjacent elements and a highly constrained resource allocation problem. The Greedy Algorithms section demonstrates optimal local choices leading to global minimums or maximums, featuring proofs by contradiction for problems like optimal rope connection (using Min-Heaps), fair prize distribution among participants, and workload balancing across computational nodes.

### AA_HW3: Computational Complexity & NP-Completeness
Dedicated to theoretical computer science, this section focuses on the P vs. NP dilemma. It includes rigorous polynomial-time reduction proofs to demonstrate NP-Hardness and NP-Completeness. Key highlights include reducing the Partition problem to Rectangle Tiling, transforming Vertex Cover into a Cycle Removal problem, and proving the NP-Completeness of Heavy Hamiltonian Cycles. Additionally, it models real-world exam scheduling using Graph Coloring reductions and analyzes the complexity of light-based logic circuits through SAT3 mapping.

### AA_HW4: Network Flows and Cut Problems
This assignment explores the practical and theoretical applications of flow networks. It involves modeling complex real-world scenarios into directed graphs and utilizing standard algorithms (like Ford-Fulkerson and Edmonds-Karp) to find optimal solutions. Key problems include calculating edge and vertex disjoint paths for secure routing, bipartite matching for assigning students to optimal internship positions, isolating infected nodes in a cognitive network using minimum cut strategies, and optimizing constrained seating arrangements for researchers using maximum flow properties.

### AA_HW5: Linear Programming (LP) and Optimization
This module dives into mathematical optimization, specifically formulating problems as Linear Programs and understanding their geometric and algebraic properties. The homework covers the optimization of currency exchange rates without borrowing, defining feasible regions and extreme points graphically, and applying the Two-Phase Simplex Method to find initial feasible points. Furthermore, it beautifully bridges the gap between different algorithmic paradigms by mathematically proving the Max-Flow Min-Cut theorem using LP Duality concepts.

### AA_HW6: Approximation Algorithms
Addressing NP-Hard problems computationally requires efficient approximation strategies. This assignment explores various techniques to find near-optimal solutions within guaranteed mathematical bounds. It includes a greedy 
H
n
/
2

 and 
2
-approximation for the Shortest Superstring problem in DNA/text sequencing, a 
(
2
−
2
/
k
)
 approximation for the Multiway Cut problem, and a 
3
/
2
 approximation for Makespan Load Balancing in mountaineering scenarios. It also features LP-relaxation and Greedy methods for the Set Cover (broadcasting) and Maximum Coverage (antenna placement) problems.

### AA_HW7: Randomized Algorithms
The final section explores the immense power of introducing randomness into algorithmic logic to achieve better average-case time complexities. It covers the distinction between Las Vegas and Monte Carlo algorithms, featuring a randomized Divide & Conquer approach for the classic “Nuts and Bolts” matching problem. It further delves into probability calculations for expected population distributions, randomized binary search complexity, verifying matrix multiplication (
A
×
B=
C
) in 
O
(
n
2
)
 time using random vectors, and computing the expected edges to connect a random graph. Finally, it provides a mathematical resolution to the Optimal Stopping (Secretary Problem) for auction bidding.

## 🛠️ Key Features
Theoretical Depth: Every folder contains PDF reports with extensive mathematical proofs, recurrence relation solving (Master Theorem), and rigorous approximations.
Ready-to-Run Code: Python scripts for the algorithmic challenges are provided right next to the PDF reports.
Visual Documentation: The reports include visual traces of tables, network flow graphs, Simplex operations, and screenshots of the code running on test cases.
## 💻 Installation & Usage
To explore the solutions and run the Python scripts locally, follow these steps:

### 1. Clone the repository:
```text
git clone https://github.com/YourUsername/Advanced-Algorithms-UT.git
cd Advanced-Algorithms-UT
```
### 2. Navigate to a specific homework directory:

```text
cd AA_HW6
```
### 3. Run the Python implementations:

```text
python shortest_superstring.py
```
(Note: Ensure you have Python 3.x installed. Any external mathematical or graphing libraries are listed at the top of the respective scripts).

## 🤝 Contributing
While this is a personal academic repository, constructive feedback, alternative optimization ideas, or discussions regarding theoretical proofs are always welcome. Feel free to open an issue or submit a pull request if you spot any typographical errors in the mathematical formulas.

## 📄 License
This project is open-source and available under the MIT License.

## 📬 Contact
Developed by Behzad Jannati

University of Tehran - Computer Engineering Department

GitHub: [https://github.com/bhzadjnty7](https://github.com/bhzadjnty7)

Linkedin: [www.linkedin.com/in/behzadjannati](www.linkedin.com/in/behzadjannati)
