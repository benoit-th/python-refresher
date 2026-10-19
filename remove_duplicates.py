# For this exercise : The set is not a good idea because this is not an ordered type of data, so I will lose the order it has been given to me.

def remove_duplicates(items):
    unique = []
    items_set = set()
    for item in items:
        if item not in items_set:
            unique.append(item)
            items_set.add(item)

    return unique

assert remove_duplicates(["odoo", "python", "odoo"]) == ["odoo", "python"]
assert remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]
assert remove_duplicates([1, 2, 1, 7, 7, 6, 5, 6]) == [1, 2, 7, 6, 5]
assert remove_duplicates([]) == []
print("All tests passed")
