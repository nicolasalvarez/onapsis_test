Test
============

Installation
------------
Installing the project:
* $ mkvirtualenv onapsis_test
* (onapsis_test)$ pip install -r requirements.txt
* (onapsis_test)$ cd onapsis_test
* (onapsis_test)$ python setup.py develop

Execution
---------
Running it:
* (onapsis_test)$ pserve development.ini

Checking it's running:
* (onapsis_test)$ curl -I localhost:6543
HTTP/1.1 200 OK
Content-Length: 3779
Content-Type: text/html; charset=UTF-8
Date: Mon, 13 Nov 2017 12:03:59 GMT
Server: waitress

A script with some requests:
* $ bash api_requests_tests.sh

Testing
-------