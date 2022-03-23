import util

class Pokemon:
    def __init__(self,
            species,
            nickname,
            pokemon_type,
            health_points,
            moves,
            level):
        self.__species = util.validate_str(species)
        self.nickname = nickname

        self.pokemon_type = pokemon_type
        self.level = level
        self.moves = moves

        self.health_points = health_points
        self.max_health_points = health_points
        self.fainted = False
    
    def attack(self, pokemon, move):
        if move not in self.moves:
            print(f"{self.name} tried to use {move} but doesn't know it!")
        print(f"{self.name} used {move} on {pokemon.name}")
    
    def lose_hp(self, amount):
        if amount < 0:
            self.gain_hp(amount * -1)

        if self.health_points - amount <= 0:
            self.health_points = 0
            self.fainted = True
        else:
            self.health_points -= amount
    
    def gain_hp(self, amount):
        if amount < 0:
            self.lose_hp(amount * -1)

        if self.health_points == 0:
            self.fainted = False

        if self.health_points + amount >= self.max_health_points:
            self.health_points = self.max_health_points
        else:
            self.health_points += amount
    
    @property
    def name(self):
        if self.nickname is None or len(self.nickname) == 0:
            return self.__species
        return self.nickname


def unit_tests():
    sparky = Pokemon(
        species="Pikachu",
        nickname="Sparky",
        pokemon_type=ELECTRIC_TYPE,
        health_points=100,
        moves=[
            "thunder",
            "thunderbolt",
            "quick attack"
        ],
        level=50
    )
    assert sparky.max_health_points == 100

    # partially lose health
    sparky.lose_hp(50)
    assert sparky.health_points == 50
    assert not sparky.fainted

    # lose health to faint
    sparky.lose_hp(50)
    assert sparky.health_points == 0
    assert sparky.fainted

    # keep losing health should still stay the same
    sparky.lose_hp(50)
    assert sparky.health_points == 0
    assert sparky.fainted

    # healing should revive pokemon
    sparky.gain_hp(50)
    assert sparky.health_points == 50
    assert not sparky.fainted

    # healing beyond the max hp should be capped
    sparky.gain_hp(100)
    assert sparky.health_points == 100
    assert not sparky.fainted


def main():
    unit_tests()


if __name__ == "__main__":
    main()
