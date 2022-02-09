import base64
import math

from challenge_2 import xor_byte_arrays
from challenge_3 import best_match, xor_with_all_bytes
from challenge_5 import xor_encode


def hamming_distance(bytes1, bytes2):
    binary_data = [bin(x) for x in xor_byte_arrays(bytes1, bytes2)]

    distance = 0

    for elem in binary_data:
        distance += elem.count("1")
    
    return distance


def guess_keysize(input):
    keysizes = []

    for keysize in range(2,41):
        # all combinations of first 4 keysize blocks
        dist = hamming_distance(input[0:keysize], input[keysize:keysize*2]) / keysize
        dist += hamming_distance(input[0:keysize], input[keysize*2:keysize*3]) / keysize
        dist += hamming_distance(input[0:keysize], input[keysize*3:keysize*4]) / keysize
        dist += hamming_distance(input[keysize:keysize*2], input[keysize*2:keysize*3]) / keysize
        dist += hamming_distance(input[keysize:keysize*2], input[keysize*3:keysize*4]) / keysize
        dist += hamming_distance(input[keysize*2:keysize*3], input[keysize*3:keysize*4]) / keysize
        dist = dist / 6
        keysizes.append((keysize, dist))

    keysizes = sorted(keysizes, key=lambda x: x[1])
    keysize = keysizes[0][0]
    return keysize



if __name__ == "__main__":
    input = base64.b64decode(open("6.txt").read())

    keysize = guess_keysize(input)

    blocks = []

    for _ in range(keysize):
        blocks.append([])

    for idx, b in enumerate(input):
        blocks[idx % keysize].append(b)

    match = []
    key = []

    for block in blocks:
        text_decoded = xor_with_all_bytes(block)
        key_byte, m = best_match(text_decoded)
        match.extend(m)
        key.append(key_byte)

    key = bytes(key).decode("ascii")

    res = xor_encode(key, input)

    print(res.decode("ascii"))

    res = []
    for _ in range(keysize):
        res.append([])

    for idx, b in enumerate(match):
        res[idx % keysize].append(b)


    res = [b for a in res for b in a]