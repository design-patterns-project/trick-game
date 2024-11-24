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

    # Pontuação inicial
    scores = {player.name: 0 for player in players}
    truco_level = 1  # Nível inicial do truco

    # Loop de jogo
    while not game.winner:
        current_player = game.players[game.current_turn]
        print(f"\nJogador atual: {current_player.name}")

        if isinstance(current_player, Player):
            print(f"\nÉ a sua vez, {current_player.name}.")
            print(f"\nCartas jogadas na mesa:")
            for player, card in zip(game.players, game.played_cards):
                print(f"- {player.name} jogou {card}")

            print(f"\nSua mão: {[f'{i+1}: {card}' for i, card in enumerate(current_player.hand)]}")
            action = input("Escolha sua ação (1 - Jogar Carta, 2 - Gritar Truco, 3 - Desistir): ")

            if action == "1":
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
                print(f"{current_player.name} gritou truco!")
                truco_level += 1
                if game.ask_truco(current_player):
                    print("Truco aceito! Apostas aumentaram.")
                else:
                    print("Truco recusado. Você ganhou esta rodada.")
                    scores[current_player.name] += truco_level * 2
                    game.reset_round()
                    continue

            elif action == "3":
                print(f"{current_player.name} desistiu do jogo.")
                game.winner = "Bots"
                break

            else:
                print("Ação inválida. Tente novamente.")
                continue

        else:
            # Turno do bot
            if game.should_bot_call_truco(current_player):
                print(f"{current_player.name} gritou truco!")
                truco_level += 1
                if game.ask_truco(current_player):
                    print("Truco aceito! Apostas aumentaram.")
                else:
                    print(f"{current_player.name} perdeu ao gritar truco!")
                    game.reset_round()
                    continue
            else:
                bot_card = current_player.play_card()
                game.played_cards.append(bot_card)
                print(f"{current_player.name} jogou {bot_card}.")

        # Verifica quem venceu o turno
        winner = game.determine_turn_winner()
        scores[winner.name] += truco_level
        print(f"\n{winner.name} venceu este turno!")
        print(f"Pontuações: {scores}")

        # Atualiza o turno
        game.switch_turn()

        # Checa se alguém atingiu a pontuação máxima
        if max(scores.values()) >= 12:  # Pontuação máxima do truco paulista
            game.winner = max(scores, key=scores.get)

    print(f"\nO jogo terminou! Vencedor: {game.winner}")

if __name__ == "__main__":
    main()
