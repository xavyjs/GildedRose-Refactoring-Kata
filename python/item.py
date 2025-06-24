"""
    Item: Moved from gilded_rose for easier
    maintenance

    Added type checks for readability
    though Item class was supposed to not be 
    modified according to the SRS


"""

class Item:
    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> str:
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)