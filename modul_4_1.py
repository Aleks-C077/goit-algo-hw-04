# modul_4_1
"""
Module 4, Task 1

"""

from pathlib import Path

def total_salary(path):
    

    file_name = Path(path)
    salary = list()
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                
                salary.append(int(line.split(",")[1].strip()))
    except Exception as e:
        print(f'{e} with file')
        return (0, 0)
    
    total_payroll = sum((salary))
    average_salary = sum((salary)) / len(salary)
    result = (total_payroll, average_salary)
    return result
