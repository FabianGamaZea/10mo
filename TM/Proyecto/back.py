import numpy as np
#from multipledispatch import dispatch

#@dispatch(list)
def min(A:list):
    A = np.array(A)
    
    if np.ndim(A)>=2:
        A = np.array(A)
        gg = []

        for a in np.transpose(A):
            gg.append(a.min())
        return gg
    else:
        return np.array(A).min()





print(min([[2,8,4],[1,2,3]]))
