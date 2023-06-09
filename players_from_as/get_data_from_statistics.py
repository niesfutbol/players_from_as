def obtain_data_from_statistics(statistics):
    expected = {
        "minutes": statistics["games"]["minutes"],
        "shots_total": statistics["shots"]["total"],
        "shots_on": statistics["shots"]["on"],
        "passes_total": statistics["passes"]["total"],
        "passes_key": statistics["passes"]["key"],
        "passes_accuracy": statistics["passes"]["accuracy"],
        "tackles_total": statistics["tackles"]["total"],
        "tackles_blocks": statistics["tackles"]["blocks"],
        "tackles_interceptions": statistics["tackles"]["interceptions"],
        "duels_total": statistics["duels"]["total"],
        "duels_won": statistics["duels"]["won"],
        "team_name": statistics["team"]["name"],
        "team_logo": statistics["team"]["logo"],
        "league_name": statistics["league"]["name"],
        "league_logo": statistics["league"]["logo"],
    }
    return expected


def obtain_data_from_player(player):
    expected = {
        "age": player["age"],
        "nationality": player["nationality"],
        "height": player["height"],
        "weight": player["weight"],
        "photo": player["photo"],
        "full_name": f"{player['firstname']} {player['lastname']}",
        "curp": f"{player['lastname'][0:2]}{player['firstname'][0]}{player['nationality'][0:2]}".upper(),
    }
    return expected


def get_player_info(player):
    return {
        **obtain_data_from_player(player["player"]),
        **obtain_data_from_statistics(player["statistics"][0]),
    }


def get_player_info_from_list(list_of_players):
    return {player["player"]["id"]: get_player_info(player) for player in list_of_players}
