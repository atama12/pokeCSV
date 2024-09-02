from ..Utility.Common import *
from .ItemCategory import ItemCategory
from typing import List

class ItemPocket(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/item-fling-effect/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def categories(self):
        array : List[ItemCategory] = [ItemCategory(json_data["name"]) for json_data in self._json_data["categories"]]
        return array
    
    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array
    
    