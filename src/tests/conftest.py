import sys
import os

# Получаем абсолютный путь к папке src
# Мы берем путь текущего файла (conftest.py), поднимаемся на два уровня вверх и заходим в src
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))

if root_path not in sys.path:
    sys.path.insert(0, root_path)

print(f"\n[DEBUG] PYTHONPATH updated with: {root_path}")
