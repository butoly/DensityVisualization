'''
import numpy as np
import mayavi.mlab as mlab

x, y, z = np.ogrid[-10:10:20j, -10:10:20j, -10:10:20j]
#s = np.sin(x*y*z)/(x*y*z)
s = x**2 + y**2 + z**2


#scalar = np.load("data/pr772_full_reconst.npy")
#print(s.shape) Возвращает размерности объекта
    
#mlab.pipeline.volume(mlab.pipeline.scalar_field(s), vmin = 0, vmax = 0.8)
mlab.contour3d(x, y, z, s)

mlab.show()
'''


import numpy as np
from scipy import stats
from mayavi import mlab

mu, sigma = 0, 0.1 
x = 10*np.random.normal(mu, sigma, 5000)
y = 10*np.random.normal(mu, sigma, 5000)    
z = 10*np.random.normal(mu, sigma, 5000)

xyz = np.vstack([x,y,z])
kde = stats.gaussian_kde(xyz)

# Evaluate kde on a grid
xmin, ymin, zmin = x.min(), y.min(), z.min()
xmax, ymax, zmax = x.max(), y.max(), z.max()
xi, yi, zi = np.mgrid[xmin:xmax:30j, ymin:ymax:30j, zmin:zmax:30j]
coords = np.vstack([item.ravel() for item in [xi, yi, zi]]) 
density = kde(coords).reshape(xi.shape)

# Plot scatter with mayavi
figure = mlab.figure('DensityPlot')

grid = mlab.pipeline.scalar_field(xi, yi, zi, density)
min = density.min()
max=density.max()
mlab.pipeline.volume(grid, vmin=min, vmax=min + .5*(max-min))

mlab.axes()
mlab.show()
