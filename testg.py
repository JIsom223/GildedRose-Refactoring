import unittest

from gil_r import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        print(repr(items[0]))
        self.assertEqual("+5 Dexterity Vest", items[0].name)
    
    def test_foo2(self):
        items = [Item(name="Aged Brie", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        print(repr(items[0]))
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(21, items[0].quality)
        
    def test_foo3(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        print(repr(items[0]))
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(22, items[0].quality)
        self.assertEqual(9, items[0].sell_in)
        
    def test_foo4(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=47)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        print(repr(items[0]))
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-2, items[0].sell_in)
        
    def test_foo5(self):
        items = [Item(name="Aged Brie", sell_in=-1, quality=47)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        print(repr(items[0]))
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(50, items[0].quality)
        self.assertEqual(-2, items[0].sell_in)
    
    def test_foo6(self):
        items = [Item(name="Conjured Mana Cake", sell_in=-1, quality=35)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        print(repr(items[0]))
        self.assertEqual(34, items[0].quality)
        self.assertEqual(-2, items[0].sell_in)
        
    def test_foo7(self):
        items = [Item(name="Elixir of the Mongoose", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        print(repr(items[0]))
        self.assertEqual("Elixir of the Mongoose", items[0].name)
        self.assertEqual(19, items[0].quality)
        self.assertEqual(9, items[0].sell_in)
    
if __name__ == '__main__':
    unittest.main()