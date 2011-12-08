Stupid simple JSONP proxy. Currently deployable to Google App Engine, but it's
all just plain old portable Python.

Request Parameters
==================

* callback - Name of the Javascript function to wrap around the response
* url      - URL of the JSON web service

Example
=======

http://jsonpme.appspot.com/?callback=foo&url=http://some.json.endpoint.here.com

returns --> 'foo({"key": "val"})'
