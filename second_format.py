import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()
from collections import Counter


def get(filename: str, top_size: int, min_word_len: int) -> str:
    all_words = []
    open_file = root
    find_file = open_file.findall("channel/item")
    for article in find_file:
        words = article.find("description").text.lower().split()
        for word in words:
            if len(word) > min_word_len:
                all_words.append(word)
    counter = Counter(all_words)
    sorted_list = counter.most_common(10)
    return f"топ {top_size} самые часто используемые слова:{sorted_list}"

print(get("newsafr.xml", 10, 6))

  