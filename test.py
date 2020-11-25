from LightPipes import *
import matplotlib.pyplot as plt
import numpy as np

wavelength = 633*nm
N = 1024
size = 10*mm
particle = 20*um
z = 1.5*cm
x_shift = 400*um

F_ref = Begin(size,wavelength,N)
F_ref = MultIntensity(F_ref,0.2)

F_obj = Begin(size,wavelength,N)

F_obj1 = CircScreen(F_obj,particle)
F_obj1 = Fresnel(F_obj1,5*mm)
F_obj2 = CircScreen(F_obj1,particle,x_shift,0)
# inten = F_obj.field
# base = np.zeros((2048,2048),dtype=complex)
# base[512:(512+N) ,512:(512+N)] = inten
# F_obj_ = Begin(size*2,wavelength,N*2)
# F_obj_.field=base



# F_obj_ = Fresnel(F_obj_,z)
F_obj_mix = Fresnel(F_obj2,z)
# holo =Forvard(F_obj,z)
holo = BeamMix(F_ref,F_obj_mix)

I=Intensity(2,holo)
plt.imshow(I, cmap='gray'); plt.axis('off');plt.title('intensity pattern')
plt.show()

