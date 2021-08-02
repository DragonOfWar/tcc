import matplotlib.pyplot as plt

xAxis = [1,10,20,30,40,50,60,70,80,90]
yAxis = [86.46,88.06,88.48,88.53,88.71,88.92,89.05,89.10,89.12,89.15]

yAxisReal = [62.71,59.77,58.69,57.84,57.10,55.92,55.57,57.18,61.07,64.5]

yAxis2 = [0,0,0,0,0,0,0,0,0,0,0]

plt.plot(xAxis,yAxis, label='Base sintética')
plt.plot(xAxis,yAxisReal, label='Base real')
# plt.title('title name')
plt.legend()
plt.ylim(bottom=0, top=100)
plt.ylabel('Acurácia')
plt.xlabel('% de dados rotulados')
plt.show()