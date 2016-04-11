def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    method = environ['REQUEST_METHOD']
    print(method)
    return [b'<h1>Hello, web web</h1>']
