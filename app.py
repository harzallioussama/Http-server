import os

from tcpServer import TcpServer
from httprequest import HttpRequest

class HttpServer(TcpServer) :
    headers = {
        'Server' : 'HarousServre' ,
        'Content-Type' : 'text/html'
    }
    statusCode = {
        200 : 'Ok' ,
        201 : 'Ok' ,
        404 : 'Not Found' ,
        501 : 'Not Implemented'
    }
    def request_handler(self , data) :
        req = HttpRequest(data)
        # print(data.decode())
        try :
            handler = getattr(self , "%s_handler" % (req.method))
        except AttributeError :
            handler = self.http_501_handler
        response = handler(req)
        return response
    def GET_handler(self , req) :
        filename = req.uri[1:]
        response_line = response_body = b""
        print(os.path.exists(filename))
        if os.path.exists(filename) :
            response_line = self.response_line(statusCode = 200)
            with open(filename , 'rb') as f :
                response_body = f.read()
            # print(response_body)
        else :
            response_line = self.response_line(501)
            response_body = b"<body><html><h1>Not Implemented</h1></html></body>"
        response_header = self.response_header()
        blank_line = self.blank_line()
        return b"".join([response_line , response_header , blank_line , response_body])
    def POST_handler(self , req) :
        # print(req.body)
        filename = req.uri[1:]
        response_line = b""
        response_body = b""
        if os.path.exists(filename) :
            response_line = self.response_line(statusCode = 201) 
            with open(filename , 'rb') as f :
                response_body = f.read()
            # for e in req.body :
            #     response_body += b"<h1>%s \r\n" % e.encode()
            #     response_body += b"</h1>"
            # response_body += b"</html></body>"
            # response_body = req.body.encode()
        else :
            response_line = self.response_line(501)
            response_body = b"<body><html><h1>Not Implemented</h1></html></body>"
        response_header = self.response_header()
        blank_line = self.blank_line()
        print("finished")
        return b"".join([response_line , response_header , blank_line , response_body])
    def http_501_handler(self , req) :
        status = self.statusCode[501]
    def response_line(self , statusCode) :
        status = self.statusCode[statusCode]
        return ("HTTP/1.1 %s %s" % (statusCode , status)).encode()
    def response_header(self) :
        header = ""
        for h in self.headers :
            header += "%s : %s \r\n" % (h , self.headers[h])
        return header.encode()
    def blank_line(self) :
        return b"\r\n" 

httpserver = HttpServer()
httpserver.start()