class HttpRequest :
    def __init__(self , data) :
        self.method = None 
        self.uri = None
        self.http_version = '1.1'
        self.body = None
        self.parse(data)
    def parse(self , data) :
        data = data.decode()
        # print(data)
        lines = data.split('\r\n')
        words = lines[0].split(" ")
        self.method = words[0]
        if len(words) > 0 :
            self.uri = words[1]
        if len(words) > 1 :
            self.http_version = words[2]
        if not lines[-2] :
            self.body = lines[-1].split("&")
