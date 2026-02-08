from typing import List
from .base import BaseParser
from ..models import FinanceEntry, FinanceType
from .utils import extract_amount, extract_date

class SmartParser(BaseParser):
    """Парсер, работающий по принципу разделителя '|'."""

    def validate(self, content: str) -> bool:
        return "|" in content

    def parse(self) -> List[FinanceEntry]:
        if not self.source_path.exists():
            return []

        lines = self.source_path.read_text(encoding='utf-8').splitlines()
        results = []

        # Текущий контекст парсинга
        curr_type = FinanceType.EXPENSE
        curr_date = None
        curr_cat = "Общее"

        for line in lines:
            clean = line.strip()
            if not clean:
                continue

            # Контекст заголовков
            if clean.startswith("# "):
                curr_type = FinanceType.INCOME if "Доход" in clean else FinanceType.EXPENSE
                continue
            if clean.startswith("##"):
                curr_cat = clean.replace("#", "").strip()
                continue

            # Контекст даты
            found_date = extract_date(clean)
            if found_date:
                curr_date = found_date
                continue

            # Основная логика: Разделитель '|'
            if "|" in clean:
                parts = clean.split("|")
                # Чистим название от маркеров списка
                title = parts[0].strip("- [*] ").strip()
                # Извлекаем сумму из правой части
                amount = extract_amount(parts[1])

                if amount > 0:
                    results.append(FinanceEntry(
                        title=title or "Без названия",
                        amount=amount,
                        finance_type=curr_type,
                        category=curr_cat,
                        event_date=curr_date,
                        is_paid="[x]" in clean or "Оплачено" in curr_cat,
                        raw_text=clean
                    ))
        return results
