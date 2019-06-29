#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

parameters = {
  "jsonrpc": "2.0",
  "method": "host.get",
  "params": {
     "filter":{
        "host":[]}
     },
  "id": 1
}

print ('dict={}, method={}'.format(parameters, parameters['method']))
sstr = json.dumps(parameters)
print ('after------json dumps')
print ('str={}'.format(sstr))
print ('after------json loads')
jso = json.loads(sstr, encoding='utf-8')
print ('dict={}'.format(str(jso).encode('utf-8')))
print ('dict={}, method={}'.format(jso, jso['method']))
sstr22 = json.dumps(jso)
print ('str={}'.format(sstr22))


```
[root@cfBareos test]# python3 json_test.py 
dict={'jsonrpc': '2.0', 'method': 'host.get', 'params': {'filter': {'host': []}}, 'id': 1}, method=host.get
after------json dumps
str={"jsonrpc": "2.0", "method": "host.get", "params": {"filter": {"host": []}}, "id": 1}
after------json loads
dict=b"{'jsonrpc': '2.0', 'method': 'host.get', 'params': {'filter': {'host': []}}, 'id': 1}"
dict={'jsonrpc': '2.0', 'method': 'host.get', 'params': {'filter': {'host': []}}, 'id': 1}, method=host.get
str={"jsonrpc": "2.0", "method": "host.get", "params": {"filter": {"host": []}}, "id": 1}
[root@cfBareos test]# python json_test.py 
dict={'params': {'filter': {'host': []}}, 'jsonrpc': '2.0', 'method': 'host.get', 'id': 1}, method=host.get
after------json dumps
str={"params": {"filter": {"host": []}}, "jsonrpc": "2.0", "method": "host.get", "id": 1}
after------json loads
dict={u'jsonrpc': u'2.0', u'params': {u'filter': {u'host': []}}, u'method': u'host.get', u'id': 1}
dict={u'jsonrpc': u'2.0', u'params': {u'filter': {u'host': []}}, u'method': u'host.get', u'id': 1}, method=host.get
str={"jsonrpc": "2.0", "params": {"filter": {"host": []}}, "method": "host.get", "id": 1}
```
