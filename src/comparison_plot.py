import matplotlib.pyplot as plt

# Simulated convergence times (example values)
algorithms = ['Deterministic PR', 'Randomized PR']
convergence_times = [2.4, 1.6]  # In seconds

plt.figure(figsize=(6,4))
plt.bar(algorithms, convergence_times, color=['skyblue', 'lightgreen'])
plt.title('PageRank Convergence Time Comparison')
plt.ylabel('Time (seconds)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the plot
plt.savefig('results/efficiency_comparison.png')
plt.show()
