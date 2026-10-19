# list(set(items)) doesn't work: a set is unordered, so the original order is lost.

def remove_duplicates(items):
    unique = []
    seen = set()
    for item in items:
        if item not in seen:
            unique.append(item)
            seen.add(item)

    return unique

assert remove_duplicates(["odoo", "python", "odoo"]) == ["odoo", "python"]
assert remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]
assert remove_duplicates([1, 2, 1, 7, 7, 6, 5, 6]) == [1, 2, 7, 6, 5]
assert remove_duplicates([]) == []
print("All tests passed")
