import board
from kb import KMKKeyboard
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType
from kmk.keys import KC
from kmk.hid import HIDModes
keyboard = KMKKeyboard()
keyboard.debug_enabled = True
keyboard.modules.append(Layers())
split = Split(split_type=SplitType.UART, split_side=keyboard.split_side, data_pin=board.GP1, data_pin2=board.GP0, use_pio=True, uart_flip=False)
keyboard.modules.append(split)

# keymap
keyboard.keymap = [ [KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.R,KC.T,KC.E,KC.E,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.E,KC.E,KC.A,KC.S,KC.D,KC.F,KC.G,KC.E,KC.E,KC.H,KC.J,KC.K,KC.L,KC.E,KC.E,KC.E,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.N,KC.M,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E,KC.E],
[],
[],
[],
[],
[],
[],
[] ]
# keymap
if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.USB)
