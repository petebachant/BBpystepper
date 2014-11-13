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


License
-------

BBpystepper Copyright (c) 2013-2014 Peter Bachant

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
