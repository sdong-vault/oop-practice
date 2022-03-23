
def validate_str(s: str):
    if s is not None and len(s) > 0:
        return s
    else:
        raise ValueError()


class PokemonTrainer:
    def __init__(self, name, pokemon, backpack):
        self.name = validate_str(name)
        self.pokemon = pokemon
        self.backpack = backpack
    
    def has_remaining_pokemon(self):
        for poke in self.pokemon:
            if not poke.fainted:
                return True
        return False

class PokemonType:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name

ELECTRIC_TYPE = PokemonType("electric")
WATER_TYPE = PokemonType("water")
GRASS_TYPE = PokemonType("grass")
FIRE_TYPE = PokemonType("fire")
ROCK_TYPE = PokemonType("rock")

class Pokemon:
    def __init__(self,
            species,
            nickname,
            pokemon_type,
            health_points,
            moves,
            level):
        self.__species = validate_str(species)
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


def create_trainer_1():
    rokko = Pokemon(
        species="Samurott",
        nickname="Rokko",
        pokemon_type=WATER_TYPE,
        health_points=100,
        moves=[
            "hydro pump"
        ],
        level=50,
    )
    lancelot = Pokemon(
        species="Roserade",
        nickname="Lancelot",
        pokemon_type=GRASS_TYPE,
        health_points=100,
        moves=[
            "petal dance"
        ],
        level=50,
    )
    mushishi = Pokemon(
        species="Arcanine",
        nickname="Mushishi",
        pokemon_type=FIRE_TYPE,
        health_points=100,
        moves=[
            "flamethrower"
        ],
        level=50,
    )
    trainer = PokemonTrainer(
        name="Alison",
        pokemon=[rokko, lancelot, mushishi],
        backpack={}
    )
    return trainer


def create_trainer_2():
    minato = Pokemon(
        species="Decidueye",
        nickname="Minato",
        pokemon_type=GRASS_TYPE,
        health_points=100,
        moves=[
            "leaf blade"
        ],
        level=50,
    )
    watson = Pokemon(
        species="Walrein",
        nickname="Watson",
        pokemon_type=WATER_TYPE,
        health_points=100,
        moves=[
            "ice beam"
        ],
        level=50,
    )
    seisma = Pokemon(
        species="Rhyperior",
        nickname="Seisma",
        pokemon_type=ROCK_TYPE,
        health_points=100,
        moves=[
            "earthquake"
        ],
        level=50,
    )
    trainer = PokemonTrainer(
        name="Susanna",
        pokemon=[minato, watson, seisma],
        backpack={}
    )
    return trainer


def main():
    unit_tests()

    trainer1 = create_trainer_1()
    trainer2 = create_trainer_2()

    turn_order = [trainer1, trainer2]
    turn_index = 0
    def increment_turn_order():
        return (turn_index + 1) % len(turn_order)
    def get_current_trainer():
        return turn_order[turn_index]

    while True:
        trainer = get_current_trainer()

        if not trainer.has_remaining_pokemon():
            print(f"Trainer {trainer.name} does not have anymore pokemon to fight!")
            print(f"Trainer {trainer.name} has lost the match!")
            turn_index = increment_turn_order()
            break

        print(f"It is {trainer.name}'s turn!")
        print(f"What would you like to do?")

        print(f"1. Attack")
        print(f"2. Forfeit")

        response = input()

        if response == "attack":
            print("attack!!!")
        else:
            print(f"Trainer {trainer.name} has forfeited the match!")
            print(f"Trainer {trainer.name} has lost the match!")
            turn_index = increment_turn_order()
            break

        turn_index = increment_turn_order()
    
    trainer = get_current_trainer()
    print(f"Trainer {trainer.name} has won!")



if __name__ == "__main__":
    main()
