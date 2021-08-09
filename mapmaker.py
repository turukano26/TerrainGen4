import matplotlib.pyplot as plt
import numpy as np
from perlin_numpy import (
    generate_fractal_noise_2d, generate_fractal_noise_3d,
    generate_perlin_noise_2d, generate_perlin_noise_3d
)

def createMap():

    np.random.seed(0)
    noise = generate_fractal_noise_2d((8192, 8192), (8, 8), 5)
    plt.figure()
    plt.imshow(noise, cmap='gray', interpolation='lanczos')
    plt.colorbar()
    plt.show()

createMap()