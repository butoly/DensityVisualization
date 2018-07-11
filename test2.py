import numpy as np
import mayavi.mlab as mlab


x1, y1, z1 = np.ogrid[-10:10:20j, -10:10:20j, -10:10:20j]
s1 = np.cos(x1*y1*z1)

#x2, y2, z2 = np.ogrid[0:10:10j, 0:10:10j, 0:10:10j]
#s2 = np.sin(x2*y2*z2)

'''
s = np.array([[[  0,   1,   2],
        [ 10,  12,  13]],
       [[100, 101, 102],
        [110, 112, 113]]])
'''

mlab.contour3d(s1, opacity = 1)
#mlab.contour3d(s2)

mlab.show()
