import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_errors(self):
        resamples = 100*[0]
        for j in range(100) :
           inc = 0
           for i in range(100) : 
               x = np.random.uniform(0,1) 
               y = np.random.uniform(0,1)
               if x*x + y*y < 1 : inc = inc + 1
           mean = inc / 100
           var = ( 100 / 99 )*(mean - mean*mean) 
           resamples[j] = np.sqrt( var /100 )*st.norm.ppf( (0.95 + 1) / 2 )
  
           est, bar = area(100) 
           self.assertTrue( bar>np.percentile(resamples,5) and bar<np.percentile(resamples,95), "Error bars are not within range for resampled errors" )
           
    def test_average(self) :
        mean, bar = np.pi/4, np.sqrt( (np.pi/4)*(1-(np.pi/4)) / 100 )*st.norm.ppf( (0.99 + 1) / 2 )
        for i in range(5) : 
            est, tbar = area(100)
            self.assertTrue( tbar>0, "the width of the error bar should not be negative" )
            self.assertTrue( np.abs(est - mean)<bar, "your function for calculating the area of the circle doesn't appear to be working" )
