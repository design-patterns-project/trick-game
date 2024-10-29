from characters.models.player import Player
from designs_patterns.factory.factories.bot_factory import BotFactory
from designs_patterns.factory.factories.deck_factory import DeckFactory
from designs_patterns.factory.factories.game_factory import GameFactory
from designs_patterns.factory.factories.player_factory import PlayerFactory
from designs_patterns.mediator.game_mediator import GameMediator
from designs_patterns.observer.observer import GameObserver
from designs_patterns.singleton.game_manager import GameManager


def main():
    # Criando a instância do GameManager
    game_manager = GameManager()
    game_manager.setup_game()

    # Criando o Mediator
    game_mediator = GameMediator()

    # Solicitando o nome do jogador humano
    human_player_name = input("Digite o seu nome: ")

    # Usando PlayerFactory para criar o jogador humano
    player_factory = PlayerFactory()
    player1 = player_factory.create(human_player_name)  # Nome do jogador humano

    # Usando BotFactory para criar bots
    bot_factory = BotFactory()
    players = [player1] + [bot_factory.create(f"Bot {i}") for i in range(1, 4)]  # Cria 3 bots

    # Registrando jogadores no Mediator
    for player in players:
        game_mediator.register_player(player)

    # Criando e embaralhando o baralho
    deck_factory = DeckFactory()
    deck = deck_factory.create()
    deck.shuffle()

    # Criando e iniciando o jogo com o Mediator
    game_factory = GameFactory()
    game = game_factory.create(players, game_mediator)  # Passando os jogadores corretamente

    # Criando um observador e registrando no jogo
    game_observer = GameObserver()
    game.attach(game_observer)

    # Iniciando o jogo
    game.start_game()

    # Loop de jogo
    while not game.winner:
        current_player = game.players[game.current_turn] 

        if isinstance(current_player, Player):
            print(f"\nÉ a sua vez, {current_player.name}.")
            action = input("Escolha sua ação (1 - Jogar Carta, 2 - Gritar Truco, 3 - Desistir): ")

            if action == "1":
                print(f"Sua mão: {[str(card) for card in current_player.hand]}")
                try:
                    card_index = int(input("Escolha o número da carta para jogar: ")) - 1
                    if 0 <= card_index < len(current_player.hand):
                        card = current_player.hand.pop(card_index)
                        game.played_cards.append(card)
                        print(f"{current_player.name} jogou {card}.")
                    else:
                        print("Escolha inválida. Tente novamente.")
                        continue
                except ValueError:
                    print("Por favor, insira um número válido.")
                    continue

            elif action == "2":
                current_player.call_truco()
                print(f"{current_player.name} gritou truco!")
            elif action == "3":
                print(f"{current_player.name} desistiu do jogo.")
                game.winner = "Bots"  
                break
            else:
                print("Ação inválida. Tente novamente.")
                continue
        else:
            # Turno do bot
            bot_card = current_player.play_card() 
            game.played_cards.append(bot_card)
            print(f"{current_player.name} jogou {bot_card}.")

        game.check_winner()  
        game.switch_turn()  

    print(f"O jogo terminou! Vencedor: {game.winner}")

if __name__ == "__main__":
    main()
