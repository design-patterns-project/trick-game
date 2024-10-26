from designs_patterns.factory.factories.deck_factory import DeckFactory
from designs_patterns.factory.factories.game_factory import GameFactory
from designs_patterns.factory.factories.player_factory import PlayerFactory
from designs_patterns.factory.factories.round_factory import RoundFactory


if __name__ == "__main__":
    player_factory = PlayerFactory()
    player1 = player_factory.create("Jogador 1")
    player2 = player_factory.create("Jogador 2")
    
    deck_factory = DeckFactory()
    deck = deck_factory.create()
    deck.shuffle()
    
    game_factory = GameFactory()
    game = game_factory.create([player1, player2])
    game.start_game()
    
    round_factory = RoundFactory()
    round1 = round_factory.create([player1, player2])
    round1.start_round()
