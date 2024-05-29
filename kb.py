# RIGHT
import board
print(dir(board))

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


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
    data_pin = board.RX
    #data_pin = board.GP1
    #data_pin2 = board.GP0

        #flake8: noqa
        #fmt: off
    coord_mapping = [
       0, 1, 2, 3, 4, 5,                       38, 37, 36, 35, 34, 33,
       6, 7, 8, 9, 10, 11, 12,             45, 44, 43, 42, 41, 40, 39,
       13, 14, 15, 16, 17, 18, 19,         52, 51, 50, 49, 48, 47, 46,
       20, 21, 22, 23, 24, 25,                 58, 57, 56, 55, 54, 53,
           26, 27, 28, 29, 30, 31, 32, 65, 64, 63, 62, 61, 60, 59,
    ]
