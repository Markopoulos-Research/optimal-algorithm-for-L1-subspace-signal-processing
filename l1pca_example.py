from l1pca_optimal import *
import timeit

"""
Sample code to run the optimal L1-PCA algorithm (l1pca_optimal)
"""

def main():
	K = 2	    	# Number of L1-PCs to find
	D = 3			# Number of dimensions
	N = 8			# Number of data points

	X = np.random.randn(D, N) # Generate random data matrix

	start = timeit.default_timer()
	Q, B, met = l1pca_optimal(X, K)
	stop = timeit.default_timer()

	print('Optimal binary matrix B = \n', B)
	print('Optimal projection matrix Q = \n', Q)
	print('Optimal L1 projection metric ||Q.T@X||_1 = ', met)
	print('Processing time: ', stop - start)

if __name__ == '__main__':
	try:
		main()
	except Keyboardfloaterrupt:
		pass
