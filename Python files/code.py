print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.extensions.international import International
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import make_key
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(International())
keyboard.modules.append(Layers())
combos = Combos()
keyboard.modules.append(combos)

keyboard.col_pins = (board.A1, board.A3, board.SDA, board.A2, board.SCL,)
keyboard.row_pins = (board.SCK, board.MISO, board.A0, board.TX, board.RX, board.MOSI)



keyboard.diode_orientation = DiodeOrientation.COL2ROW

"""
The below was just an input test, to se if all buttons were working.
Layer 1:
a b  c  d  OK
a OK OK OK OK
/ 7  8  9  {
* 4  5  6  }
- 1  2  3  [
+ OK 0  =  ]
"""
"""
The following is the layout I soldered, though I do not recommend it for organizing
#        1  2  3   4    5
  PIN   A1 A3 SDA A2   SCL
1 SCK   [] [] []  []   []
2 MISO  [] [] []  []   []

3 A0    [] [] []  []   []
4 TX    [] [] []  []   []
5 RX    [] [] []  []   []
6 MOSI  [] [] []  []   []
"""

"""
               NUMPAD LAYER
#        1      2      3       4       5
  PIN   A1     A3     SDA     A2      SCL
1 SCK   [INS]  [COPY] [PASTE] [CUT]   [NUM]
2 MISO  [LYR1] [<-]   [||]    [->]    [<--]

3 A0    [/]    [7]    [8]     [9]     [{]
4 TX    [*]    [4]    [5]     [6]     [}]
5 RX    [-]    [1]    [2]     [3]     [[]
6 MOSI  [+]    [DEL]  [0]     [=]     []]
"""

"""
                ARROW LAYER
#        1       2      3       4      5
  PIN   A1      A3     SDA     A2     SCL
1 SCK   [ESC]   [F1]   [F2]    [F3]   [F4]
2 MISO  [LYR1]  [1]    [2]     [3]    [4]

3 A0    [TAB]   [Q]    [W]     [R]    [A]
4 TX    [C]     [A]    [S]     [D]    [A]
5 RX    [SHIFT] [T]    [B]     [E]    [A]
6 MOSI  [Z]     [CTRL] [SPACE] [A]    [A]
"""

keyboard.keymap = [
    [
        KC.INS,           KC.LCTRL(KC.C), KC.LCTRL(KC.V), KC.LCTRL(KC.X),       KC.NLCK,
        KC.TO(1),         KC.MPRV,        KC.MPLY,        KC.MNXT,              KC.BSPACE,

        KC.LSHIFT(KC.N7), KC.P7,          KC.P8,          KC.P9,                KC.RALT(KC.N7),
        KC.PAST,          KC.P4,          KC.P5,          KC.P6,                KC.RALT(KC.N0),
        KC.PMNS,          KC.P1,          KC.P2,          KC.P3,                KC.RALT(KC.N8),
        KC.PPLS,          KC.DEL,         KC.P0,          KC.LSHIFT(KC.N0),     KC.RALT(KC.N9),
    ],
    [
        KC.ESC,    KC.F1,   KC.F2,    KC.F3,   KC.F4,
        KC.TO(0),  KC.N1,   KC.N2,    KC.N3,   KC.N4,

        KC.TAB,    KC.Q,    KC.W,     KC.R,    KC.A,
        KC.C,      KC.A,    KC.S,     KC.D,    KC.A,
        KC.LSHIFT, KC.T,    KC.B,     KC.E,    KC.A,
        KC.Z,      KC.CTRL, KC.SPACE, KC.A,    KC.A,
    ]
]
if __name__ == '__main__':
    keyboard.go()
