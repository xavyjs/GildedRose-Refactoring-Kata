# quality_operations.py
from item import Item
from config import QUALITY_CONFIG


def decrease_item_quality(item: Item, amount: int = 1) -> None:
    item.quality = max(item.quality - amount, QUALITY_CONFIG["MIN_QUALITY"])


def increase_item_quality(item: Item, amount: int = 1) -> None:
    item.quality = min(item.quality + amount, QUALITY_CONFIG["MAX_QUALITY"])