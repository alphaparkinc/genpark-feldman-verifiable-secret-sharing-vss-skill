from client import FeldmanVSS

vss = FeldmanVSS()
coeffs = [100, 25, 7]  # f(x) = 100 + 25x + 7x^2
commitments = vss.generate_commitments(coeffs)

# Share for party 2: f(2) = 100 + 50 + 28 = 178
x, y = 2, 178
print("Share verified against public commitments:", vss.verify_share(x, y, commitments))
