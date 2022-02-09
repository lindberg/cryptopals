import base64
import math
from challenge_5 import xor_encode

letter_frequencies = {
    ' ' : 18.28846265,
    'E' : 10.26665037,
    'T' : 7.51699827,
    'A' : 6.53216702,
    'O' : 6.15957725,
    'N' : 5.71201113,
    'I' : 5.66844326,
    'S' : 5.31700534,
    'R' : 4.98790855,
    'H' : 4.97856396,
    'L' : 3.31754796,
    'D' : 3.28292310,
    'U' : 2.27579536,
    'C' : 2.23367596,
    'M' : 2.02656783,
    'F' : 1.98306716,
    'W' : 1.70389377,
    'G' : 1.62490441,
    'P' : 1.50432428,
    'Y' : 1.42766662,
    'B' : 1.25888074,
    'V' : 0.79611644,
    'K' : 0.56096272,
    'X' : 0.14092016,
    'J' : 0.09752181,
    'Q' : 0.08367550,
    'Z' : 0.05128469
}


def best_match(text_list):
    best_match = None
    best_penalty = math.inf
    key = -1

    # Find best match
    for idx, text in enumerate(text_list):
        if text is None:
            continue
        
        text_upper = text.upper()
        penalty = 0

        for letter, eng_freq in letter_frequencies.items():
            occurrences = text_upper.count(letter)
            freq = occurrences / len(text_upper)

            penalty += abs(freq - eng_freq)
        
        if penalty <= best_penalty:
            best_match = text
            best_penalty = penalty
            key = idx
    
    #print(chr(key))
    return key, best_match


def xor_with_all_bytes(byte_array):
    text_decoded = []

    # Find match with best letter frequencies
    for byte in range(256):
        try:
            text_decoded.append(bytes(x ^ byte for x in byte_array).decode("utf-8"))
        except:
            text_decoded.append(None)
    
    return text_decoded


def hamming_distance(bytes1, bytes2):
    binary_data = [bin(x ^ y) for (x, y) in zip(bytes1, bytes2)]

    distance = 0

    for elem in binary_data:
        distance += elem.count("1")
    
    return distance


input = base64.b64decode(open("6.txt").read())

keysizes = []

for keysize in range(2,41):
    dist = hamming_distance(input[0:keysize], input[keysize:keysize*2]) / keysize
    dist += hamming_distance(input[keysize*2:keysize*3], input[keysize*3:keysize*4]) / keysize
    dist += hamming_distance(input[keysize*3:keysize*4], input[keysize*4:keysize*5]) / keysize
    dist += hamming_distance(input[keysize*4:keysize*5], input[keysize*5:keysize*6]) / keysize
    #dist += hamming_distance(input[keysize*5:keysize*6], input[keysize*6:keysize*7]) / keysize
    dist = dist / 4
    #print(keysize)
    #print(dist)
    keysizes.append((keysize, dist))

keysizes = sorted(keysizes, key=lambda x: x[1])
#print(keysizes)
keysizes = [keysize for (keysize, _) in keysizes[0:3]]

keysize = 29

blocks = []

for _ in range(keysize):
    blocks.append([])

for idx, b in enumerate(input):
    blocks[idx % keysize].append(b)
    #print(idx % keysize)

match = []
key = []

for block in blocks:
    text_decoded = xor_with_all_bytes(block)
    key_byte, m = best_match(text_decoded)
    match.extend(m)
    key.append(key_byte)

    #print(best_match(text_decoded))
    #break

key = bytes(key).decode("ascii")

res = xor_encode(key, input)

print(res.decode("ascii"))
#print(res)

res = []
for _ in range(keysize):
    res.append([])

for idx, b in enumerate(match):
    res[idx % keysize].append(b)


res = [b for a in res for b in a]
#print("".join(res))
#print(bytes(blocks[keysize-1]).decode("utf-8"))