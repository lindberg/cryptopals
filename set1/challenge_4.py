from challenge_3 import best_match, xor_with_all_bytes


if __name__ == "__main__":
    lines = open("4.txt").read().split("\n")
    candidate_texts = []

    for line in lines:
        line = bytes.fromhex(line)
        candidate_texts.extend(xor_with_all_bytes(line))

    key, res = best_match(candidate_texts)
    print(chr(key))
    print(res)