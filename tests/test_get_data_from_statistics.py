import json
import players_from_as as pfa


def test_get_player_info_from_list_from_json():
    f = open("tests/data/data_statisitcs_players_team_39_season_2022_page_2.json")
    players = json.load(f)
    obtained = pfa.get_player_info_from_list(players["response"])
    assert obtained[24888]["curp"] == "HWHKO", "Assert curp of Hwang Hee-Chan"


statistics = {
    "team": {
        "id": 50,
        "name": "Manchester City",
        "logo": "https://media-2.api-sports.io/football/teams/50.png",
    },
    "league": {
        "id": 39,
        "name": "Premier League",
        "country": "England",
        "logo": "https://media-3.api-sports.io/football/leagues/39.png",
        "flag": "https://media-2.api-sports.io/flags/gb.svg",
        "season": 2022,
    },
    "games": {
        "appearences": 35,
        "lineups": 35,
        "minutes": 3150,
        "number": None,
        "position": "Goalkeeper",
        "rating": "6.676470",
        "captain": False,
    },
    "substitutes": {"in": 0, "out": 0, "bench": 3},
    "shots": {"total": None, "on": None},
    "goals": {"total": 0, "conceded": 31, "assists": 1, "saves": 43},
    "passes": {"total": 1068, "key": 1, "accuracy": 26},
    "tackles": {"total": 3, "blocks": None, "interceptions": 1},
    "duels": {"total": 16, "won": 13},
    "dribbles": {"attempts": None, "success": None, "past": None},
    "fouls": {"drawn": 2, "committed": 1},
    "cards": {"yellow": 3, "yellowred": 0, "red": 0},
    "penalty": {"won": None, "commited": None, "scored": 0, "missed": 0, "saved": 0},
}

statistics_2 = {
    "team": {
        "id": 50,
        "name": "Manchester City",
        "logo": "https://media-3.api-sports.io/football/teams/50.png",
    },
    "league": {
        "id": 39,
        "name": "Premier League",
        "country": "England",
        "logo": "https://media-3.api-sports.io/football/leagues/39.png",
        "flag": "https://media-2.api-sports.io/flags/gb.svg",
        "season": 2022,
    },
    "games": {
        "appearences": 23,
        "lineups": 21,
        "minutes": 1849,
        "number": None,
        "position": "Defender",
        "rating": "7.021739",
        "captain": False,
    },
    "substitutes": {"in": 2, "out": 5, "bench": 8},
    "shots": {"total": 9, "on": 3},
    "goals": {"total": 2, "conceded": 0, "assists": 2, "saves": None},
    "passes": {"total": 1511, "key": 8, "accuracy": 61},
    "tackles": {"total": 23, "blocks": 10, "interceptions": 9},
    "duels": {"total": 104, "won": 70},
    "dribbles": {"attempts": 7, "success": 6, "past": None},
    "fouls": {"drawn": 8, "committed": 10},
    "cards": {"yellow": 2, "yellowred": 0, "red": 0},
    "penalty": {"won": None, "commited": None, "scored": 0, "missed": 0, "saved": None},
}

player = {
    "id": 626,
    "name": "J. Stones",
    "firstname": "John",
    "lastname": "Stones",
    "age": 29,
    "birth": {"date": "1994-05-28", "place": "Barnsley", "country": "England"},
    "nationality": "England",
    "height": "188 cm",
    "weight": "80 kg",
    "injured": False,
    "photo": "https://media-3.api-sports.io/football/players/626.png",
}

player_2 = {
    "id": 617,
    "name": "Ederson",
    "firstname": "Ederson",
    "lastname": "Santana de Moraes",
    "age": 30,
    "birth": {"date": "1993-08-17", "place": "Osasco", "country": "Brazil"},
    "nationality": "Brazil",
    "height": "188 cm",
    "weight": "86 kg",
    "injured": False,
    "photo": "https://media-3.api-sports.io/football/players/617.png",
}

full_player = {"player": player, "statistics": [statistics_2]}
full_player_2 = {"player": player_2, "statistics": [statistics]}


def test_obtain_data_from_statistics():
    expected = {
        "minutes": 3150,
        "shots_total": None,
        "shots_on": None,
        "passes_total": 1068,
        "passes_key": 1,
        "passes_accuracy": 26,
        "tackles_total": 3,
        "tackles_blocks": None,
        "tackles_interceptions": 1,
        "duels_total": 16,
        "duels_won": 13,
        "team_name": "Manchester City",
        "team_logo": "https://media-2.api-sports.io/football/teams/50.png",
        "league_name": "Premier League",
        "league_logo": "https://media-3.api-sports.io/football/leagues/39.png",
    }
    obtained = pfa.obtain_data_from_statistics(statistics)
    assert obtained == expected
    expected = {
        "minutes": 1849,
        "shots_total": 9,
        "shots_on": 3,
        "passes_total": 1511,
        "passes_key": 8,
        "passes_accuracy": 61,
        "tackles_total": 23,
        "tackles_blocks": 10,
        "tackles_interceptions": 9,
        "duels_total": 104,
        "duels_won": 70,
        "team_name": "Manchester City",
        "team_logo": "https://media-3.api-sports.io/football/teams/50.png",
        "league_name": "Premier League",
        "league_logo": "https://media-3.api-sports.io/football/leagues/39.png",
    }
    obtained = pfa.obtain_data_from_statistics(statistics_2)
    assert obtained == expected


def test_obtain_data_from_player():
    expected = {
        "age": 29,
        "nationality": "England",
        "height": "188 cm",
        "weight": "80 kg",
        "photo": "https://media-3.api-sports.io/football/players/626.png",
        "full_name": "John Stones",
        "curp": "STJEN",
    }
    obtained = pfa.obtain_data_from_player(player)
    assert obtained == expected, "Assert the player info"


def test_get_player_info():
    obtained = pfa.get_player_info(full_player)
    expected = {
        "age": 29,
        "nationality": "England",
        "height": "188 cm",
        "weight": "80 kg",
        "photo": "https://media-3.api-sports.io/football/players/626.png",
        "full_name": "John Stones",
        "curp": "STJEN",
        "minutes": 1849,
        "shots_total": 9,
        "shots_on": 3,
        "passes_total": 1511,
        "passes_key": 8,
        "passes_accuracy": 61,
        "tackles_total": 23,
        "tackles_blocks": 10,
        "tackles_interceptions": 9,
        "duels_total": 104,
        "duels_won": 70,
        "team_name": "Manchester City",
        "team_logo": "https://media-3.api-sports.io/football/teams/50.png",
        "league_name": "Premier League",
        "league_logo": "https://media-3.api-sports.io/football/leagues/39.png",
    }
    assert obtained == expected, "Assert the full player info"


list_of_players = [full_player, full_player_2]


def test_get_player_info_from_list():
    obtained = pfa.get_player_info_from_list(list_of_players)
    expected = {
        "age": 29,
        "nationality": "England",
        "height": "188 cm",
        "weight": "80 kg",
        "photo": "https://media-3.api-sports.io/football/players/626.png",
        "full_name": "John Stones",
        "curp": "STJEN",
        "minutes": 1849,
        "shots_total": 9,
        "shots_on": 3,
        "passes_total": 1511,
        "passes_key": 8,
        "passes_accuracy": 61,
        "tackles_total": 23,
        "tackles_blocks": 10,
        "tackles_interceptions": 9,
        "duels_total": 104,
        "duels_won": 70,
        "team_name": "Manchester City",
        "team_logo": "https://media-3.api-sports.io/football/teams/50.png",
        "league_name": "Premier League",
        "league_logo": "https://media-3.api-sports.io/football/leagues/39.png",
    }
    assert obtained[626] == expected, "Assert the full player info from list"
    assert obtained[617]["minutes"] == 3150, "Assert minutos of Ederson"
    assert obtained[617]["curp"] == "SAEBR", "Assert curp of Ederson"
