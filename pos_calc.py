import numpy as np
import sys
import unittest
from scipy.special import binom

class Test(unittest.TestCase):
	def __init__(self,first, second):
		self.first = first
		self.second = second

	def testEq(self):
		self.assertEqual(self.first,self.second)

binom_trial = lambda n,k,p: binom(n, k)*p**k*(1.-p)**(n-k)

n = int(sys.argv[1])
p = float(sys.argv[2])
k = np.array([x for x in range(0,n+1)])

mean = sum(k*binom_trial(n,k,p))
mean = round(mean, 2)

check = Test(mean, n*p)
check.testEq()

print(mean)
