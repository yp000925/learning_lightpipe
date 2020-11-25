#Study note


### Note
Since there are new version (field first) and old version (field last) of this library, the decorator `@backward_compatible` is used to do the transformation.  

### Kind of propagators
*`Forward()` : Propagates the field using direct integration -> far field
* `Forvard()` : Propagates the field using a FFT algorithm. -> near field  (the simplest and fastest, the spectral method)
* `Steps()` : Propagates the field a distance, nstep x z, in nstep steps in a
    medium with a complex refractive index stored in the
    square array refr. [example](LensLikeMedium.py)
*`Fresnel()`:  Propagates the field using a convolution method.


### Kind of aperture and screen
* `CircAperture` `RectAperture` `GaussAperture`
* `CircScreen` `RectScreen` `GaussScreen` : the inversion of the aperture 
other aperture
`SuperGaussAperture(Fin, w, n=2.0, x_shift=0.0, y_shift=0.0, T=1.0)`
* the aperture are also used with  `Lens()`function to create typical shape lens
```python
Ffield=CircAperture(Ffield,Dlens/2)
Ffield=Lens(Ffield,f) #in order to create the circular lens
```
### [define own phase and intensity filters](subintphase2.py)
`MultIntensity(F,Int)` and `MultiPhase(F,Phi)`
`MultIntensity(F,Int)` : Intens: numpy.ndarray, float, int $E_{out} = E_{in}\times A^2$
`MultiPhase(F,Phi)` : $E_{out} = E_{in}\times e^{j\phi}$
`RandomIntensity(Fin, seed=123, noise=1.0)`
`RandomPhase(Fin, seed=456, maxPhase=3.141592653589793)`
`SubIntensity(Fin, Intens)` : Substitutes a given intensity distribution in the field with $sqrt(A)$. 
`SubPhase(Fin, Phi)` : Substitutes a given phase distribution in the field with $e^{j\phi}$.


### [interference of two beam](Young.py)
`BeamMix` performs the addition of two light field `Fout.field += Fin2.field`


### Field manipulation 
`Phase(Field)`+`PhaseUnwrap(Phi)` 
`Intensity(Field)` 
`Power(Fin)`
`Tilt(Fin, tx, ty)` : tx (int, float) –> tilt in radians ; ty (int, float) –> tilt in radians
### Fourier Transform
`PipFFT(Fin,index = 1)` : index=1-> forward transform index=-1-> back transform 


### Wave form
`PlaneWave(Fin, w, tx=0.0, ty=0.0, x_shift=0.0, y_shift=0.0)` :Creates a (circular) plane wavefront with diameter of w 
`PointSource(Fin, x=0.0, y=0.0)`
`GaussBeam( Fin, w0, n=0, m=0, xshift=0, yshift=0, tx=0, ty=0, doughnut=False, LG=False)`

