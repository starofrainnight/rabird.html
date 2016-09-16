
class ElementXPathWrapper(object):
    def __init__(self, element):
        self._element = element

    def xpath(self, pattern):
        if hasattr(self._element, "xpath"):
            # Support lxml elements
            return self._element.xpath(pattern)
        elif hasattr(self._element, "xpath_find_all"):
            # Support rabird.selenium elements
            return self._element.xpath_find_all(pattern)
        elif hasattr(self._element, "findall"):
            # Support python ElementTree elements
            return self._element.findall(pattern)
        elif hasattr(self._element, "find_elements_by_xpath"):
            # Support selenium elements
            return self._element.find_elements_by_xpath(pattern)
        else:
            raise NotImplementedError("Unsupported element type!")

class Widget(object):
    def __init__(self, element):
        self._wrapper = ElementXPathWrapper(element)

    @property
    def element(self):
        return self._wrapper._element
