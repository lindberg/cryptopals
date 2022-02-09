if __name__ == "__main__":
    ciphertexts = [bytes.fromhex(ciphertext) for ciphertext in open("8.txt").read().split()]

    for idx, ciphertext in enumerate(ciphertexts):
        blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
        if len(blocks) != len(set(blocks)):
            print(f"Ciphertext at line {idx} was encrypted using ECB mode!")