class MetaURLBuilder(type):
    def __new__(cls, name, bases, attrs):

        attrs["__slots__"] = (
                    "built_url",
                    "__base",
                    "__endpoint_list",
                )
        required_attrs = [
                "get_built_urls", 
                "get_base", 
                
                "set_base",
                "set_endpoints"
                ]

        for attr in required_attrs:
            if attr not in attrs:
                raise AttributeError(f"Missing required attr {attr}")
 
        return super().__new__(cls,name,bases,attrs)



class URLBuilder(metaclass=MetaURLBuilder):

    def __init__(self, base=None, endpoint_list:list[str]=[]) -> None:
        self.built_url = []
        self.__base = base 
        self.__endpoint_list = endpoint_list


    def build(self):
        for path in self.__endpoint_list:
            self.built_url.append(f"{self.__base}{path}")

    def get_built_urls(self)->list:
        return self.built_url
    def get_base(self)->str:
        return self.__base
    def get_endpoints(self)->list:
        return self.__endpoint_list

    def set_base(self, base:str)->None:
        self.__base = base
    def set_endpoints(self, endpoint:list)->None:
        self.__endpoint_list = endpoint
