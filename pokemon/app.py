from pokemon import Pokemon
from pokemon_type import WATER_TYPE, GRASS_TYPE, FIRE_TYPE, ROCK_TYPE
from trainer import PokemonTrainer
from battle_engine import BattleEngine
import moves

def create_trainer_1():
    rokko = Pokemon(
        species="Samurott",
        nickname="Rokko",
        pokemon_type=WATER_TYPE,
        health_points=100,
        moves=[
            moves.HYDRO_PUMP,
        ],
        level=50,
    )
    lancelot = Pokemon(
        species="Roserade",
        nickname="Lancelot",
        pokemon_type=GRASS_TYPE,
        health_points=100,
        moves=[
            moves.PETAL_DANCE,
        ],
        level=50,
    )
    mushishi = Pokemon(
        species="Arcanine",
        nickname="Mushishi",
        pokemon_type=FIRE_TYPE,
        health_points=100,
        moves=[
            moves.FLAMETHROWER,
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
            moves.PETAL_DANCE,
        ],
        level=50,
    )
    watson = Pokemon(
        species="Walrein",
        nickname="Watson",
        pokemon_type=WATER_TYPE,
        health_points=100,
        moves=[
            moves.HYDRO_PUMP,
        ],
        level=50,
    )
    seisma = Pokemon(
        species="Rhyperior",
        nickname="Seisma",
        pokemon_type=ROCK_TYPE,
        health_points=100,
        moves=[
            moves.ROCK_SLIDE,
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
