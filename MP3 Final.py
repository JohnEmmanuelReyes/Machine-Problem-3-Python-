import numpy as np

#Inputing (xi,yi) 
print("Array Input Example: \nInput example points of xi: 1 2 3 4 5 \nInput example points of yi: 2 3 4 5 6   \n(xi,yi) stored in matrix p") 
#All xi Input
x=list(map(int, input("Input points of X:   ").split()))
#All yi Input
y=list(map(int, input("Input points of Y:   ").split()))
lx=len(x);ly=len(y);

if lx==ly:
    p=np.column_stack((x,y))
    lp = len(p)
#considering the degree of the polynomial
    if lp < 11:
        i=lp
    else:
        i=10  
else:
   raise NameError('Unequal number of array') 

X = p[:, 0]; Y = p[:, 1]
for n in range(i):
#finds the best fit 
   pf = np.polyfit(X, Y, n)
   pv = np.polyval(pf, X)
   norm = np.linalg.norm(Y - pv)
   if n == 0:
       f = pf
       temp = norm
   if temp > norm:
       f = pf
print('The coefficients in polynomial curve fitting are: \n',f)
