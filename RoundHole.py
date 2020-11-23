from LightPipes import *
import matplotlib.pyplot as plt

wavelength=625*nm
size=25.0*mm
N=1024

F=Begin(size,wavelength,N)
F=CircAperture(5*mm, 0, 0, F)
F=Forvard(300*cm,F)
I=Intensity(0,F)

plt.imshow(I,cmap='jet')
plt.show()

screen = CircScreen(F, 10*mm)