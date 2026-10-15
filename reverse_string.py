def reverse_string(text):
    reversed = ""
    for ch in text:
        reversed = ch + reversed

    return reversed

assert reverse_string("") == ""
assert reverse_string("Odoo") == "oodO"
assert reverse_string("odoo") == "oodo"
assert reverse_string("odoo-test") == "tset-oodo"
print("All tests passed")