from ..Utility.Common import *
from .Moves import Moves
from typing import List

class MoveCategory(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/move-category/" + str(id))
        
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def moves(self):
        array : List[Moves] = [Moves(json_data["name"]) for json_data in self._json_data["moves"]]
        return array
    
    @property
    def descriptions(self):
        array : List[Description] = [Description(json_data) for json_data in self._json_data["descriptions"]]
        return array