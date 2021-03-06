class Path(object):
    __slots__ = ["entries"]

    def __init__(self, entries=tuple()):
        self.entries = entries

    def append(self, other):
        new_path = self.entries
        for element in other.split('/'):
            if len(element) == 0:
                new_path = tuple()
            else:
                new_path = new_path + (element,)
        return Path(new_path)

    def lower(self):
        return "/" + "/".join(self.entries)

    def __hash__(self):
        return hash(self.entries)

    def __eq__(self, other):
        return self.entries == other.entries
