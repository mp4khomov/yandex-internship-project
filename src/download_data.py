"""
Скачивает датасет Online Retail II с UCI Machine Learning Repository.

Использование:
    python src/download_data.py

Файл попадает в data/online_retail_II.xlsx (~45 МБ).
"""

import os
import sys
from pathlib import Path

import requests

URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00502/online_retail_II.xlsx"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
TARGET_DIR = PROJECT_ROOT / "data"
TARGET_PATH = TARGET_DIR / "online_retail_II.xlsx"


def download() -> None:
    TARGET_DIR.mkdir(exist_ok=True)

    if TARGET_PATH.exists():
        print(f"Файл уже скачан: {TARGET_PATH}")
        return

    print(f"Скачиваю датасет с {URL} ...")
    response = requests.get(URL, stream=True, timeout=60)
    response.raise_for_status()

    total_mb = int(response.headers.get("content-length", 0)) / 1024 / 1024
    print(f"Размер: ~{total_mb:.1f} МБ")

    with open(TARGET_PATH, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            f.write(chunk)

    print(f"Готово. Файл сохранён: {TARGET_PATH}")


if __name__ == "__main__":
    try:
        download()
    except Exception as exc:
        print(f"Ошибка при скачивании: {exc}", file=sys.stderr)
        sys.exit(1)
