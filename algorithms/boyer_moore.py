def _bad_char(pattern: str) -> dict:
    return {ch: i for i, ch in enumerate(pattern)}


def boyer_moore(text: str, pattern: str) -> int:
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    bad_char = _bad_char(pattern)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        shift = j - bad_char.get(text[s + j], -1)
        s += max(1, shift)
    return -1
