import numpy as np
import time

M = int(input('введите M: '))
N = int(input('введите N: '))

start_time = time.time()

for i in range(M + 1):
    print(f'out series (M): {i}')
    time.sleep(1)
    for j in range(N + 1):
        print(f'in series (N): {j}')
        time.sleep(1)

end_time = time.time()

total_time = end_time - start_time
print(f'Общее время работы: {total_time}')