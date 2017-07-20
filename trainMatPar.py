import scipy.io as sio
import numpy as np
mat = sio.loadmat('trainCharBound.mat')
mat1 = mat['trainCharBound']['ImgName']
column,rows = mat1.shape
print rows
for i in range(rows):
    
    x = mat['trainCharBound']['ImgName'][0][i]
    x = np.array_str(x)
    x = x[1:-1]
    n,a = x.split('/')
    a,b = a.split('.')
    a = a + ".gt.txt"
    file = open(a, "w+")
    y = mat['trainCharBound']['chars'][0][i]
    print a, y
    print type(y)
    #file.write(y)
    file.close()

