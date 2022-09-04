from xml.dom import minidom
import xml.etree.ElementTree as ET


def subir():
  myDoc = minidom.parse('./prueba.xml')

  items = myDoc.getElementsByTagName("item")

  #print(items[0].attributes['name'].value)

 
    
  tree = ET.parse('./prueba.xml')
  root = tree.getroot()

  print("/n/n --------ETREE-----------")
  for items in root:
      for item in items:
           print("Atributo name del item: ", item.attrib['name'])
           print("Contenido del item: ", item.text)

  data = ET.Element('data')

  items1 = ET.SubElement(data, 'items', {"name": "padre1"})
  items2 = ET.SubElement(data, 'items', {"name": "padre2"})

  item1 = ET.SubElement(items1, 'item', {"name": "item1"})
  item2 = ET.SubElement(items1, 'item', {"name": "item2"})

  item3 = ET.SubElement(items2, 'item', {"name": "item3"})
  item4 = ET.SubElement(items2, 'item', {"name": "item4"})

  item1.text = "item1ABC"
  item2.text = "item2ABC"
  item3.text = "item3ABC"
  item4.text = "item4ABC"

  myData = ET.tostring(data)
  file = open("./prueba2.xml", "wb")
  file.write(myData)

