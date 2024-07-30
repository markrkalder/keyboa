# RIGHT
import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.split import SplitSide

class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP8,
        board.GP7,
        board.GP6,
        board.GP5,
        board.GP4,
        board.GP3,
        board.GP2,
    )

    row_pins = (board.GP29, board.GP28, board.GP27, board.GP26, board.GP15)
    diode_orientation = DiodeOrientation.COL2ROW
    split_side = SplitSide.RIGHT

    #fmt: off
    coord_mapping = [
        0,  1,  2,  3,  4,  5,                            40, 39, 38, 37, 36, 35,
        7,  8,  9, 10, 11, 12, 13,                        48, 47, 46, 45, 44, 43, 42,
        14, 15, 16, 17, 18, 19, 20,                       55, 54, 53, 52, 51, 50, 49,
        21, 22, 23, 24, 25, 26,                               61, 60, 59, 58, 57, 56,
        28, 29, 30, 31, 32, 33, 34,                       69, 68, 67, 66, 65, 64, 63
    ]
    # fmt:on
