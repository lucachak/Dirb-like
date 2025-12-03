'''
class meant to handle the request and retrieve the info
'''


import http.client as hc

class MetaConnectionHandler(type):

    def __new__(cls, name, bases, attrs):

        attrs["__slots__"] = (
                "__url",
                )
        
        required_attrs = [
                "get_client", 
                "set_client", 
                "get_url", 
                "set_url"
                ]

        try:
            for attr in required_attrs:
                if attr not in attrs:
                    raise NotImplementedError(f"""
                                    this attribute {attr} was not implemented
                                    """)
        except NotImplementedError as e:
            print(e)            
        return super().__new__(cls, name, bases, attrs)












class ConnectionHandler(metaclass=MetaConnectionHandler):

    def __init__(self, url:str) -> None:

        self.__url = self.url_parser(url.lower())
        


    #getters
    def get_url(self):
        return self.__url

    def get_client(self)->hc.HTTPConnection|None:
        return self.__client if not None else "no client yet..."

    #setters
    def set_client(self, client:hc.HTTPConnection) -> None:
        self.__client = client

    def set_url(self, url:str) -> None:
        self.__url = url

    
    def url_parser(self, url:str)->list[str]:
       
        url_break =url.split(":")

        conn_type = url_break[0]
        base_uri = (url_break[1])[2:]
        port = (url_break[2][0:4]).strip("/")
        path_args = url_break[2][4:]


        return [conn_type, base_uri, port, path_args]



    def connect(self):


        try:

            if self.__url[0] == "http":
                conn = hc.HTTPConnection(
                        self.__url[1],
                        int(self.__url[2])
                        )
                conn.request("GET", "/Api/products/")
                response = conn.getresponse()

                print(response.status, response.reason)

                print(
                        response
                        .read()
                        .decode('utf-8')
                        )
                conn.close()

            elif self.__url[0] == "https":
                conn = hc.HTTPSConnection(
                        self.__url[1],
                        int(self.__url[2])
                        )
                conn.request("GET", "/Api/products/")


                conn.close()
        except ValueError as e:
            print("not connected")
