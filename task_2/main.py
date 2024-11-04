def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cats_info.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    print(f"Некоректний формат у рядку: {line}")
        return cats_info
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка: {e}")
        return []

cats_info = get_cats_info("cats_file.txt")
print(cats_info)
