import xml.etree.ElementTree as ET
tree = ET.parse('node_data.xml')
root = tree.getroot()
root.tag
root.attrib

for child in root:
    xyappend = [child.attrib['name']]
    for v in child:
        if v.tag == 'posx':
            xyappend.append(int(v.text))
        elif v.tag == 'posy':
            xyappend.append(int(v.text))
    print(xyappend)   
