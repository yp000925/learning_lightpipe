import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.fftpack import fftn, ifftn, fftshift, ifftshift
from LightPipes import *

image = mpimg.imread('letterA_512.png') ### image size 512 x 512
imgI = np.sum(image,axis=2) ### get grayscale
imgE = np.sqrt(imgI) #need the E-field before FFT
# of course with 1 and 0 this does not make a difference but for
# completeness make this correct

# h = ifftn(imgray)  #wrong, image barely visible in corners

h = fftshift(ifftn(ifftshift(imgE)))
hInt = np.abs(h)**2 #the sqrt above will just give wrong scaling, but
# the square here is essential for FFT to be defined in correct quantity
hPhase = np.angle(h) # probably because otherwise there is a discrepancy
# between the magnitude abs() and the angle() here...

size = 16*mm
lam = 520*nm
N=512

f=0.75*m

Field = Begin(size, lam, N)
Field = SubIntensity(hInt,Field)
Field = SubPhase(hPhase,Field)
#Field = CircAperture(size/20, 0, 0, Field) #uncomment to enable lowpass filter
I0 = Intensity(0,Field)
Field = Lens(f,0,0,Field)
Field = Forvard(f, Field)
Im_Field = Intensity(0,Field)
Ph = Phase(Field, unwrap=True)
plt.figure()
fig, axs = plt.subplots(1, 2)
ax1, ax2 = axs
im1 = ax1.imshow(np.log(I0), cmap='jet') #switch to log to see filter better
# im1 = ax1.imshow((I0), cmap='gray') #switch to lin to see most information
                                      # is actually in center of input plane
ax1.set_title('I_0 at lens plane')
ax2.imshow((Im_Field), cmap='gray')
ax2.set_title('Ifield')
