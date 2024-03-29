import xml.etree.ElementTree as ET
from os import getcwd

sets=[('fire', 'train'), ('fire', 'trainval'), ('fire', 'val')]

classes = ["fire"]


def convert_annotation(year, image_id, list_file):
    in_file = open('fire/data/%s.xml'%(image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

for year, image_set in sets:
    image_ids = open('fire/%s_%s.txt'%(year, image_set)).read().strip().split('\n')
    list_file = open('%s_%s.txt'%(year, image_set), 'w')
    for image_id in image_ids:
        print (image_id[0:6])
        list_file.write('%s/fire/%s.jpg'%(wd, image_id[0:6]))
        convert_annotation(year, image_id[0:6], list_file)
        list_file.write('\n')
    list_file.close()

