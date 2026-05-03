def rabin_karp(text: str, pattern: str, base: int = 256, mod: int = 101) -> int:
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    h = pow(base, m - 1, mod)
    p_hash = t_hash = 0
    for i in range(m):
        p_hash = (base * p_hash + ord(pattern[i])) % mod
        t_hash = (base * t_hash + ord(text[i])) % mod
    for s in range(n - m + 1):
        if p_hash == t_hash:
            if text[s:s + m] == pattern:
                return s
        if s < n - m:
            t_hash = (base * (t_hash - ord(text[s]) * h) + ord(text[s + m])) % mod
    return -1
