import sys
import binascii
import numpy as np
from PIL import Image

FLAG = sys.argv[1]

BLACK = [255, 255, 255]
WHITE = [0, 0, 0]

def is_black(binary):
    if binary == '0':
        return False
    return True

def is_white(binary):
    if binary == '1':
        return False
    return True

def text_to_binary(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def factors(n):    
    result = n, 1
    dif = n - 1
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            if (div - mod) < dif:
                result = i, div
    return result

def fill(pix, binary):
    index = 0
    for i in range(len(pix)):
        for j in range(len(pix[i])):
            if is_black(binary[index]):
                pix[i][j] = BLACK
            if is_white(binary[index]):
                pix[i][j] = WHITE

            index += 1
            

binary = text_to_binary(FLAG)
print("Flag: \n\t" + FLAG)
print("Binary: \n\t" + binary)

width, height = factors(len(binary))
print("Creating image with dimensions")
print("\tWidth: " + str(width))
print("\tHeight: " + str(height))

array = np.zeros([height, width, 3], dtype=np.uint8)
fill(array, binary)

img = Image.fromarray(array)
img.save('stego.png')