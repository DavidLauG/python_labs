import sys
import os
# Добавляем путь к корневой папке проекта
# Add the path to the project root folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lib.text import normalize, tokenize, count_freq, top_n

sort_list=count_freq(["a","b","a","c","b","b"])

print(normalize('  двойные   пробелы  '))
print(tokenize('emoji 😀 не слово'))
print(sort_list)
print(top_n(sort_list))