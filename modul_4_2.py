# modul_4_2
"""
Modul 4, Task 2

"""
from pathlib import Path

def get_cats_info(path):
    
    file_name = Path(path)
    list_cat = []
    keys = ["id", "name","age"]
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                
                elements = line.strip().split(",")
                list_cat.append(dict(zip(keys, elements)))
                
    except Exception as e:
        print(f'{e} with file')
    return list_cat