class WordSlot:
    def __init__(self, row, col, dir, len=None):
        self.row = row
        self.col = col
        self.dir = dir
        self.len = len
        self.word = None

    def __repr__(self):
        return 'WordSlot[row={} col={} dir={} len={}]'.format(
            self.row, self.col, self.dir, self.len)

    def __eq__(self, other):
        print('WordSlot.__eq__')
        return (self.row == other.row) and (self.col == other.col) and (self.dir == other.dir)


a = WordSlot(1, 2, 'N')
b = WordSlot(1, 2, 'N')
print(a == b)
