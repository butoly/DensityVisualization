'''
### Визуализация плотности с равномерной сеткой плотности (плотности точек одинаковы)

import numpy as np
import mayavi.mlab as mlab

x, y ,z = np.ogrid[-10:10:20j, -10:10:20j, -10:10:20j]
s = x + y + z
#index = [[[10,10,10]]]
#new_s = np.delete(s, index)
#s = np.sin(x*y*z)/(x*y*z)
#print(s)
mlab.pipeline.volume(mlab.pipeline.scalar_field(s), color = (0,1,1))
#mlab.contour3d(s)

mlab.show()
'''

'''
import mayavi.mlab as mlab
import numpy as np

x = [[[i for i in range(10)]]]
y = [[[i for i in range(10)]]]
z = [[[i for i in range(10)]]]

nodes = mlab.points3d(x,y,z)
nodes.glyph.scale_mode = 'scale_by_vector'

#this sets the vectors to be a 3x5000 vector showing some random scalars
nodes.mlab_source.dataset.point_data.vectors = np.tile( np.random.random((5000,)), (3,1))

nodes.mlab_source.dataset.point_data.scalars = np.random.random((5000,))
'''

'''

def test_contour3d():
    x, y, z = numpy.ogrid[-5:5:64j, -5:5:64j, -5:5:64j]

    scalars = x * x * 0.5 + y * y + z * z * 2.0

    obj = contour3d(scalars, contours=4, transparent=True)
    return obj

test_contour3d()

show()
'''

'''
# Plot the atoms and the bonds ################################################
import numpy as np
from mayavi import mlab
mlab.figure(1, bgcolor=(0, 0, 0), size=(350, 350))
mlab.clf()

# The position of the atoms
atoms_x = np.array([2.9, 2.9, 3.8]) * 40 / 5.5
atoms_y = np.array([3.0, 3.0, 3.0]) * 40 / 5.5
atoms_z = np.array([3.8, 2.9, 2.7]) * 40 / 5.5

O = mlab.points3d(atoms_x[1:-1], atoms_y[1:-1], atoms_z[1:-1],
                  scale_factor=3,
                  resolution=20,
                  color=(1, 0, 0),
                  scale_mode='none')

H1 = mlab.points3d(atoms_x[:1], atoms_y[:1], atoms_z[:1],
                   scale_factor=2,
                   resolution=20,
                   color=(1, 1, 1),
                   scale_mode='none')

H2 = mlab.points3d(atoms_x[-1:], atoms_y[-1:], atoms_z[-1:],
                   scale_factor=2,
                   resolution=20,
                   color=(1, 1, 1),
                   scale_mode='none')

# The bounds between the atoms, we use the scalar information to give
# color
mlab.plot3d(atoms_x, atoms_y, atoms_z, [1, 2, 1],
            tube_radius=0.4, colormap='Reds')

# Display the electron localization function ##################################

# Load the data, we need to remove the first 8 lines and the '\n'
str = ' '.join(file('h2o-elf.cube').readlines()[9:])
data = np.fromstring(str, sep=' ')
data.shape = (40, 40, 40)

source = mlab.pipeline.scalar_field(data)
min = data.min()
max = data.max()
vol = mlab.pipeline.volume(source, vmin=min + 0.65 * (max - min),
                                   vmax=min + 0.9 * (max - min))

mlab.view(132, 54, 45, [21, 20, 21.5])

mlab.show()
'''

import numpy as np
from mayavi import mlab
mlab.figure(1, bgcolor=(1, 1, 1), size=(350, 350)) # Фон размер окна
mlab.clf()# clear figure(можно оп номеру)

# The position of the atoms
atoms_x = np.array([5, 6, 3])# * 40 / 5.5
atoms_y = np.array([7, 4, 9])# * 40 / 5.5
atoms_z = np.array([5, 8, 9])# * 40 / 5.5

O = mlab.points3d(atoms_x[1:-1], atoms_y[1:-1], atoms_z[1:-1],
                  scale_factor=2,
                  resolution=20, # разрешаюащя способность
                  color=(1, 0, 0),
                  scale_mode='none')

H1 = mlab.points3d(atoms_x[:1], atoms_y[:1], atoms_z[:1],
                   scale_factor=2,
                   resolution=20,
                   color=(1, 1, 1),
                   scale_mode='none')

H2 = mlab.points3d(atoms_x[-1:], atoms_y[-1:], atoms_z[-1:],
                   scale_factor=2,
                   resolution=20,
                   color=(1, 1, 1),
                   scale_mode='none')


x, y ,z = np.ogrid[-10:10:20j, -10:10:20j, -10:10:20j]
s = x + y + z
mlab.pipeline.volume(mlab.pipeline.scalar_field(s), color = (0,1,1))



mlab.show()
