import util
import pokemon_type

class PokemonMove:
    def __init__(self,
            name: str,
            pokemon_type: pokemon_type.PokemonType,
            base_damage: int,
            accuracy: int = 100):
        self.name = util.validate_str(name)
        self.pokemon_type = pokemon_type
        self.base_damage = base_damage
        self.accuracy = accuracy

THUNDERBOLT = PokemonMove("Thunderbolt", pokemon_type.ELECTRIC_TYPE, 80)
HYDRO_PUMP = PokemonMove("Hydro Pump", pokemon_type.WATER_TYPE, 100)
PETAL_DANCE = PokemonMove("Petal Dance", pokemon_type.GRASS_TYPE, 100)
FLAMETHROWER = PokemonMove("Flamethrower", pokemon_type.FIRE_TYPE, 80)
ROCK_SLIDE = PokemonMove("Rock Slide", pokemon_type.ROCK_TYPE, 100)
