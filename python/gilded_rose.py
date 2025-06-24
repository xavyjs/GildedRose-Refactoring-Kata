# -*- coding: utf-8 -*-

from typing import Iterable
from item import Item

"""
    Refactoring GluidedRose and Items Classes
    1. GluidedRose Class consists of only behavior and no data 
        members. So refactoring it to my 
        python function
    2. Item class is moved to a seperate file for 
        maintainability
    3. Adding type checking for better readability and
        maintenance
"""


def update_quality(items: Iterable[Item]):
    for item in items:
        if (
            item.name != "Aged Brie"
            and item.name != "Backstage passes to a TAFKAL80ETC concert"
        ):
            if item.quality > 0:
                if item.name != "Sulfuras, Hand of Ragnaros":
                    item.quality = item.quality - 1
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.name != "Aged Brie":
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality > 0:
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1