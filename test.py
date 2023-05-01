def hebbian_learning(samples):
   print("input,target,weight changes,weights")
   w1,w2,b=0,0,0
   print(w1,w2,b)
   for x1,x2,y in samples:
      w1=w1+x1*y
      w2=w2+x2*y
      b=b+y
      print("(",x1,",",x2,",",y,")",",(",x1,",",x2,",",y,")",w1,",",w2)
import numpy as np
x=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,-1]])
print("hebbian learning")
print("and with x binary input and binary output")
hebbian_learning(x)
# WAP in python to implement hebbian_learning rule on the following datasets
# WAP a program to implement a simple artificial neural network
