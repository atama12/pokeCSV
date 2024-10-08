
<div id="top"></div>

# PyPokeClasses

<p style="display: inline">

</p>

<p style="font-size : 16px">
  PyPokeClasses is a Python package that provides a class-based structure for accessing and interacting with PokeAPI's JSON data. It simplifies the process of making API requests and handling the returned data, allowing developers to focus on building applications with Pokémon-related data.
</p>

<!-- プロジェクト名を記載 -->

## Features
<ul>
  <li>
    Class-based access to various Pokémon entities from PokeAPI.
  </li>
  <li>
    Easy integration of PokeAPI into Python projects.
  </li>
  <li>
    Structured handling of API responses.
  </li>
  <li>
    Lightweight and flexible for various use cases.
  </li>
</ul>

## Installation

You can install this package using pip:

```python
pip install PyPokeClasses
```

## Usage

Here is an example of how to use PyPokeClasses to fetch and interact with Pokémon data:

```
from PyPokeClasses.Pokemon import Pokemon

# Initialize a Pokemon instance by name or ID
pikachu = Pokemon('pikachu')

# Access basic information
print(f"Name: {pikachu.name}")
print(f"Height: {pikachu.height}")
print(f"Weight: {pikachu.weight}")

# Access additional data
print(f"Base Experience: {pikachu.base_experience}")
print(f"Types: {[t.type.name for t in pikachu.types]}")
```

Thanks to this design, the class dynamically fetches and stores the data in object properties, allowing users to easily access and interact with PokeAPI data directly from the class instance. Moreover, code completion (autocomplete) for these properties is supported, which enhances the development experience by suggesting available Pokémon attributes and methods during coding.

![ダウンロード](https://github.com/user-attachments/assets/6968777b-1f4a-47c6-92f8-a29165f21fad)

<h2> Supported Entities</h2>

| Entities        | Classes                                                                      | Links |
| -------------| ----------                                                                | --------|
| Berries     |   Berry / BerryFirmness / BerryFlavor   | [Link](https://pokeapi.co/docs/v2#berries-section)
| Contests    | ContestType / ContestEffect / SuperContestEffect | [Link](https://pokeapi.co/docs/v2#contests-section)
| Encounters   | EncounterMethod / EncounterCondition / EncounterConditionValue | [Link](https://pokeapi.co/docs/v2#encounters-section)
| Evolution       | EvolutionChain / EvolutionTrigger | [Link](https://pokeapi.co/docs/v2#evolution-section)
| Games  | Generation / Pokedex / Version / VersionGroup | [Link](https://pokeapi.co/docs/v2#games-section)
| Items      | Item / ItemAttribute / ItemCategory / ItemFlingEffect / ItemPocket | [Link](https://pokeapi.co/docs/v2#items-section)
| Locations     | Location / LocationArea / PalParkArea / Region | [Link](https://pokeapi.co/docs/v2#locations-section)
| Machines     | Machine | [Link](https://pokeapi.co/docs/v2#machines-section)
| Moves     | MoveAilments / MoveBattleStyles / MoveCategory /MoveDamageClass / MoveLearnMethod / Moves / MoveTarget | [Link](https://pokeapi.co/docs/v2#moves-section)
| Pokemon     | Abilities / Characteristic / EggGroup / Genders / GrowthRate / Natures / PokeathlonStats / Pokemon / PokemonColors / PokemonForms / PokemonHabitats / PokemonShapes / PokemonSpecies / Stats / Types | [Link](https://pokeapi.co/docs/v2#locations-section)

## APIRefference

Each class within the package is mapped to the corresponding PokeAPI endpoint. Refer to the official <a href="https://pokeapi.co/">PokeAPI documentation</a> for details about the available data.

## LICENSE
This project is licensed under the MIT License - see the LICENSE file for details.
