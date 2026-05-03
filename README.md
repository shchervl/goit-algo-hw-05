# goit-algo-hw-05

Порівняння ефективності алгоритмів пошуку підрядка: **Boyer-Moore**, **KMP** та **Rabin-Karp** на двох текстових статтях.

## Структура

```
algorithms/        # реалізації алгоритмів
  boyer_moore.py
  kmp.py
  rabin_karp.py
benchmark/         # логіка вимірювання
  benchmark.py
data/              # тестові тексти
  text_1.txt
  text_2.txt
  patterns.json    # підрядки для пошуку по кожному файлу
results/
  results.md       # результати та висновки
main.py            # точка входу
```

## Запуск

```bash
uv run main.py
```

## Додавання нового тексту

1. Покласти файл у `data/text_N.txt`
2. Додати запис у `data/patterns.json`:

```json
"text_N.txt": {
  "existing": "фраза яка є в тексті",
  "fictional": "фраза якої немає в тексті"
}
```

Бенчмарк автоматично підхопить новий файл при наступному запуску.
