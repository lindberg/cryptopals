import math


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

    # Find best match
    for text in text_list:
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
    
    return best_match


def xor_with_all_bytes(hex_string):
    byte_array = bytes.fromhex(hex_string)

    text_decoded = []

    # Find match with best letter frequencies
    for byte in range(256):
        try:
            text_decoded.append(bytes(x ^ byte for x in byte_array).decode("utf-8"))
        except:
            text_decoded.append(None)
    
    return text_decoded



if __name__ == "__main__":
    hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

    text_decoded = xor_with_all_bytes(hex_string)

    match = best_match(text_decoded)

    print(match)
