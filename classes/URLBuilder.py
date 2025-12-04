from typing import List
class MetaURLBuilder(type):
    def __new__(cls, name, bases, attrs):

        attrs["__slots__"] = (
                "__endpoint_list"
                )
        required_attrs = ["get_url_list", "set_url_list"]

        for attr in required_attrs:
            if attr not in attrs:
                raise AttributeError()
            
        return super().__new__(cls,name,bases,attrs)



class URLBuilder:

    def __init__(self, endpoint_list:list[str]) -> None:
        built_url = []

        if endpoint_list is not isinstance(endpoint_list,List):
            self.__endpoint_list = endpoint_list
        else:
            print("must be an list")


    def build(self):

        print(f"building with {self.__endpoint_list}")

