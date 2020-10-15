import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()
from collections import Counter

def get(doc):
  results = []
  open_file = root
  find_file = open_file.findall("channel/item")
  for result in find_file:
    first_result = result.find("description").text.lower().split()
    for second_result in first_result:
      if len(second_result) > 6:
        results.append(second_result)

  last_list = Counter(results)
  sorted_list = last_list.most_common(10)
  return f'топ 10 самые часто используемые слова:{sorted_list}'

print(get("newsafr.xml"))

  