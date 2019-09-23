from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET
# import xml.dom.minidom
# import json
req = Request('http://172.18.98.98:8080/api/running/configure-tacacs/east-CSR03')
req.add_header('Authorization', 'Basic YWRtaW46YWRtaW4=')
# req.add_header('Accept', 'application/vnd.yang.data+json')
response = urlopen(req)
response_string = response.read().decode('utf-8')
root = ET.fromstring(response_string)
print('this is response string: ' + response_string)
print('this is root tag: ' + root.tag)
print('this is root attrib: ')
print(root.attrib)
print(root[0].text)
print(root[3][1].text)
for dev in root.iter('{http://com/example/configuretacacs}device'):
    print('DEVICE: ' + dev.text)
for ops in root.findall('{http://tail-f.com/ns/rest}operations'):
    my_op = ops.find('{http://com/example/configuretacacs}touch').text
    print('This is TOUCH Op: ' + my_op)
for child in root:
    print(child.tag, child.attrib, child.text)
    if child.tag in '{http://tail-f.com/ns/rest}operations':
        for grandchild in child:
            print(grandchild.tag, grandchild.attrib, grandchild.text)
response.close()
