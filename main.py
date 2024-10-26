from characters.models.card import Card
from designs_patterns.factory.factories.deck_factory import DeckFactory
from designs_patterns.factory.factories.game_factory import GameFactory
from designs_patterns.factory.factories.player_factory import PlayerFactory
from designs_patterns.factory.factories.round_factory import RoundFactory
from designs_patterns.mediator.game_mediator import GameMediator
from designs_patterns.singleton.game_manager import GameManager

def main():
    # Criando a instância do GameManager
    game_manager = GameManager()
    game_manager.setup_game()

    # Criando o Mediator
    game_mediator = GameMediator()

    # Criando jogadores
    player_factory = PlayerFactory()
    player1 = player_factory.create("Jogador 1")
    player2 = player_factory.create("Jogador 2")
    
    # Registrando jogadores no Mediator
    game_mediator.register_player(player1)
    game_mediator.register_player(player2)
    
    # Criando e embaralhando o baralho
    deck_factory = DeckFactory()
    deck = deck_factory.create()
    deck.shuffle()
    
    # Criando e iniciando o jogo com o Mediator
    game_factory = GameFactory()
    game = game_factory.create([player1, player2], game_mediator)
    game.start_game()
    
    # Criando e iniciando a primeira rodada com o Mediator
    round_factory = RoundFactory()
    round1 = round_factory.create([player1, player2], game_mediator)
    round1.start_round()

    # Simulando a conclusão de turnos
    player1.play_card(Card("A", "Copas"))
    player2.play_card(Card("2", "Copas"))

if __name__ == "__main__":
    main()
