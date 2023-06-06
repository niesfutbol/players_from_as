import players_from_as as pfa


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
    }
    obtained = pfa.obtain_data_from_statistics(statistics)
    assert obtained == expected
