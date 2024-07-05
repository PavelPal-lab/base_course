import random
import numpy as np 

flowers = ['конопля', 'марихуана', 'архидея']
colors = ['синий', 'белый', 'зеленый', 'желтый', 'красный']

flowers_colors = dict(zip(flowers, random.sample(colors, len(flowers))))
print(flowers_colors)