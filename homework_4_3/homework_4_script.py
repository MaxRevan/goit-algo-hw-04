import sys
from pathlib import Path
from colorama import Fore, Back, Style

def list_directory_contents(dir_path, indent=''):
    dir_path = Path(dir_path)
    if not dir_path.is_dir():
        raise ValueError(f"{dir_path} is not a valid directory.")
    
    for item in sorted(dir_path.iterdir()):
        if item.is_dir():
            print(f"{indent}{Fore.BLACK + Back.YELLOW}{item.name}{Style.RESET_ALL}/")
            list_directory_contents(item, indent + '    ')
        else:
            print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python homework_4_script.py 'directory_path'")
        sys.exit(1)

    directory_path = sys.argv[1]
    try:
        list_directory_contents(directory_path)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

