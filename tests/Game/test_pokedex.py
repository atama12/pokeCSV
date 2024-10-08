import pytest
from unittest.mock import patch
from PyPokeClasses.Games import Pokedex
import json

# 1. モックデータをファイルから読み込むためのfixture
@pytest.fixture
def mock_response_data():
    with open('tests/Game/files/pokedex.json', 'r') as file:
        return json.load(file)


# 2. API問い合わせのステータスコードが200であることを確認するテスト
def test_api_connect():

    test1 = Pokedex(1)
    test2 = Pokedex(50000)
    # ステータスコードが200であることを確認
    assert test1.status_code == 200
    assert test2.status_code == 404

# 3. JSONデータのプロパティが正しく定義されていることを確認するテスト
@pytest.mark.parametrize("property_name, expected_value", [
    ("descriptions[0].description","Pok\u00e9dex National complet"),
    ("descriptions[0].language.name","fr"),
    ("descriptions[0].language.url","https://pokeapi.co/api/v2/language/5/"),
    ("id",1),
    ("is_main_series",True),
    ("name","national"),
    ("names[0].language.name","fr"),
    ("names[0].language.url","https://pokeapi.co/api/v2/language/5/"),
    ("names[0].name","National"),
    ("pokemon_entries[0].entry_number",1),
    ("pokemon_entries[0].pokemon_species.name","bulbasaur"),
    ("pokemon_entries[0].pokemon_species.url","https://pokeapi.co/api/v2/pokemon-species/1/"),
    ("region.name","aaa"),
    ("region.url","bbb"),
    ("version_groups[0].name","aaa2"),
    ("version_groups[0].url","bbb2"),
])
@patch('PyPokeClasses.Utility.Common.BaseModel.make_request')

def test_data_check(mock_make_request, property_name, expected_value, mock_response_data):
    mock_make_request.return_value = (mock_response_data)

    test_data = Pokedex(1)
    
    # プロパティが正しく設定されているか確認
    assert eval(f"test_data.{property_name}") == expected_value
    
# # 4. JSONデータの型が正しいことを確認するテスト
# @pytest.mark.parametrize("property_name, expected_type", [
#     ("name", str),
#     ("abilities", list),
#     ("types", list),
#     ("id", int),
# ])
# @patch('pokeAPI_Models.Utility.Common.BaseModel.make_request')
# def test_type_check(mock_make_request, property_name, expected_type, mock_response_data):
#     mock_make_request.return_value = (200, mock_response_data)

#     pikachu = Pokemon(1)
    
#     # 各プロパティの型が正しいことを確認
#     assert isinstance(getattr(pikachu, property_name), expected_type)