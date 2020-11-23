#Study note
###Note
Since there are new version (field first) and old version (field last) of this library, the decorator `@backward_compatible` is used to do the transformation.  

### Kind of propagators
*`Forward()` : Propagates the field using direct integration -> far field
* `Forvard()` : Propagates the field using a FFT algorithm. -> near field
* `Steps()` : Propagates the field a distance, nstep x z, in nstep steps in a
    medium with a complex refractive index stored in the
    square array refr.
*`Fresnel()`:  Propagates the field using a convolution method.


### Kind of aperture and screen
* `CircAperture` `RectAperture` `GaussAperture`
* `CircScreen` `RectScreen` `GaussScreen` : the inversion of the aperture 

* the aperture are also used with  `Lens()`function to create typical shape lens
```python
Ffield=CircAperture(Ffield,Dlens/2)
Ffield=Lens(Ffield,f) #in order to create the circular lens
```
###define own phase and intensity filters
`MultIntensity(F,Int)` and `MultiPhase(F,Phi)`


###interference of two beam
`BeamMix` performs the addition of two light field `Fout.field += Fin2.field`