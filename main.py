import sys
from pathlib import Path

# Добавляем src в пути поиска
root_src = Path(__file__).parent / "src"
if str(root_src) not in sys.path:
    sys.path.insert(0, str(root_src))

from megaexnotes.core.parser import SmartParser
from megaexnotes.core.utils import create_blueprint

def main():
    data_dir = Path(__file__).parent / "data"
    data_dir.mkdir(exist_ok=True)

    notes_file = data_dir / "my_notes.md"

    # Если файла нет — создаем blueprint
    if not notes_file.exists():
        create_blueprint(notes_file)
        print(f"[!] Создан шаблон заметок: {notes_file}")
        print("[!] Заполни его и запусти программу снова.")
        return

    parser = SmartParser(notes_file)
    entries = parser.parse()

    print(f"\n{'ТИП':<10} | {'СУММА':<10} | {'НАЗВАНИЕ'}")
    print("-" * 50)

    for e in entries:
        print(f"{e.finance_type:<10} | {e.amount:<10} | {e.title}")

    print("-" * 50)
    print(f"Всего записей обработано: {len(entries)}")

if __name__ == "__main__":
    main()
