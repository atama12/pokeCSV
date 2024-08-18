from Models.Utility.Common import *
from typing import List
class PokemonSpecies(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/pokemon-species/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def order(self):
        return int(self._json_data["order"])
    
    @property
    def gender_rate(self):
        return int(self._json_data["gender_rate"])
    @property
    def capture_rate(self):
        return int(self._json_data["capture_rate"])
    @property
    def base_happiness(self):
        return int(self._json_data["base_happiness"])
    @property
    def is_baby(self):
        return bool(self._json_data["is_baby"])
    @property
    def is_legendary(self):
        return bool(self._json_data["is_legendary"])
    
    @property
    def is_mythical(self):
        return bool(self._json_data["is_mythical"])
    
    @property
    def hatch_counter(self):
        return int(self._json_data["hatch_counter"])

    @property
    def has_gender_differences(self):
        return bool(self._json_data["has_gender_differences"])
    @property
    def forms_switchable(self):
        return bool(self._json_data["forms_switchable"])
    @property
    def growth_rate(self):
        return NamedAPIResource(self._json_data["growth_rate"])
    @property
    def pokedex_numbers(self):
        array : List[PokemonSpeciesDexEntry] = [ PokemonSpeciesDexEntry(json_data) for json_data in self._json_data["pokedex_numbers"]]
        return array
    @property
    def egg_groups(self):
        array : List[NamedAPIResource] = [ NamedAPIResource(json_data) for json_data in self._json_data["egg_groups"]]
        return array
    
    @property
    def color(self):
        return NamedAPIResource(self._json_data["color"])
    
    @property
    def shape(self):
        return NamedAPIResource(self._json_data["shape"])
    
    @property
    def evolves_from_species(self):
        return NamedAPIResource(self._json_data["evolves_from_species"])
    @property
    def evolution_chain(self):
        return APIResource(self._json_data["evolution_chain"])
    @property
    def habitat(self):
        return NamedAPIResource(self._json_data["habitat"])
    @property
    def generation(self):
        return NamedAPIResource(self._json_data["generation"])
    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array
    @property
    def pal_park_encounters(self):
        array : List[PalParkEncounterArea] = [PalParkEncounterArea(json_data) for json_data in self._json_data["pal_park_encounters"]]
        return array
    @property
    def flavor_text_entries(self):
        array : List[FlavorText] = [FlavorText(json_data) for json_data in self._json_data["flavor_text_entries"]]
        return array    
    @property
    def form_descriptions(self):
        array : List[Description] = [Description(json_data) for json_data in self._json_data["form_descriptions"]]
        return array
    @property
    def genera(self):
        array : List[Genus] = [Genus(json_data) for json_data in self._json_data["genera"]]
        return array
    @property
    def varieties(self):
        array : List[PokemonSpeciesVariety] = [PokemonSpeciesVariety(json_data) for json_data in self._json_data["varieties"]]
        return array
    
    
class Genus:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def genus(self):
        return str(self.__json_data["genus"])
    
    @property
    def language(self):
        return NamedAPIResource(self.__json_data["language"])    
    
class PokemonSpeciesDexEntry:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def entry_number(self):
        return int(self.__json_data["entry_number"])
    
    @property
    def pokedex(self):
        return NamedAPIResource(self.__json_data["pokedex"])
    
class PalParkEncounterArea:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def base_score(self):
        return int(self.__json_data["base_score"])
    @property
    def rate(self):
        return int(self.__json_data["rate"])
    @property
    def area(self):
        return NamedAPIResource(self.__json_data["area"])
    
class PokemonSpeciesVariety:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def is_default(self):
        return bool(self.__json_data["is_default"])

    @property
    def pokemon(self):
        return NamedAPIResource(self.__json_data["pokemon"])