def rgb(r, g, b):
    rgbex = toHex(r) + toHex(g) + toHex(b)
    return rgbex
    
def toHex(d):
    upper_string = ""
    hex_string = hex(d)[2:]  # Remove the "0x" prefix
    if len(hex_string) < 2:  # Ensure 2-digit hexadecimal
        hex_string = ("0" + hex_string)
    upper_string = hex_string.upper()
    if d < 0:
        upper_string = "00"
    if d > 254:
        upper_string = "FF"
    return upper_string
    
    pass