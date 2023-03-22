""" Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла.Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
 исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано.
   Далее счётчик файлов и расширение
"""
import os
import shutil
from pathlib import Path

with (
open('text_one.md', 'w', encoding='utf-8')as f1,
open('text_two.txt', 'w', encoding='utf-8') as f2,
open('text_three.txt', 'w', encoding='utf-8')as f3,
open('text_four.txt', 'w', encoding='utf-8')as f4
):
    f1.write('Hello world!')
    f2.write('Hello world!')
    f3.write('Hello world!')
    f4.write('Hello world!')


#желаемое конечное имя файлов new_name
#количество цифр в порядковом номере - не знаю как сделать
#расширение исходного файла ext_old
#расширение конечного файла new_ext
#диапазон сохраняемого оригинального имени сut [а:b]
#порядковый номер i
        
dir_files = os.listdir()
print(dir_files)

def files_rename(new_name: str,  ext_old: str, new_ext: str, a,b:int):
    for i in range(len(dir_files)):
        if ext_old in dir_files[i]:
            cut =dir_files[i][a:b]
            name = (f'{cut}{new_name}{i}{new_ext}')
            os.rename(dir_files[i], name)
            

files_rename('file', '.txt','.md', 0, 3)




