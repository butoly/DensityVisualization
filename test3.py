import numpy as np
import mayavi.mlab as mlab

#np.set_printoptions(threshold=np.nan)
#s = np.load('data/pr772_full_reconst.npy')
s=np.ones((5,5,5))
mlab.contour3d(s,contours = 5)

mlab.show()
