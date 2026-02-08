from abc import ABC, abstractmethod
from typing import Any, List
from pathlib import Path


class BaseParser(ABC):
    """Абстрактный базовый класс для всех парсеров проекта.

    Этот класс определяет интерфейс, который должны реализовывать все
    конкретные парсеры проекта.
    """
    def __init__(self, source_path: Path):
        """Инициализация парсера.

        Args:
            source_path (Path): Путь к файлу или директории для парсинга
        """
        self.source_path = source_path

    @abstractmethod
    def parse(self) -> List[Any]:
        """Основной метод для извлечения данных.

        Returns:
            List[Any]: Список извлеченных данных.
        """
        pass

    @abstractmethod
    def validate(self, content: str) -> bool:
        """Проверка структуры контента перед парсингом.

        Args:
            content (str): Содержимое файла для проверки.

        Returns:
            bool: True если структура корректна, иначе False
        """
        pass
