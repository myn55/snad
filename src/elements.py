import numpy as np
from enum import Enum

# an element consists of 4 8-bit unsigned integers to save on memory
ELEMENT_TEMPLATE = np.array([
    0, # type - type of element using the ElementType enum
    0, # register A - data storage
    0, # register B - data storage
    0, # clock - frame update
], dtype=np.uint8)

class ElementType(Enum):
    EMPTY = np.uint8(0)
    SAND = np.uint8(1)

ElementColors = [
    (0,)*4,
    (194, 178, 128, 255)
]

# main function for getting an element
def newElement(type : np.uint8):
    return np.array([
        type,
        0,
        0,
        0,        
    ], dtype=np.uint8)