import matplotlib.pyplot as plt
import numpy as np
from perlin_numpy import (
    generate_fractal_noise_2d, generate_fractal_noise_3d,
    generate_perlin_noise_2d, generate_perlin_noise_3d
)

maps_to_combine = []

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
    maps_to_combine.append(exp_noise)

def createPerlinMap():
    perlin_map = createMap()
    perlin_map = perlin_map-perlin_map.min()
    perlin_map /= perlin_map.max()
    maps_to_combine.append(perlin_map)
    
def combineMaps():
    combined_map = np.zeros((map_size[0], map_size[1]))

    for current_map in maps_to_combine:
        combined_map = np.add(combined_map, current_map)

    return combined_map/len(maps_to_combine)

        
def plotFinalMap(noise_map):
    plt.figure()
    plt.imshow(noise_map, cmap='gray', interpolation='lanczos')
    plt.colorbar()
    plt.show()


createExpMap()
createPerlinMap()

noise_map = combineMaps()
plotFinalMap(noise_map)