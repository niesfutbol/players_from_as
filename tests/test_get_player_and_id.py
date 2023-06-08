import json
import players_from_as as pfa


def test_get_player_and_id():
    f = open("tests/data/data_statisitcs_players_team_39_season_2022_page_2.json")
    players = json.load(f)
    obtained = pfa.get_player_and_id(players["response"])

