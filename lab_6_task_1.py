import matplotlib.pyplot as plt

x = [1.1, 5.1, 5.1, 1.1, 1.1]
y = [1.5, 1.5, 5.5, 5.5, 1.5]

plt.plot(x, y, 'b-')

plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.xlim(0, 6)
plt.ylim(0, 6)

plt.axis('equal')

plt.savefig('fig_task_1.png')
