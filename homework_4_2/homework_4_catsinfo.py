def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r') as file:
            for line in file:
                cats_id, name, age = line.split(",")
                cats_info.append({
                    "id": cats_id,
                    "name": name,
                    "age": int(age)
                })
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return None
    except ValueError:
        print("Файл містить некоректні дані.")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None
    
    return cats_info

path = "homework_4_2/cats_info.txt"
cats_info = get_cats_info(path)
print(cats_info)