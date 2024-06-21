import numpy as np 
from lab_3_task_1 import g 

x0 = int(input('x: '))
y0 = int(input('y: '))
v0 = int(input('v: '))
experiment = []
for t in range (0, 6, 1) :
    x = x0 + v0 * t
    y = y0 + v0 * t - ((g * t ** 2) / 2)
    experiment.append([t, x, y])

end = np.array(experiment)
print(end) 
