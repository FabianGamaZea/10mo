import numpy as np

#from multipledispatch import dispatch

#@dispatch(list)

def convertArray(A:str):
    A = eval(A)
    return A


def min(A:str):
    A = convertArray(A)
    A = np.array(A)
    
    if np.ndim(A)>=2:
        gg = []

        for a in np.transpose(A):
            gg.append(a.min())
        return gg
    else:
        return A.min()

def  mink(A:list,long:str):
    long = int(long)
    A = convertArray(A)
    A = np.array(A)
    
    if np.ndim(A)>=2:
        gg = []

        for a in A:
            gg.append( np.sort(a)[:long].tolist())
        return gg
    else:
        print(np.sort(A))
        return np.sort(A)[:long]




print(mink("[[1,2,3],[1,2,3]]","3"))




