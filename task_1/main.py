def total_salary(path):
    try:
        total = 0
        count = 0
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    _, salary = line.strip().split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Некоректний формат у рядку: {line}")

        if count == 0:
            return 0, 0
        average = total / count
        return total, average

    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Помилка: {e}")
        return 0, 0


if __name__ == "__main__":
    total, average = total_salary("./salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
