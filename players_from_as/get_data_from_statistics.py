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
    }
    return expected
