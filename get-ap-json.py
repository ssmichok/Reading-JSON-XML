#!/usr/bin/env python
from urllib.request import Request, urlopen
import json
req = Request('http://172.18.98.98:8080/api/running/configure-tacacs/east-CSR03')
req.add_header('Authorization', 'Basic YWRtaW46YWRtaW4=')
req.add_header('Accept', 'application/vnd.yang.data+json')
response = urlopen(req)
response_string = response.read().decode('utf-8')
# print(response_string)
json_object = json.loads(response_string)
print(json.dumps(json_object, sort_keys=True, indent=4))
oper = json_object['configure-tacacs:configure-tacacs']
for key,val in oper['operations'].items():
    print('keys: ' + key + ' url: ' + val)
print('this is name of the service: ' + oper['name'])
print('this is name of the region: ' + oper['region'])
response.close()
