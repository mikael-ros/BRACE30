# BRACE30

Excuse the assorted keycaps :o (I did not have all of them)
![BRACE30](/Images/BRACE30_ONDESK_ANGLE.jpg "BRACE30")

A 30% extended numpad, running on the tiny Adafruit QT PY 2040. 

I only designed this to get a shortcut for {}, [], and / - hence "BRACE"

My first handwired keyboard, and one of my first CAD designs overall.

---

## Parts used
* eSun PLA+ White, for case and plate
* Adafruit QT PY RP2040, for controlling keys
* Colored cables for identification
* "1N4148 DO-35 75V 300mA" diodes
* Kailh BOX White switches
* Mainly Steelseries Pudding keycaps
* 5 mm long M3 screws, specifically harvested from an old microwave at some point

## Features
* KMK (all though, this depends on your microcontroller)
* 30 keys
* Matched to the dimensions of the Epomaker TH80 Pro
    * Which means a curved side profile
* Nordic layout support (by way of key combos in KMK)
* Screw threads built in, if you print at the right settings

## Design process
1. [Keyboard layout editor](http://www.keyboard-layout-editor.com/##@@_y:0.25&a:7%3B&=%E2%9D%A4&=%E2%9D%A4&=%E2%9D%A4&=%E2%9D%A4&_x:0.25&fa@:1%3B%3B&=%E2%AD%95%3B&@_f:3%3B&=FN&_f:3%3B&=PREV&_f:3%3B&=PAUSE&_f:3%3B&=NEXT&_x:0.25%3B&=BACK%3B&@_y:0.25&f:3%3B&=%2F%2F&_f:3%3B&=7&_f:3%3B&=8&_f:3%3B&=9&_x:0.25&f:3%3B&=%7B%3B&@_f:3%3B&=*&_f:3%3B&=4&_f:3%3B&=5&_f:3%3B&=6&_x:0.25&f:3%3B&=%7D%3B&@_f:3%3B&=-&_f:3%3B&=1&_f:3%3B&=2&_f:3%3B&=3&_x:0.25&f:3%3B&=%5B%3B&@_f:3%3B&=+&_f:3%3B&=DEL&_f:3%3B&=0&_f:3%3B&=%2F=&_x:0.25&f:3%3B&=%5D) was used to make the layout, and export it
2. [ai03](https://kbplate.ai03.com/) was then used to export the plate CAD files
3. Measurments were taken of the Epomaker and the parts
4. The model was sketched up in Fusion 360
### Pitfalls
* During the project, I first tried to print with PETG, which was a nightmare
* I had to cut the USB C port a little, to allow room for the USB C cable

## 3D printing settings
> I used a Sovol SV06 to print these

### Plate
* See CURA profile in CAD files, but change:
    * 50% infill, Cross 3D
    * Print upside down

### Case
* See CURA profile in CAD files

## Construction
![BRACE30 plate](/Images/BRACE30_PLATE.jpg "BRACE30 plate")

1. I first soldered all the rows, with the diode legs, then all the columns, see [Mad Mod Labs](https://www.youtube.com/watch?v=iv__343ZwE0&t=1068s)
2. I then soldered each column and row to a GPIO pin each

![BRACE30 cables](/Images/BRACE30_CABLES.jpg "BRACE30 cables")

![BRACE30 soldered](/Images/BRACE30_SOLDERED.jpg "BRACE30 soldered")

3. Extended the hole for the USB C cable (check "Known Issues")

![BRACE30 cutout](/Images/BRACE30_USBC_CUTOUT.jpg "BRACE30 cutout")

4. Downloaded and installed CircuitPython onto the board, and then [KMK](https://github.com/KMKfw/kmk_firmware)
5. Sanded the sides until smooth
6. Screwed together the case and glued the microcontroller to the port section

![BRACE30 switchplate](/Images/BRACE30_NOCAP.jpg "BRACE30 switchplate")
---

## Known issues
- [ ] USB C port is not flush, you need to cut into the PLA or redesign the case
- [ ] Plate height is higher than TH80, which was not the plan, but it does not affect anything
- [ ] Tolerances on plate are a tad too loose, which could be fixed by subtracting about 0.1 mm from the holes - this means switches easily pop out currently (unless you decide to hot glue them)
- [ ] Microcontroller does not fit into slot made for it, needs an additional tolerance of about 0.2-0.3 mm
- [ ] KMK is for some reason flipped
- [ ] Work around for Nordic keys

## Future plans
- [ ] Print a new case
- [ ] Make firmware more advanced
- [ ] Get uniform keycaps
