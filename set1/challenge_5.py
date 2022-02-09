def xor_encode(key, input_bytes):
    key_size = len(key)

    res = []
    for idx, c in enumerate(input_bytes):
        res.append(c ^ key[idx % key_size])

    return bytes(res)


if __name__ == "__main__":
    input = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

    res = xor_encode(b'ICE', str.encode(input))
    print(res.hex())