class helperFunc(object):
    def __init__(self, item):
        self.item = item
    def qualityMinusOne(self, item):
        if item.quality > 0:
            item.quality -= 1
    def qualityPlusOne(self, item):
        if item.quality < 50:
            item.quality += 1