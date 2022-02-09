from challenge_3 import best_match, xor_with_all_bytes


lines = open("4.txt").read().split("\n")
candidate_texts = []

for line in lines:
    candidate_texts.extend(xor_with_all_bytes(line))

res = best_match(candidate_texts)
print(res)
