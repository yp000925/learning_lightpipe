from LightPipes import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


GridSize = 10*mm
GridDimension = 128
lambda_ = 500*nm #lambda_ is used because lambda is a Python build-in function.

R=2.5*mm #Radius of the aperture
# xs=1*mm; ys=1*mm#shift of the aperture

Field = Begin(GridSize, lambda_, GridDimension)

Field1=CircAperture(R,Field)
I1=Intensity(0,Field1)

Field2=RectAperture(Field,1*mm,2.5*mm)
I2=Intensity(0,Field2)

Field3=SuperGaussAperture(Field,2.5*mm)
I3=Intensity(0,Field3)


fig=plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224,projection='3d')
ax1.imshow(I1,cmap='rainbow'); ax1.axis('off'); ax1.set_title('CircAperture')
ax2.imshow(I2,cmap='rainbow'); ax2.axis('off'); ax2.set_title('RectAperture')
ax3.imshow(I3,cmap='rainbow'); ax3.axis('off'); ax3.set_title('SuperGaussAperture')
x,y = Field3.mgrid_cartesian
ax4.plot_surface(x,y,I3,cmap='rainbow');  ax4.set_title('SuperGaussAperture 3d')
plt.show()