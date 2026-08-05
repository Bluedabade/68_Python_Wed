def advanced_string_transformation(s: str) -> str:
    words = s.split(" ")
    words = [w[::-1] for w in words]
    step1 = " ".join(words)

    step2 = step1.swapcase()

    next_vowel = {
        "a": "e", "e": "i", "i": "o", "o": "u", "u": "a",
        "A": "E", "E": "I", "I": "O", "O": "U", "U": "A",
    }
    step3_chars = []
    for ch in step2:
        step3_chars.append(next_vowel.get(ch, ch))
    step3 = "".join(step3_chars)

    out = []
    count = 0
    for ch in step3:
        out.append(ch)
        count += 1
        if count == 3:
            out.append("#")
            count = 0
    step4 = "".join(out)

    return step4

s = "Hello World"
print(advanced_string_transformation(s))
