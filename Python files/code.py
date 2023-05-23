print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.extensions.international import International
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import make_key
from kmk.modules.combos import Combos, Chord, Sequence

from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(International())
combos = Combos()
keyboard.modules.append(combos)

keyboard.col_pins = (board.SCL, board.A2, board.SDA, board.A3, board.A1,)
keyboard.row_pins = (board.SCK, board.MISO, board.A0, board.TX, board.RX, board.MOSI)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.NLCK,          KC.D,              KC.C,    KC.B,    KC.A,
        KC.BSPACE,        KC.MNXT,           KC.MPLY, KC.MPRV, KC.A,

        KC.RALT(KC.N7),   KC.P9,             KC.P8,   KC.P7,   KC.LSHIFT(KC.N7),
        KC.RALT(KC.N0),   KC.P6,             KC.P5,   KC.P4,   KC.PAST,
        KC.RALT(KC.N8),   KC.P3,             KC.P2,   KC.P1,   KC.PMNS,
        KC.RALT(KC.N9),   KC.LSHIFT(KC.N0),  KC.N0,   KC.DEL , KC.PPLS,
    ]
]
if __name__ == '__main__':
    keyboard.go()
