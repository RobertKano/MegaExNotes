import re
from pathlib import Path
from typing import Optional

def extract_amount(text: str) -> float:
    """Извлекает сумму из правой части строки после '|'."""
    # Убираем пробелы между цифрами (10 000 -> 10000)
    clean_text = re.sub(r'(\d)\s+(?=\d)', r'\1', text)
    match = re.search(r'(\d+)\s*(тр|р|т\.р|к|т|т\.р\.)?', clean_text.lower())
    if not match:
        return 0.0

    value = float(match.group(1))
    suffix = match.group(2)
    if suffix in ['тр', 'т.р', 'к', 'т', 'т.р.']:
        return value * 1000
    return value

def extract_date(text: str) -> Optional[str]:
    """Ищет дату строго в формате (DD-MM-YYYY)."""
    match = re.search(r'\((\d{2}-\d{2}-\d{4})\)', text)
    return f"({match.group(1)})" if match else None

def create_blueprint(path: Path):
    """Создает эталонный файл с правилами."""
    content = (
        "# MegaExNotes: My Finance Log\n"
        "> Правило: Сумма ВСЕГДА после разделителя '|'. Дата в скобках (ДД-ММ-ГГГГ) выше блока.\n\n"
        "# Доход\n"
        "- (08-02-2026)\n"
        "    - Зарплата основная | 120 000\n"
        "    - Продажа гитары | 15тр\n\n"
        "# Расход\n"
        "## Периодические\n"
        "- Аренда квартиры | 45 000\n"
        "- Интернет и связь | 1200\n\n"
        "## Разовые\n"
        "- (09-02-2026)\n"
        "    - [ ] Купить кроссовки | 8500\n"
        "    - [x] Поход в кино | 1500\n"
    )
    path.write_text(content, encoding='utf-8')
