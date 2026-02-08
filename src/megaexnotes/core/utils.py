from typing import Optional
import re


def extract_amount(text: str) -> float:
    """Извлекает числовое значение из строк типа '600р', '10тр', '12 000'.

    Args:
        text (str): Строка с упоминанием суммы.

    Returns:
        float: Чистое число.
    """
    # 1. Очищаем число от пробелов (12 000 -> 12000)
    clean_text = re.sub(r'(\d)\s+(?=\d)', r'\1', text)

    # 2. Ищем число и возможный суффикс (р, тр)
    # Группа 1: цифры, Группа 2: суффикс
    match = re.search(r'(\d+)\s*(тр|р|т\.р|к)?', clean_text.lower())

    if not match:
        return 0.0

    value = float(match.group(1))
    suffix = match.group(2)

    if suffix in ['тр', 'т.р', 'к']:
        return value * 1000
    return value


def extract_date(text: str) -> Optional[str]:
    """Ищет дату в формате (DD-MM-YYYY)."""
    match = re.search(r'\((\d{2}-\d{2}-\d{4})\)', text)
    return f"({match.group(1)})" if match else None
