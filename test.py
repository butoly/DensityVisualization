import numpy as np
import mayavi.mlab as mlab

# Create some random data
N = 20
x, y, z = np.mgrid[-5:5:30j, -5:5:30j, -5:5:30j]
s = np.sin(x * y  * z)/(x * y * z)

# Plot and show in mayavi2
#pts = mlab.points3d(x, y, z)#, val, scale_factor=.5,transparent=True)
#mlab.pipeline.volume(x,y,z)
mlab.pipeline.volume(mlab.pipeline.scalar_field(s))
mlab.show()
