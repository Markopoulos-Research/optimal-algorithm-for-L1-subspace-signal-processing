"""
Optimal L1-PCA Algorithm with time complexity O[N^(DK-K+1)]
Input: data matrix (X) and number of PCs to be found (K)
Output: optimal binary matrix (B), projection matrix (Q) and L1-projection metric ||Q.T@X||_L1
"""

from numpy.linalg import svd
import numpy as np
from utils import *
import itertools

def l1pca_optimal(X, K):
    D = X.shape[0]
    N = X.shape[1]
    U, S, V = svd(X.T, full_matrices=False)
    Q = U @ np.diag(S)
    B = compute_candidates(Q.T)
    P = B.shape[1]
    Z = list(itertools.combinations(range(P), K))
    metopt = 0
    for i in range(len(Z)):
        met = np.linalg.norm(X @ B[:, Z[i]], 'nuc')
        if met > metopt:
            metopt = met
            zopt = Z[i]
    Bopt = B[:,zopt]
    U, _, V = svd(X@Bopt, full_matrices=False)
    Qopt = U@V.T
    return Qopt, Bopt, metopt

