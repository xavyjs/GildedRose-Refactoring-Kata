from typing import Protocol
from item import Item
from config import QUALITY_CONFIG
from quality_operation import decrease_item_quality, increase_item_quality

"""
    Contains
    1. ItemUpdater Abstraction with behaviors for to update sell_in and quality
    2. A DefaultItemUpdater to define default behaviors for 1
    3. For every Item Type a new ItemUpdater that overrides behavior of 2
    TO OVERRIDE DEFAULT BEHAVIOR FOLLOW THE SKELETON FROM 3
"""


class ItemUpdater(Protocol):
    def update_sell_in(self, item: Item) -> None:
        pass

    def update_quality(self, item: Item) -> None:
        pass


class DefaultItemUpdater:
    def update_sell_in(self, item: Item) -> None:
        item.sell_in = item.sell_in - 1

    def update_quality(self, item: Item) -> None:
        decrease_item_quality(item)
        if item.sell_in < 0:
            decrease_item_quality(item)


class AgedBrieItemUpdater(DefaultItemUpdater):
    def update_quality(self, item: Item) -> None:
        increase_item_quality(item)
        if item.sell_in < 0:
            increase_item_quality(item)


class BackstagePassesItemUpdater(DefaultItemUpdater):
    def update_quality(self, item: Item) -> None:
        increase_item_quality(item)
        if item.sell_in < 10:
            increase_item_quality(item)
        if item.sell_in < 5:
            increase_item_quality(item)
        if item.sell_in < 0:
            item.quality = QUALITY_CONFIG["MIN_QUALITY"]


class SulfurasItemUpdater(DefaultItemUpdater):
    def update_sell_in(self, item: Item) -> None:
        pass

    def update_quality(self, item: Item) -> None:
        pass


class ConjuredItemUpdater(DefaultItemUpdater):
    def update_quality(self, item: Item) -> None:
        decrease_item_quality(item, 2)
        if item.sell_in < 0:
            decrease_item_quality(item, 2)