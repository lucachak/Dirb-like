'''
class meant to handle the request and retrieve the info
'''

from http.client import HTTPConnection


class MetaConnectionHandler(type):

    def __new__(cls, name, bases, attrs):

        attrs["__slots__"] = (
                "__client",
                "__url"
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
                    raise NotImplementedError(f"this attribute {attr} was not implemented")
        except NotImplementedError as e:
            print(e)
            
        return super().__new__(cls, name, bases, attrs)



class ConnectionHandler(metaclass=MetaConnectionHandler):

    def __init__(self, client:HTTPConnection, url:str) -> None:

        self.__client = client
        self.__url = url

    #getters
    def get_url(self)->str:
        return self.__url

    def get_client(self)->HTTPConnection:
        return self.__client

    #setters
    def set_client(self, client:HTTPConnection) -> None:
        self.__client = client

    def set_url(self, url:str) -> None:
        self.__url = url


    #main methods
    def request_using_URL(self):
        pass

