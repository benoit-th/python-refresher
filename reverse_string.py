def reverse_string(text):
    result = ""
    for ch in text:
        result = ch + result

    return result

assert reverse_string("") == ""
assert reverse_string("Odoo") == "oodO"
assert reverse_string("odoo") == "oodo"
assert reverse_string("odoo-test") == "tset-oodo"
print("All tests passed")