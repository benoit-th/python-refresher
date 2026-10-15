def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for ch in text:
        if ch.lower() in vowels:
            count += 1

    return count

assert count_vowels("Odoo Developer") == 7
assert count_vowels("") == 0
assert count_vowels("xyz") == 0
assert count_vowels("AEIOU") == 5
print("All tests passed")