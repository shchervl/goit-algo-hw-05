import json
import timeit
from pathlib import Path

from algorithms import boyer_moore, kmp, rabin_karp

DATA_DIR = Path(__file__).parent.parent / "data"

ALGORITHMS = {
    "Boyer-Moore": boyer_moore,
    "KMP":         kmp,
    "Rabin-Karp":  rabin_karp,
}

REPEATS = 1000


def load_texts(patterns: dict) -> dict[str, str]:
    return {
        f.name: f.read_text(encoding="utf-8")
        for f in sorted(DATA_DIR.glob("*.txt"))
        if f.name in patterns
    }


def load_patterns() -> dict:
    return json.loads((DATA_DIR / "patterns.json").read_text(encoding="utf-8"))


def measure_pattern(text: str, pattern: str) -> dict[str, float]:
    """Measure all algorithms on a single text+pattern. Returns {algo: ms}."""
    return {
        algo_name: timeit.timeit(lambda: algo(text, pattern), number=REPEATS) / REPEATS * 1000
        for algo_name, algo in ALGORITHMS.items()
    }


def benchmark() -> None:
    patterns = load_patterns()
    texts = load_texts(patterns)

    col_w = 14
    header = f"{'Алгоритм':<{col_w}} {'Текст':<12} {'Підрядок':<12} {'Час (мс)':>10}"
    print(header)
    print("-" * len(header))

    results: dict[str, dict[str, dict[str, float]]] = {}
    first_group = True

    for filename, text in texts.items():
        results[filename] = {}
        for kind, pattern in patterns[filename].items():
            if not first_group:
                print()
            first_group = False
            times = measure_pattern(text, pattern)
            results[filename][kind] = times
            for algo_name, ms in times.items():
                print(f"{algo_name:<{col_w}} {filename:<12} {kind:<12} {ms:>10.4f}")

    print()
    print("=== Висновки ===")

    for filename, by_kind in results.items():
        for kind, times in by_kind.items():
            winner = min(times, key=times.get)
            print(f"{filename} | {kind}: найшвидший → {winner} ({times[winner]:.4f} мс)")
