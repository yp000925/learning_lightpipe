from LightPipes import *
import matplotlib.pyplot as plt
import numpy as np

"""
    Fresnel zone plate
"""

size = 12 * mm
wavelength = 5 * um
N = 1000
N2 = int(N / 2)

f = 5 * cm
N_zones = 100
T = 1
p = 8 * cm
q = 1 / (1 / f - 1 / p)

dx = 0.1 * mm
PassEvenZones = False

F = Begin(size, wavelength, N)
F = GaussBeam(F, 0.5 * mm)
F1 = PointSource(F, x=-dx)
F2 = PointSource(F, x=dx)
F = BeamMix(F1, F2)
I0 = Intensity(F)
F = Fresnel(F, p)
# F=Lens(F,f)
# F=ZonePlate(F,N_zones)
#%%

F = ZonePlate(F, N_zones, f=f, T=T, PassEvenZones=PassEvenZones)
# F=ZonePlate(F,N_zones,p=p,q=q,T=T, PassEvenZones=PassEvenZones)
I2 = Intensity(F)
F = Fresnel(F, q)
I1 = Intensity(F, 1)

s1 = r'LightPipes for Python' + '\n'
s2 = r'Test-ZonePlate.py' + '\n\n' \
    f'size = {size / mm:4.2f} mm' + '\n' \
         f'$\lambda$ = {wavelength / um:4.2f} $\mu$m' + '\n' \
         f'N = {N:d}' + '\n' + \
     f'f = {f / mm:4.2f} mm' + '\n' \
         f'p = {p / mm:4.2f} mm' + '\n' \
         f'q = {q / mm:4.2f} mm' + '\n' \
         f'number of zones = {N_zones:d}' + '\n' \
         f'Transmission = {T:4.2f}' + '\n' \
         f'Pass even zones: {PassEvenZones}' + '\n\n' \
                                               r'${\copyright}$ Fred van Goor, June 2020'

fig = plt.figure(figsize=(11, 6))
ax1 = fig.add_subplot(221);
ax1.axis('off')
ax2 = fig.add_subplot(222);
ax2.axis('off')
ax3 = fig.add_subplot(223);
ax3.axis('off')
ax4 = fig.add_subplot(224);
ax1.imshow(I2, cmap='gray');
ax1.set_title('input intensity')
ax2.imshow(I1, cmap='jet');
ax2.set_title('output intensity')
ax3.text(0.0, 1.0, s1, fontsize=12, fontweight='bold')
ax3.text(0.0, 0.0, s2)
X = np.linspace(-size / 2, size / 2, N)
ax4.plot(X / mm, I1[N2]);
ax4.set_xlabel('x[mm]');
ax4.set_ylabel('Intensity [a.u.]')
plt.show()
