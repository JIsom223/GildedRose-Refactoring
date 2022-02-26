import unittest

from gil_r import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item(name="Aged Brie", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("+5 Dexterity Vest", items[0].name)
        # self.assertEqual(10, items[0].sell_in)

        
if __name__ == '__main__':
    unittest.main()