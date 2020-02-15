import sys
import binascii
import numpy as np
from PIL import Image

im =Image.open(sys.argv[1])

pix = np.array(im)

def is_black(pixel):
    if np.any(pixel != 0):
        return False

    return True

def is_white(pixel):
    if np.any(pixel != 255):
        return False
    return True

def binary_to_text(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

binary = ''
for i in range(len(pix)):
    for j in range(len(pix[i])):

        if is_black(pix[i][j]):
            binary = binary + '0'
        if is_white(pix[i][j]):
            binary = binary + '1'
        

print("Binary: \n\t" + binary)
text = binary_to_text(binary)
print("Text: \n\t" + text)