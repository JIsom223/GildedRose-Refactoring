from helper import helperFunc
class GildedRose(object):
    def __init__(self, items):
        self.items = items
  
    def update_quality(self):
        for item in self.items:
            helper = helperFunc(item)
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            if item.name == "Conjured Mana Cake":
                helper.qualityMinusOne(item)
                helper.qualityMinusOne(item)
            if item.sell_in < 0:
                if item.name == "+5 Dexterity Vest" or item.name == "Elixir of the Mongoose":
                    helper.qualityMinusOne(item)
                    helper.qualityMinusOne(item)
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = 0
                elif item.name == "Aged Brie":
                    helper.qualityPlusOne(item)
            else:
                if item.name == "+5 Dexterity Vest" or item.name == "Elixir of the Mongoose":
                    helper.qualityMinusOne(item)
                elif item.name == "Backstage passes to a TAFKAL80ETC concert" or item.name == "Aged Brie":
                    helper.qualityPlusOne(item)
                    if item.name == "Backstage passes to a TAFKAL80ETC concert" and item.sell_in < 6:
                        helper.qualityPlusOne(item)
                    if item.name == "Backstage passes to a TAFKAL80ETC concert" and item.sell_in < 11:
                        helper.qualityPlusOne(item)
            item.sell_in -= 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)