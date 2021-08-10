import matplotlib.pyplot as plt
import numpy as np
from perlin_numpy import (
    generate_fractal_noise_2d, generate_fractal_noise_3d,
    generate_perlin_noise_2d, generate_perlin_noise_3d
)

# Parameters
map_size = 2048, 2048
seed = 0
ocatves = 5


def createMap():
    np.random.seed(seed)
    noise = generate_fractal_noise_2d((map_size[0], map_size[1]), (8, 8), ocatves)
    return noise    

def createExpMap():
    exp_noise = np.exp2(createMap()*10)
    exp_noise /= exp_noise.max()
    return exp_noise
    
def plotFinalMap(noise_map):
    plt.figure()
    plt.imshow(noise_map, cmap='gray', interpolation='lanczos')
    plt.colorbar()
    plt.show()


noise_map =  createExpMap()
plotFinalMap(noise_map)