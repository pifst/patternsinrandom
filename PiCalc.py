import decimal

decimal.getcontext().prec = 100000  # Setting precision


def arccot(n, terms):
    base = 1 / decimal.Decimal(n)
    result = 0
    sign = 1
    for b in range(1, 2 * terms, 2):
        result += sign * (base ** b) / b
        sign = -sign
    return result


pi = (16 * arccot(5, 50) - 4 * arccot(239, 11))

pi2 = int(pi(100,000))
print(pi)

# First 100 of pi
# 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067
