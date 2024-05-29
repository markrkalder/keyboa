from kb import KMKKeyboard

from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
#from kmk.modules.holdtap import HoldTap
#from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
keyboard.debug_enabled = True

#keyboard.modules.append(Layers())
#keyboard.modules.append(HoldTap())
#keyboard.extensions.append(MediaKeys())

split = Split(split_type=SplitType.UART)
keyboard.modules.append(split)


ESC_LCTL = KC.HT(KC.ESC, KC.LCTL)
QUOTE_RCTL = KC.HT(KC.QUOTE, KC.RCTL)
ENT_LALT = KC.HT(KC.ENT, KC.LALT)
MINUS_RCTL = KC.HT(KC.MINUS, KC.RCTL)
keyboard.keymap = [
   [
       KC.ESC,        KC.N1,          KC.N2,          KC.N3,          KC.N4,          KC.N5,                                                                     KC.N6,          KC.N7,          KC.N8,          KC.N9,          KC.N0,          KC.MINUS,
       KC.TAB,        KC.Q,          KC.W,          KC.E,          KC.R,          KC.T,          KC.RIGHT,                                     KC.UP,       KC.Y,          KC.U,          KC.I,          KC.O,          KC.P,          KC.BSPC,
       ESC_LCTL,      KC.A,          KC.S,          KC.D,          KC.F,          KC.G,          KC.LEFT,                                      KC.DOWN,     KC.H,          KC.J,          KC.K,          KC.L,          KC.SCLN,       QUOTE_RCTL,
       KC.LSFT,       KC.Z,          KC.X,          KC.C,          KC.V,          KC.B,                                                                     KC.N,          KC.M,          KC.COMM,       KC.DOT,        KC.SLSH,       KC.RSFT,
                      KC.LBRC,       KC.CAPS,       KC.E,      KC.E,       ENT_LALT,      KC.SPC,        KC.E,       KC.E,      KC.SPC,      KC.RALT,       KC.E,       KC.E,        KC.E,      KC.RBRC,
   ]
]


if __name__ == '__main__':
   keyboard.go()

# [1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016,
# 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027,
# 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038,
# 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049,
# 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060,
# 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071,
# 1072, 1073, 1074, 1075