
class Table(object):
    def __init__(self, element):
        self._element = element

    @property
    def element(self):
        return self._element

    @property
    def headers(self):
        return self.root.findall(".//tbody/tr[1]/th")

    @property
    def row_count(self):
        count = len(self.root.findall(".//tbody/tr"))
        if len(self.headers) > 0:
            count -= 1

        return count

    @property
    def col_count(self):
        elements = self.root.findall(".//tbody/tr[1]/td")
        if len(elements) <= 0:
            elements = self.headers

        return len(elements)

    def get_row(self, index):
        index += 1
        if len(self.headers) > 0:
            index += 1

        return self.root.findall(".//tbody/tr[%s]/td" % index)

    def get_col(self, index):
        index += 1
        start_pos = 0
        if len(self.headers) > 0:
            start_pos = 1

        return self.root.findall(".//tbody/tr/td[%s]" % index)[start_pos:]

    def get(self, row, col):
        return self.get_row(row)[col]
