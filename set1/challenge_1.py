def hex2base64(hex_string):
    # hex string to bit string
    bitstring = bin(int(hex_string, base=16))[2:]

    # add any zeroes that has disappeared
    while len(bitstring) % 6 != 0:
        bitstring = "0" + bitstring

    # divide into 6 bit chunks
    chunks = [bitstring[i:i+6] for i in range(0, len(bitstring), 6)]

    res = ""
    for chunk in chunks:
        char_idx = int(chunk, 2)

        # convert to base64
        if char_idx <= 25:
            res += chr(char_idx + 65)
        elif char_idx <= 51:
            res += chr(char_idx + 97 - 26)
        elif char_idx <= 61:
            res += chr(char_idx + 48 - 52)
        elif char_idx == 62:
            res += "+"
        elif char_idx == 63:
            res += "/"
        else:
            print("Something went wrong!")
            exit()

    return res


if __name__ == "__main__":
    hex_string = '0x49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    print(hex2base64(hex_string))