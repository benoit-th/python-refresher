def word_count(text):
    # count = {word, count.get(count += 1, 1) for word in text}
    count = {}
    for word in text.lower().split():
        count[word] = count.get(word, 0) + 1

    return count

assert word_count("Odoo is great and odoo is open") == {'odoo': 2, 'is': 2, 'great': 1, 'and': 1, 'open': 1}
assert word_count("This is a test") == {'this': 1, 'is': 1, 'a': 1, 'test': 1}
assert word_count("") == {}
print("All tests passed")
