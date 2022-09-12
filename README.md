## Optimal algorithm for L1-norm Principal Component Analysis (L1-PCA; L1PCA)

In this repo we implent the algorithm of [[1]](https://ieeexplore.ieee.org/document/6851920) for computing the L1-norm Principal-Component of a matrix. 
Formally, the provided script solves 

![equation](https://latex.codecogs.com/svg.image?\mathbf{Q}_{L1}&space;=&space;\underset{\mathbf{Q}&space;\in&space;\mathbb{R}^{D\times&space;K},&space;\mathbf{Q}^T\mathbf{Q}&space;=&space;\mathbf{I}_{K}&space;}{\rm&space;argmax}&space;||\mathbf{Q}^T&space;\mathbf{X}||_{1,1})

optimally for a data matrix X(DxN) of rank d with complexity ![equation](https://latex.codecogs.com/svg.image?\mathcal{O}(N^{DK-K&plus;1})).

---
* IEEEXplore article: https://ieeexplore.ieee.org/document/6851920
* Source code: https://github.com/RIT-MILOS-LAB/optimal-algorithm-for-L1-subspace-signal-processing
---
**Questions/issues**

Inquiries regarding the scripts provided below are cordially welcome. In case you spot a bug, please let me know. If you use some piece of code for your own work, please cite the article above.

---
**Citing**

If you use our algorithm, please cite [[1]](https://ieeexplore.ieee.org/document/6851920).

|[[1]](https://ieeexplore.ieee.org/document/6851920)|Markopoulos, P.P., Karystinos, G.N. and Pados, D.A., 2014. Optimal algorithms for $ L_ {1} $-subspace signal processing. IEEE Transactions on Signal Processing, 62(19), pp.5046-5058. doi: 10.1109/TSP.2014.2338077.|
|-----|--------|
