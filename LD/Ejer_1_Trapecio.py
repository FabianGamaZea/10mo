import matplotlib.pyplot as plt

y = []
x = [0,1,2,3,4,5,6,7,8,9,10]
for i in range(len(x)):
	if i > 3 and i < 7:
		y.append(1)
	else:
		y.append(0)

plt.title("Trapecio")
plt.plot(x,y)
plt.ylabel("Eje X")
plt.xlabel("Eje Y")
plt.show()
