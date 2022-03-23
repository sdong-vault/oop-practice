
class Pokemon:
    POKEMON_SPECIES_NAME = "Pokemon pokemon"

    def __init__(self, species_name, nickname, pokemon_type, health_points, moves, level):
        self.species_name = species_name
        self.__check_nickname_not_null(nickname)
        self.pokemon_type = pokemon_type
        self.health_points = health_points
        self.moves = moves
        self.level = level
    
    def attack(self, move_index):
        print(f"{self.__nickname} used {self.moves[move_index]}")
    
    def __check_nickname_not_null(self, nickname):
        if nickname is not None:
            self.__nickname = nickname
        else:
            raise ValueError()
    
    @property
    def nickname(self):
        return f"$$$ {self.__nickname} $$$"

    @staticmethod
    def which_pokemon_is_stronger(pokemon1, pokemon2):
        if pokemon1.level > pokemon2.level:
            return pokemon1
        else:
            return pokemon2


def main():
    sparky = Pokemon(
        species_name="Pikachu",
        nickname="Sparky",
        pokemon_type="electric",
        health_points=100,
        moves=[
            "thunder",
            "thunderbolt",
            "quick attack"
        ],
        level=50
    )
    sparky.__nickname = "poop"  # don't want randos to set nickname randomly
    print(sparky.nickname)      # still allow randos to get nickname
    # sparky.attack(speedy, "thunderbolt")

    speedy = Pokemon(
        "Pikachu",
        "Speedy",
        "electric",
        34,
        [
            "thundershock",
            "quick attack"
        ],
        25
    )
    speedy.attack(0)

    print(speedy.nickname)

    print(Pokemon.which_pokemon_is_stronger(sparky, speedy).nickname)


    """
    Pokemon can have...
    name
    health
    type
    HP / PP
    moves
    level

    attack
    defend
    faint
    cry (make a noise)
    """


if __name__ == "__main__":
    main()
