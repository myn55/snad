import numpy as np
from enum import Enum

class ElementType(Enum):
    EMPTY = np.uint8(0)
    SAND = np.uint8(1)

class ElementColors(Enum):
    EMPTY = (0)*4
    SAND = (194, 178, 128, 255)

# an element consists of 4 8-bit unsigned integers to save on memory
ELEMENT_TEMPLATE = np.array([
    0, # type - type of element using the ElementType enum
    0, # register A - data storage
    0, # register B - data storage
    0, # clock - frame update
], dtype=np.uint8)