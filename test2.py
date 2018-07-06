import numpy as np
from scipy import stats
from mayavi import mlab


'''
mu, sigma = 0, 0.1 
x = 10*np.random.normal(mu, sigma, 5)
y = 10*np.random.normal(mu, sigma, 5)
z = 10*np.random.normal(mu, sigma, 5)
'''

x = np.array([1, 16, 7, 4, 8])
y = np.array([4, 3, 9, 1, 0])
z = np.array([7, 4, 3, 4, 6])

#xyz = np.load('data/pr772_full_reconst.npy')

xyz = np.vstack([x,y,z])
print(xyz)
kde = stats.gaussian_kde(xyz)
density = kde(xyz)

# Plot scatter with mayavi
figure = mlab.figure('DensityPlot')
pts = mlab.points3d(x, y, z, density, scale_mode='none', scale_factor=0.07)
mlab.axes()
mlab.show()
