import numpy as np
#np.array(data,dtype=int,copy=False,ndmin=1)
"""
Array custom creations:
data=np.array([1,2,3,4,5])
print(data)
print(type(data))
<class<ndarray>>
[]-1d
[[]]-2d
[[[]]]-3d
data=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data)"""
data=np.array([1,2,3,4,5])
print(data)
print(type(data))
data=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data)

data=np.array([2,4,6,8],ndmin=3,dtype=float)
print(data)

data=np.array([2,4,6,8],ndmin=3,dtype=complex)
print(data)

data=np.array([2,4,6,8],ndmin=3,dtype=int)
print(data)

data=np.array([2,4,6,8],ndmin=3,dtype=bool)
print(data)

#data=np.array([2, ,4,6,8],ndmin=3,dtype=bool)
