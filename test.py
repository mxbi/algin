from vec import v

x = v([1, 2, 3, 4])
y = v([2, 0, 0, 1])

assert str(x) == 'Vector: [1, 2, 3, 4]'
assert x != y
assert x == v([1, 2, 3, 4])

# Test addition
assert x + y == v([3, 2, 3, 5])
assert y + x == x + y
assert x + 5 == v([6, 7, 8, 9])
assert x + 5 == 5 + x

# Test multiplication
assert x * y == v([2, 0, 0, 4])
assert y * x == x * y
assert y * 5 == v([10, 0, 0, 5])
assert y * 5 == 5 * y

# Test subtraction
assert x - y == v([-1, 2, 3, 3])
assert y - x == v([1, -2, -3, -3])
assert x - 1 != 1 - x
assert x - 1 == v([0, 1, 2, 3])
assert 1 - y == v([-1, 1, 1, 0])

# Test true division
assert y / x == v([2, 0, 0, 0.25])
assert x / 2 != 2 / x
assert x / 2 == v([0.5, 1, 1.5, 2])
assert y / 2 == v([1, 0, 0, 0.5])
assert 2 / x == v([2, 1, 2 / 3, 0.5])

# Test floor division
assert y // x == v([2, 0, 0, 0])
assert x // 2 != 2 // x
assert x // 2 == v([0, 1, 1, 2])
assert y // 2 == v([1, 0, 0, 0])
assert 2 // x == v([2, 1, 0, 0])

print('All tests pass!')
