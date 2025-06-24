from typing import Iterable
from item import Item
from config import ITEM_TYPES
from item_updater import (
    DefaultItemUpdater,
    AgedBrieItemUpdater,
    BackstagePassesItemUpdater,
    SulfurasItemUpdater,
    ConjuredItemUpdater
)


ITEM_UPDATERS = {
    ITEM_TYPES["AGED_BRIE"]: AgedBrieItemUpdater(),
    ITEM_TYPES["BACKSTAGE_PASSES"]: BackstagePassesItemUpdater(),
    ITEM_TYPES["SULFURAS"]: SulfurasItemUpdater(),
    ITEM_TYPES["CONJURED"]: ConjuredItemUpdater()
}


def update_quality(items: Iterable[Item]) -> None:
    for item in items:
        update_quality_single(item)


def update_quality_single(item: Item):
    item_updater = ITEM_UPDATERS.get(item.name, DefaultItemUpdater())
    item_updater.update_sell_in(item)
    item_updater.update_quality(item)