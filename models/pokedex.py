import json
from database import Database

class Pokedex(Database):
    def __init__(self):
        self.path = "./data/pokedex.json"
        self.data_pokedex = self.read_json()

    def clear_pokedex(self):
        """
        Function used to clear json pokedex.
        :return: ∅
        """
        with open(self.path, "w") as file:
            file.truncate()   # Use the truncate method to clear the file's content.

            # Rewrote "{}" in the empty file to avoid an error, in which the file was not recognized as a json format.
            json.dump({}, file)

    def add_pokemon(self, name):
        """Function that add a pokemon in data_pokedex"""
        self.data_pokedex[name] = all_pokemons.data_pokemons[name]

if __name__ == '__main__':
    from pokemon_dictionary import PokemonDictionary

    all_pokemons = PokemonDictionary()
    player_pokedex = Pokedex()
    player_pokedex.add_pokemon("Mewtwo")

    print(player_pokedex.data_pokedex)