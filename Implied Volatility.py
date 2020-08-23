# Question 1
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import scipy.optimize as sc

# The stock data given by the question is defined below

price = 100
Time = 1/12
Strike = [90, 95, 97.5, 100, 105, 110]
put = [1.3675, 1.7984, 2, 2.3828, 5.7711, 10.2249]
r=0.05
y=0

M = np.arange(-0.5,0.5,0.001)     #This is the moneyness array, which ranges from -0.5 to 0.5 by construction

def volatility (S,T,K,P,M):      #This function describes volatility based on Moneyness
  sigma = (norm.ppf((P+S*math.exp(-y*T)*(0.5+M))/(K*math.exp(-r*T)))+norm.ppf(0.5-M))/(math.sqrt(T))
  return sigma

k90 = plt.plot (M, volatility(price, Time, Strike[0], put[0], M), label='k90')
k95 = plt.plot (M, volatility(price, Time, Strike[1], put[1], M), label='k95')
k100 = plt.plot (M, volatility(price, Time, Strike[3], put[3], M), label='k100')
k105 = plt.plot (M, volatility(price, Time, Strike[4], put[4], M), label='k105')
k110 = plt.plot (M, volatility(price, Time, Strike[5], put[5], M), label='k110')
plt.xlabel('Moneyness')
plt.ylabel('Implied Volatility')
plt.legend()
plt.title('Implied Volatility Smile Plot')
plt.show()
