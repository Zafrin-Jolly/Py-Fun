NUM_WORDS = {
    # English
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9,
    # German
    "null": 0, "eins": 1, "zwei": 2, "drei": 3, "vier": 4, "fünf": 5,
    "sechs": 6, "sieben": 7, "acht": 8, "neun": 9,
    # Spanish
    "cero": 0, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9,
    # Russian
    "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5,
    "шесть": 6, "семь": 7, "восемь": 8, "девять": 9,
    # Chinese
    "零": 0, "一": 1, "二": 2, "三": 3, "四": 4,
    "五": 5, "六": 6, "七": 7, "八": 8, "九": 9,
}

ROMAN_MAP = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_to_int(s):
    s = s.strip().upper()
    total = 0
    prev = 0
    for ch in reversed(s):
        val = ROMAN_MAP.get(ch, 0)
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total


class Calculator:
    """A multilingual calculator with support for Roman numerals and factorization."""

    def _to_number(self, value):
        if isinstance(value, (int, float)):
            return value
        if not isinstance(value, str):
            raise ValueError(f"Unsupported type: {type(value)}")
        val = value.strip().lower()
        # Try float
        try:
            return float(val)
        except ValueError:
            pass
        # Try multilingual words
        if val in NUM_WORDS:
            return NUM_WORDS[val]
        # Try Roman numerals
        try:
            return roman_to_int(val)
        except Exception:
            pass
        raise ValueError(f"Unrecognized number format: {value}")

    def add(self, a, b): return self._to_number(a) + self._to_number(b)
    def sub(self, a, b): return self._to_number(a) - self._to_number(b)
    def mul(self, a, b): return self._to_number(a) * self._to_number(b)
    def div(self, a, b): return self._to_number(a) / self._to_number(b)

    def factorize(self, n):
        num = int(self._to_number(n))
        factors = []
        d = 2
        while d * d <= num:
            while num % d == 0:
                factors.append(d)
                num //= d
            d += 1
        if num > 1:
            factors.append(num)
        return factors
