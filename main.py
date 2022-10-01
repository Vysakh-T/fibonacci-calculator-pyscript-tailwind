import numpy as np
import random
arr = np.array([22,58,57,87,34,5])
pyscript.write('output', f"{arr}")

def shuffle_array(*args):
    shuffled = sorted(arr, key=lambda k: random.random())
    pyscript.write('output', f"{shuffled}")