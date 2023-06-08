import json
import players_from_as as pfa


def test_get_player_and_id():
    f = open("tests/data/data_statisitcs_players_team_39_season_2022_page_2.json")
    players = json.load(f)
    obtained = pfa.get_player_and_id(players["response"])
    assert obtained[24888] == "Hwang Hee-Chan", "Assert name of Hwang Hee-Chan"
    assert obtained[149564] == "L. Cundle", "Assert name of L. Cundle"
