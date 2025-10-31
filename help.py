import os
import glob


def print_file_content(path, relative_path):
    print(f"Файл {relative_path}:")

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
        return content.count('\n') + 1


def get_project_structure():
    structure = []

    for root, dirs, files in os.walk('.'):
        # Игнорируем служебные папки
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__']]

        level = root.replace('.', '').count(os.sep)
        indent = '  ' * level
        structure.append(f"{indent}{os.path.basename(root)}/")

        subindent = '  ' * (level + 1)
        for file in sorted(files):
            if file.endswith('.py') and file != 'help.py':  # Игнорируем себя
                structure.append(f"{subindent}{file}")

    return '\n'.join(structure)


if __name__ == "__main__":

    print("Структура проекта:")
    print(get_project_structure())
    print()

    # Находим все Python файлы
    python_files = []
    for pattern in ['**/*.py', '*.py']:
        python_files.extend(glob.glob(pattern, recursive=True))

    # Игнорируем служебные папки и сам help.py
    python_files = [
        f for f in python_files
        if not any(ignore in f for ignore in ['__pycache__', '/.', '\\..', 'venv', 'help'])
    ]

    total_lines = 0
    # Выводим содержимое каждого файла
    for filepath in python_files:
        relative_path = filepath if filepath.startswith('.') else f"./{filepath}"
        total_lines += print_file_content(filepath, relative_path)

    # Выводим суммарное количество строк кода
    print(f"\nСУММАРНОЕ КОЛИЧЕСТВО СТРОК КОДА: {total_lines}")
