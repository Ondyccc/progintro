import numpy as np

width = float(input("šiřka: "))
height = float(input("výška: "))
def rectangle (width, height):
    obsah = width * height
    obvod = 2 * (width + height)
    čtverec = width == height
    def scale(factor):
        return width * factor, height * factor
    return obsah, obvod, čtverec, scale
def describe(rectangle):
    obsah, obvod, čtverec, scale = rectangle
    description = f"Obdelník:{width}x{height} Obsah: {obsah}, obvod: {obvod}, Čtverec: {čtverec}"
    return description
print (describe(rectangle(width, height)))