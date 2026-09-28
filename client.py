"""Feldman's Verifiable Secret Sharing (VSS) Engine.
100% Python Standard Library.
"""

class FeldmanVSS:
    """Feldman's Verifiable Secret Sharing with public commitments."""
    P = 2147483647
    G = 7

    def generate_commitments(self, coeffs):
        return [pow(self.G, c, self.P) for c in coeffs]

    def verify_share(self, x, y, commitments):
        lhs = pow(self.G, y, self.P)
        rhs = 1
        for i, c in enumerate(commitments):
            rhs = (rhs * pow(c, pow(x, i), self.P)) % self.P
        return lhs == rhs
