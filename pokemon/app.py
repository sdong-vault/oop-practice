from pokemon import Pokemon, WATER_TYPE, GRASS_TYPE, FIRE_TYPE, ROCK_TYPE
from trainer import PokemonTrainer
from battle_engine import BattleEngine

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
    battle_engine = BattleEngine(
        create_trainer_1(),
        create_trainer_2()
    )

    winner = None
    while winner is None:
        response = battle_engine.prompt_current_battler()

        battle_engine.resolve_action(response)

        battle_engine.increment_turn_order()

        winner = battle_engine.determine_winner()
    
    print(f"Trainer {winner.name} has won!")



if __name__ == "__main__":
    main()
