# rsa.py

class RSA:
    def __init__(self):
        self.p = None
        self.q = None
        self.n = None
        self.phi = None
        self.e = None
        self.d = None

    def compute_key(self, prime1, prime2, coprime_index):
        """Generates the public and private keys using two primes and a coprime index."""
        # Step 1: Set primes and calculate modulus n = p * q
        self.p = prime1
        self.q = prime2
        self.n = self.p * self.q

        # Step 2: Calculate Euler's Totient function, φ(n) = (p - 1) * (q - 1)
        self.phi = (self.p - 1) * (self.q - 1)

        # Step 3: Find coprimes of φ(n)
        coprimes = self._find_coprimes(self.phi)

        # Step 4: Choose the e (public exponent) based on coprime_index
        if coprime_index <= len(coprimes):
            self.e = coprimes[coprime_index - 1]  # Coprime index is 1-based
        else:
            raise ValueError("Coprime index is out of bounds")

        # Step 5: Calculate d (private exponent) such that (d * e) % φ(n) = 1
        self.d = self._mod_inverse(self.e, self.phi)

    def encrypt(self, plaintext):
        """Encrypts the given message using the public key (e, n)."""
        return pow(plaintext, self.e, self.n)

    def decrypt(self, ciphertext):
        """Decrypts the given message using the private key (d, n)."""
        return pow(ciphertext, self.d, self.n)

    def _find_coprimes(self, num):
        """Find all integers less than num that are coprime with num."""
        coprimes = []
        for i in range(2, num):
            if self._gcd(i, num) == 1:
                coprimes.append(i)
        return coprimes

    def _gcd(self, a, b):
        """Calculates the Greatest Common Divisor using the Euclidean algorithm."""
        while b != 0:
            a, b = b, a % b
        return a

    def _mod_inverse(self, a, m):
        """Finds the modular inverse of a under modulo m using the Extended Euclidean Algorithm."""
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1
