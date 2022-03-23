
class Pokemon:
    def __init__(self, species, nickname, pokemon_type, health_points, moves, level):
        self.__check_species_not_null(species)
        self.nickname = nickname

        self.pokemon_type = pokemon_type
        self.level = level
        self.moves = moves

        self.health_points = health_points
        self.max_health_points = health_points

        self.fainted = False
    
    def __check_species_not_null(self, species):
        if species is not None:
            self.__species = species
        else:
            raise ValueError()
    
    def attack(self, pokemon, move):
        if move not in self.moves:
            print(f"{self.name} tried to use {move} but doesn't know it!")
        print(f"{self.name} used {move} on {pokemon.name}")
    
    def lose_hp(self, amount):
        if self.health_points - amount <= 0:
            self.health_points = 0
            self.fainted = True
        else:
            self.health_points -= amount
    
    def gain_hp(self, amount):
        if self.health_points == 0:
            self.fainted = False

        if self.health_points + amount >= self.max_health_points:
            self.max_health_points += amount
        else:
            self.health_points += amount
    
    @property
    def name(self):
        if self.nickname is None or len(self.nickname) == 0:
            return self.__species
        return self.nickname

    @staticmethod
    def which_pokemon_is_stronger(pokemon1, pokemon2):
        if pokemon1.level > pokemon2.level:
            return pokemon1
        else:
            return pokemon2


def main():
    sparky = Pokemon(
        species="Pikachu",
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
    # sparky.__nickname = "poop"  # don't want randos to set nickname randomly
    # print(sparky.nickname)      # still allow randos to get nickname

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

    # print(speedy.nickname)
    # print(Pokemon.which_pokemon_is_stronger(sparky, speedy).nickname)

    sparky.attack(speedy, "thunderbolt")

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
