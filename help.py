import os


if __name__ == "__main__":
    structure = []
    project_files = []

    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'venv']]
        indent = '  ' * root.replace('.', '').count(os.sep)
        structure.append(f"{indent}{os.path.basename(root)}/")

        for file in sorted(files):
            if file.endswith('.py') and file != 'help.py':
                structure.append(f"{indent}  {file}")
                project_files.append(os.path.join(root, file))


    print("Структура проекта:")
    print("\n".join(structure))
    total_lines = 0

    for filepath in project_files:
        print(f"\nФайл {filepath}:")
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
            total_lines += content.count('\n') + 1

    print(f"СУММАРНОЕ КОЛИЧЕСТВО СТРОК КОДА: {total_lines}")