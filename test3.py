import numpy as np
import mayavi.mlab as mlab

#np.set_printoptions(threshold=np.nan)
s = np.load('data/pr772_full_reconst.npy')
mlab.contour3d(s,transparent = True, contours = 7)

mlab.show()
