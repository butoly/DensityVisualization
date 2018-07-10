### Визуализация плотности с равномерной сеткой плотности (плотности точек одинаковы)

import numpy as np
import mayavi.mlab as mlab

x, y ,z = np.ogrid[-10:10:20j, -10:10:20j, -10:10:20j]
s = x + y + z
index = [[[10,10,10]]]
new_s = np.delete(s, index)
#s = np.sin(x*y*z)/(x*y*z)
#print(s)
mlab.pipeline.volume(mlab.pipeline.scalar_field(new_s), color = (0,1,1))
#mlab.contour3d(s)

mlab.show()

