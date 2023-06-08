def get_player_and_id(players):
    return {player["player"]["id"]: player["player"]["name"] for player in players}
