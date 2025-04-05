import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 35]
y2 = [5, 15, 20, 25, 30]

plt.plot(x, y1, label='Line 1', color='blue', marker='o')
plt.plot(x, y2, label='Line 2', color='green', marker='s')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multiple Lines on Same Plot')
plt.legend()
plt.grid(True)
plt.show()
