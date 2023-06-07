# Задача 1

Всё в теоретическом обосновании.

# Задача 2

Вычисления в Wolfram №1 (Якобиан): https://www.wolframalpha.com/input?i2d=true&i=jacobian+%7B%7Bu+*+sqrt%5C%2840%292+*+Divide%5Bln%5C%2840%29Power%5Bu%2C2%5D+%2BPower%5Bv%2C2%5D%5C%2841%29%2CPower%5Bu%2C2%5D+%2BPower%5Bv%2C2%5D%5D%5C%2841%29%7D%2C%7Bv+*+sqrt%5C%2840%292+*+Divide%5Bln%5C%2840%29Power%5Bu%2C2%5D+%2BPower%5Bv%2C2%5D%5C%2841%29%2CPower%5Bu%2C2%5D+%2BPower%5Bv%2C2%5D%5D%5C%2841%29%7D%7D

Вычисления в Wolfram №2 (система уравнений): https://wolfreealpha.on.fleek.co/input?i2d=true&i=solve%7B%7B2+*+Divide%5Bln%5C%2840%29s+%2B+t%5C%2841%29%2Cs+%2B+t%5D*s%7D%2C%7B2+*+Divide%5Bln%5C%2840%29s+%2B+t%5C%2841%29%2Cs+%2B+t%5D*t%7D%7D%3D+%7B%7Bz%7D%2C%7Ba%7D%7D+for+s%5C%2844%29+t&lang=en

# Задача 3

Вычисление интеграла в Wolfram: https://www.wolframalpha.com/input?i2d=true&i=Integrate%5B5Divide%5BPower%5Bx%2C4%5D%2Csqrt%5C%2840%292+pi%5C%2841%29%5D+Power%5Be%2C-Divide%5BPower%5B%5C%2840%295-Power%5Bx%2C5%5D%5C%2841%29%2C2%5D%2C2%5D%5D%2C%7Bx%2C-%E2%88%9E%2Cx%7D%5D

# Задача 4

Вычисление в Wolfram: https://www.wolframalpha.com/input?i=Erfc%5B%28x%29%2F%28Sqrt%5B2%5D%29%5D%2F2+%3C%3D+0.05%2F2

Видно, что ЦПТ оценивает, как надо, а Чебышев — переоценивает:

```
Results for lambda = 0.5:
ЦПТ: 19208 times taken, acceptable share: 0.96
Results for lambda = 1:
ЦПТ: 38416 times taken, acceptable share: 0.95
Results for lambda = 5:
ЦПТ: 192080 times taken, acceptable share: 0.97
Results for lambda = 9:
ЦПТ: 345744 times taken, acceptable share: 0.95
```


```
Results for lambda = 0.5:
Чебышев: 100000 times taken, acceptable share: 1.0
Results for lambda = 1:
Чебышев: 200000 times taken, acceptable share: 1.0
Results for lambda = 5:
Чебышев: 1000000 times taken, acceptable share: 1.0
Results for lambda = 9:
Чебышев: 1800000 times taken, acceptable share: 1.0
```