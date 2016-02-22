BBpystepper
===========
`bbpystepper` is a Python module for controlling stepper motors with the
BeagleBone Black. The code by default uses full-stepping.


Dependencies
------------
  * Adafruit_BBIO


Installation
------------
  * Log in via SSH and then `git clone https://github.com/petebachant/BBpystepper.git`
  * `cd BBpystepper`
  * `python setup.py install`


Usage example
-------------

```python
>>> from bbpystepper import Stepper
>>> mystepper = Stepper()
>>> mystepper.rotate(180, 10) # Rotates motor 180 degrees at 10 RPM
>>> mystepper.rotate(-180, 5) # Rotates motor back 180 degrees at 5 RPM
>>> mystepper.angle
0.0
```


Notes
-----

* By default the GPIO pins used are `P8_13`, `P8_14`, `P8_15`, and `P8_16`. These can
  be changed by modifying the `Stepper.pins` list.

* By default the `Stepper.steps_per_rev` parameter is set to 2048 to match my
  motor (it has a built-in gearbox).

* The code doesn't keep track of where it ends in the sequence of pins. It
  simply sets all pins low after a move. This means there could be some
  additional error in the `Stepper.angle` variable if the amount of steps moved
  is not divisible by 4.
