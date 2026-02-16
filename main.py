from fuzzywuzzy import fuzz
from fuzzywuzzy import process
a = fuzz.ratio('Привет мир', 'Привет мир')
print(a)

a = fuzz.ratio('Привет мир', 'Привт кир')
print(a)

a = fuzz.partial_ratio('Привет мир', 'Привет мир!')
print(a)

a = fuzz.token_sort_ratio('Привет наш мир', 'мир наш Привет')
print(a)

a = fuzz.token_sort_ratio('1 2 Привет наш мир', '1 мир наш 2 ПриВЕт')
print(a)

a = fuzz.token_set_ratio('Привет наш мир', 'мир мир наш наш наш ПриВЕт')
print(a)

a = fuzz.WRatio('Привет наш мир', '!ПриВЕт наш мир!')
print(a)

city = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар", "Воронеж", "Омск", "Екатеринбург", "Орск", "Красногорск", "Красноярск", "Самара"]
a = process.extractOne("Краногрск", city)
print(a)