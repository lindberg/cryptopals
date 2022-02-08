input = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

input_bytes = str.encode(input)

key = str.encode("ICE")

res = []
for idx, c in enumerate(input_bytes):
    res.append(c ^ key[idx % 3])

print(bytes(res).hex())
