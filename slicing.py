s = "Python"
nums = [10, 20, 30, 40, 50]

assert s[1:4] == "yth"
assert s[-3:] == "hon"
assert s[::3] == "Ph"
assert s[4:1:-1] == "oht" # Mistake 1 : "ohty", didn't exclude the end index
assert s[1::3] == "yo"
assert s[::-1] == "nohtyP"

assert nums[-2:] == [40, 50]
assert nums[:2] == [10, 20] # Mistake 2 : [10, 20, 30], didn't exclude the end index again
assert nums[::-1] == [50, 40, 30, 20, 10]

print("All slicing tests passed")
