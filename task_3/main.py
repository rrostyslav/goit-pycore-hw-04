import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def display_directory_structure(path: Path, indent: str = ""):
    try:
        if not path.exists():
            print(f"{Fore.RED}Помилка: Шлях '{path}' не існує.")
            return
        if not path.is_dir():
            print(f"{Fore.RED}Помилка: '{path}' не є директорією.")
            return

        for item in path.iterdir():
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}📂 {item.name}")
                display_directory_structure(item, indent + "  ")
            else:
                print(f"{indent}{Fore.GREEN}📜 {item.name}")

    except Exception as e:
        print(f"{Fore.RED}Помилка: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Вкажіть шлях до директорії як аргумент.")
    else:
        directory_path = Path(sys.argv[1])
        display_directory_structure(directory_path)
