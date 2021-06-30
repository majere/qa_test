from xml.dom import minidom
import os
import sys


xml_file = minidom.parse('1.xml')
items = xml_file.getElementsByTagName('file')

for el in items:
    source = el.attributes['source_path'].value
    destination = el.attributes['destination_path'].value
    file = el.attributes['file_name'].value
    source = os.path.join(source, file)

    if os.path.isfile(source):
        print(f'Start copy {source}')
        if sys.platform == 'win32':
            cmd = f'copy {source} {destination}'
        else:
            cmd = f'cp {source} {destination}'
        os.system(cmd)
    else:
        print(f'Source "{source}" not found')
