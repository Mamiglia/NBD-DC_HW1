# NBD-DC_HW1
Homework#1 for Networking for Big Data. Sapienza 2022/23


## Part 1
1. scripts for generating p-ER and r-regular random graphs, with param K = number of nodes
2. scripts for checking that the graphs are fully connected:

  - Irreducibilty (numpy?)
  - Laplacian (numpy?)
  - BFS
  
3. Compare complexity for all the previous functions, as a function of K, then plot
4. let $p_C$ be the probability that a given graph is connected, now by running Monte Carlo simulations:
  
  - find $p_C$ for p-ER graphs when K=100
  - plot $p_C$ for r-regular graphs with r=2 and r=8 for any $K \leq 100$
