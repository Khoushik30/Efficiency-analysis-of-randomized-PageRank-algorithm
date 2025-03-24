# Efficiency Analysis of Randomized PageRank Algorithm

## 📌 Overview
This project compares the traditional deterministic PageRank algorithm with a randomized version that introduces:
- **Random Hops** – occasional jumps to random pages.
- **Random Weights** – assigning different weights to outgoing links.

The goal is to analyze whether these modifications improve the algorithm’s efficiency and performance.

## 🛠️ Technologies Used
- Python
- NetworkX
- Matplotlib
- NumPy

## 📊 Dataset
- Google Web Graph Dataset (Stanford SNAP)
- Also tested on synthetic graphs for controlled analysis

## 🚀 How to Run
1. Clone the repo:
  git clone https://github.com/khoushikraj/randomized-pagerank.git cd randomized-pagerank

3. Install required libraries:
4. Run the code:
- `deterministic_pagerank.py` for original algorithm
- `randomized_pagerank.py` for modified version
- `comparison_plot.py` to visualize results

## 📁 Project Structure
```
randomized-pagerank/  
├── src/                          # Python source files  
│   ├── deterministic_pagerank.py  
│   ├── randomized_pagerank.py  
│   └── comparison_plot.py  
├── results/                      # Output graphs and data  
│   └── efficiency_comparison.png  
├── report/                       # Final PDF report  
│   └── randomized.pdf  
├── requirements.txt              # Python dependencies  
└── README.md                     # Project documentation
```
## 👨‍💻 Author

**Khoushik Raj Rasumalla**  
MS in Computer Science  
Washington State University  
📫 Email: k.rasumalla@wsu.edu  
🌐 LinkedIn: [linkedin.com/in/khoushikraj](https://www.linkedin.com/in/khoushikraj)  
💻 GitHub: [github.com/khoushikraj](https://github.com/khoushikraj)
