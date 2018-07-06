import numpy as np
import mayavi
from mayavi import mlab

s = np.load('data/pr772_fourier_space.npy')


src = mlab.pipeline.scalar_field(s)
mlab.pipeline.iso_surface(src, contours=[s.min()+0.1*s.ptp(), ], opacity=0.3)
mlab.pipeline.iso_surface(src, contours=[s.max()-0.1*s.ptp(), ],)

mlab.show()
