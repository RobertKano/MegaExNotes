from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional


class FinanceType(str, Enum):
    INCOME = "income"     # Доход
    EXPENSE = "expense"   # Расход
    DEBT = "debt"         # Долг (входящий или исходящий)


class FinanceEntry(BaseModel):
    """Универсальная модель финансовой записи.

    Используется для хранения как запланированных трат,
    так и уже совершенных операций из секции 'Оплачено'.
    """
    title: str = Field(..., description="Название (например, 'ЗП' или 'Стиралка')")
    amount: float = Field(..., description="Сумма в числовом представлении")
    finance_type: FinanceType = Field(..., description="Категория: доход, расход или долг")

    # Дата в строгом формате (29-01-2026)
    event_date: Optional[str] = Field(
        None,
        pattern=r"\(\d{2}-\d{2}-\d{4}\)",
        description="Дата операции в скобках"
    )

    category: str = Field("Общее", description="Подкатегория (быт, люди, и т.д.)")
    is_paid: bool = Field(False, description="Флаг: совершена ли операция (из секции Оплачено)")
    raw_text: str = Field(..., description="Оригинальная строка из md-файла для отладки")

    class Config:
        """Настройки Pydantic для корректной работы с Enum."""
        use_enum_values = True


class Task(BaseModel):
    """Задача или напоминание."""
    text: str
    is_completed: bool = False
    priority: int = 0  # !!! = 3, !! = 2, ! = 1
    due_date: Optional[str] = None


class Birthday(BaseModel):
    """Запись о днях рождения."""
    day_month: str  # "15 02"
    name: str
    has_gift_sent: bool = False


