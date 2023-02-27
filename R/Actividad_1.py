
import math 
import numpy as np

roun = 4

def T(x,y,z):
    return [
        [ x, 0, 0],
        [ 0, y, 0],
        [ 0, 0, z]]

def Tp(px,py,pz):
    return np.array( [
        [ 1, 0, 0, px],
        [ 0, 1, 0, py],
        [ 0, 0, 1, pz],
        [ 0, 0, 0, 1]])

def V(x,y,z):
    return np.array([[x,y,z,1]]).transpose()

def Rx(alfa):
    alfa = math.radians(alfa)
    return np.array( [
        [ 1, 0, 0, 0],
        [ 0, round(math.cos(alfa),roun), round(-math.sin(alfa),roun), 0],
        [ 0, round(math.sin(alfa),roun), round(math.cos(alfa),roun), 0],
        [0, 0, 0, 1]])

def Ry(alfa):
    alfa = math.radians(alfa)
    return np.array([
        [ round(math.cos(alfa),roun), 0, round(math.sin(alfa),roun), 0],
        [ 0, 1, 0, 0],
        [ round(-math.sin(alfa),roun), 0, round(math.cos(alfa),roun),0],
        [0, 0, 0, 1]])

def Rz(alfa):
    alfa = math.radians(alfa)
    return np.array( [
        [round(math.cos(alfa),roun), round(-math.sin(alfa),roun), 0, 0],
        [  round(math.sin(alfa),roun), round(math.cos(alfa),roun), 0, 0],
        [ 0,0, 1, 0],
        [0, 0, 0, 1]])


def ejer_1():
    
    giro = np.dot(Ry(90),Rx(90))
    v = V(-3,10,10)
    #print("Ry ", end='')
    #print(Ry(90), end="")
    #print(Rx(90), end="")
    print(f"1. Rx(90°) * Ry(90°) * V({v.transpose()}) =")
    print(np.dot(giro,v))

def ejer_2():
    giro_1 = np.dot(Rz(45),Rx(60))
    giro_2 = np.dot(giro_1,Ry(90))
    print(f"2. ")

    print(giro_2)

def ejer_3():
    gg = np.dot( V(2,3,4).transpose(),Rz(90))
    #print( P(2,3,4).transpose())
    #print(Rz(90))
    print("P(uvw) = inv(R) * P(xyz)")
    inv = Rz(90)*-1

    print("inv"+inv)
    print(gg)

def ejer_5():
    r = V(4,4,11)
    print(r)
    inv = Tp(3,-1,2)*-1
    #p = np.invert(Tp(3,-1,2))
   
    print(inv)
    #resul = r+p
    #print(resul)
    resul = np.multiply(r,inv)
    print(resul)
    pass

def ejer_6():
    x = Tp(4, -2, 6)
    gg = np.dot(x,Rx(90)) 
    gg = np.dot(gg,V(-3, 4, 11))
    print(gg)

def ejer_7():
    giros = np.dot(Ry(-90),Rz(90))
    gg = np.dot(giros,V(1, 1, 5))

    hh =  np.dot(Ry(-90),V(1, 1, 5))
    hh = hh.transpose()
    hh = np.dot(hh,Rz(90))
    print(gg)

ejer_1()
print()
ejer_2()