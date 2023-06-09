# Решение лабораторной 1 по теорВеру by Латыпов Владимир

Таблица с вариантами заданий у меня:

|  | Задание 1 | Задание 2 | Задание 3 |
|---------|-----------|-----------|-----------|
| Вариант       | 2         | 2         | 3         |




## Задание 1

Решение в [PDF](Теоретическая_часть_лабораторной_по_теорверу.pdf) + симуляция в файле [task1_simulation.py](task1_simulation.py).

Плюс графики (получаются в результате запуска `task1_simulation.py`):
- Одна симцляция: показывается, что количество полчивших растёт экспоненциально
- «Обратная» задача: количество итераций для 
половины от максимального количества — растёт логарифмически от `n` —
это показано через подгон линейной регресии к логарифму от `n` и количества итераций:
получаем, что коэфийиенты ЛР такие: `y = 0.9976994142006237 * x + -1.2142857142857206`, то есть `a ≈ 1, b = O(1)`.
Итого: $\mu \sim \log n$.


## Задание 2

Решение в [PDF](Теоретическая_часть_лабораторной_по_теорверу.pdf)

## Задание 3

Решение в [PDF](Теоретическая_часть_лабораторной_по_теорверу.pdf) + симуляция в файле [task3_simulation.py](task3_simulation.py).
