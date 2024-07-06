def total_salary(path: str) -> tuple:
    total_salary = 0
    developers = 0

    try:
        with open(path, 'r') as file:
            for line in file:
                name, salary = line.split(',')
                total_salary += int(salary)
                developers += 1
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return None
    except ValueError:
        print("Файл містить некоректні дані.")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None

    if developers == 0:
         return (0, 0)

    average = total_salary / developers
    return (total_salary, average)

path = 'homework_4_1/salary.txt'
total_salary, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {average}")




