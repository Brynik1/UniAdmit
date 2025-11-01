from dataclasses import dataclass
from enum import Enum

class DataMode(Enum):
    SAMPLE = "sample"      # Небольшой набор тестовых данных
    BULK = "bulk"         # Большой объем сгенерированных данных

@dataclass
class DataConfig:
    mode: DataMode
    batch_size: int = 1000  # Размер пачки для bulk-режима