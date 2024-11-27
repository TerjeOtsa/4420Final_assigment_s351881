import pytest
from TarjanPlanner.io_utils import load_data
from TarjanPlanner.graph_utils import generate_random_start
from geopy.distance import geodesic


def test_load_data():
    relatives = load_data("data/relatives.csv")
    assert len(relatives) == 10  # Ensure 10 relatives are loaded
    assert "coords" in relatives[0]  # Ensure coordinates are parsed


def test_generate_random_start():
    relatives = load_data("data/relatives.csv")
    random_start = generate_random_start(relatives, max_distance=5)

    # Ensure the random start is within 5 km of at least one relative
    close_relatives = [
        relative
        for relative in relatives
        if geodesic(random_start["coords"], relative["coords"]).km <= 5
    ]
    assert len(close_relatives) > 0  # At least one relative is within 5 km
