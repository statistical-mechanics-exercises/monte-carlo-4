import numpy as np
import scipy.stats as st

def area(N) : 
  nin = 0
  for i in range(N) : 
    x = np.random.uniform(0,1)
    y = np.random.uniform(0,1)
    if x*x + y*y < 1 : nin = nin + 1
  est = nin / N
  var = (N/(N-1))*(nin/N - est*est)
  return est, np.sqrt( var / N )*st.norm.ppf( (0.95+1) / 2 )
  
print( area(1000) )
