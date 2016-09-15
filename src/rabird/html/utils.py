import unicodedata

def get_text(element):
    return ''.join(element.itertext())

def get_numeric(element):
    text = get_text(element)
    text = unicodedata.normalize('NFKC', text)
    return float(text.strip().replace(",", ""))
