import pytest
from TarjanPlanner.graph_utils import build_graph, find_optimized_route
from TarjanPlanner.io_utils import load_data
from TarjanPlanner.transport_utils import load_transport_modes


@pytest.fixture
def setup_data():
    relatives = load_data("data/relatives.csv")
    transport_modes = load_transport_modes("data/transport_modes.json")
    return relatives, transport_modes


def test_build_graph(setup_data):
    relatives, transport_modes = setup_data
    graph = build_graph(relatives, transport_modes, criterion="time")

    # Ensure all relatives and the random start are added as nodes
    assert len(graph.nodes) == 11  # 10 relatives + 1 random start

    # Check if there are edges between nodes
    assert len(graph.edges) > 0  # There should be some connections


def test_find_optimized_route(setup_data):
    relatives, transport_modes = setup_data
    graph = build_graph(relatives, transport_modes, criterion="time")

    start = "Relative_1"
    end = "Relative_5"
    path, cost, time, distance = find_optimized_route(graph, start, end, "time")

    # Check that a path is returned
    assert path is not None
    assert len(path) > 0

    # Verify non-zero cost, time, and distance
    assert cost > 0
    assert time > 0
    assert distance > 0
