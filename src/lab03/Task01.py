import sys
import os
# Добавляем путь к корневой папке проекта
# Add the path to the project root folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lib import text

sort_list=text.count_freq(["a","b","a","c","b","b"])

print(text.normalize('  двойные   пробелы  '))
print(text.tokenize('emoji 😀 не слово'))
print(sort_list)
print(text.top_n(sort_list))