import board
from kb import KMKKeyboard

from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.keys import KC

keyboard = KMKKeyboard()
keyboard.debug_enabled = True

#keyboard.modules.append(Layers())
#keyboard.extensions.append(MediaKeys())
split = Split(split_type=SplitType.UART, split_side=SplitSide.LEFT, use_pio=True, uart_flip=False)
keyboard.modules.append(split)

# fmt:off
keyboard.keymap = [
   [
       KC.ESC,        KC.N1,          KC.N2,          KC.N3,          KC.N4,          KC.N5,                                                                     KC.N6,          KC.N7,          KC.N8,          KC.N9,          KC.N0,          KC.MINUS,
       KC.TAB,        KC.Q,          KC.W,          KC.E,          KC.R,          KC.T,          KC.RIGHT,                                     KC.UP,       KC.Y,          KC.U,          KC.I,          KC.O,          KC.P,          KC.BSLS,
       KC.LSFT,       KC.A,          KC.S,          KC.D,          KC.F,          KC.G,          KC.LEFT,                                      KC.DOWN,     KC.H,          KC.J,          KC.K,          KC.L,          KC.SCLN,       KC.QUOT,
       KC.LCTL,       KC.Z,          KC.X,          KC.C,          KC.V,          KC.B,                                                                     KC.N,          KC.M,          KC.COMM,       KC.DOT,        KC.SLSH,       KC.RSFT,
       KC.LGUI,       KC.LALT,       KC.BSPC,       KC.DEL,        KC.E,      KC.LBRC,        KC.EQL,                  KC.EQL,      KC.RBRC,      KC.RALT,       KC.ENT,       KC.SPC,        KC.E,      KC.RBRC,
   ]
]
# fmt:on

if __name__ == '__main__':
   keyboard.go()
