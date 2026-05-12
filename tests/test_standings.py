from decimal import Decimal

from football_standings.standings import Match, calculate_standings, format_goal_average


def test_english_1974_rules_use_two_points_and_goal_average_tiebreaker():
    matches = [
        Match("Alpha", "Bravo", 2, 0),
        Match("Charlie", "Delta", 1, 0),
        Match("Charlie", "Echo", 1, 1),
        Match("Delta", "Alpha", 3, 0),
        Match("Bravo", "Echo", 1, 0),
    ]

    table = calculate_standings(matches)

    assert [(team.team, team.points) for team in table[:4]] == [
        ("Charlie", 3),
        ("Delta", 2),
        ("Alpha", 2),
        ("Bravo", 2),
    ]
    assert table[1].goal_average == Decimal("3")
    assert table[2].goal_average == Decimal("2") / Decimal("3")
    assert table[3].goal_average == Decimal("1") / Decimal("2")


def test_unbeaten_defence_sorts_first_on_equal_points():
    matches = [Match("Alpha", "Bravo", 1, 0), Match("Charlie", "Delta", 3, 1)]

    table = calculate_standings(matches)

    assert [team.team for team in table[:2]] == ["Alpha", "Charlie"]
    assert format_goal_average(table[0]) == "inf"
    assert format_goal_average(table[1]) == "3.000"
