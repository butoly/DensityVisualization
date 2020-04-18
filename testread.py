import numpy as np
import mayavi.mlab as mlab

#np.set_printoptions(threshold=np.nan)
s = np.load('data/pr772_fourier_space.npy')
print(s[60][60][60])
print(s[61][61][61])
print(s[62][62][62])
print(s[63][63][63])

mlab.show()
