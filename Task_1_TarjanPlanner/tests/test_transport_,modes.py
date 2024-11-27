import pytest
from TarjanPlanner.graph_utils import build_graph
from TarjanPlanner.io_utils import load_data
from TarjanPlanner.transport_utils import load_transport_modes


@pytest.fixture
def setup_data():
    relatives = load_data("data/relatives.csv")
    transport_modes = load_transport_modes("data/transport_modes.json")
    return relatives, transport_modes


def test_transport_mode_preferences(setup_data):
    relatives, transport_modes = setup_data
    graph = build_graph(relatives, transport_modes, criterion="time")

    # Check that edges have the correct modes based on distance
    for edge in graph.edges:
        data = graph[edge[0]][edge[1]]
        distance = data["distance"]

        if distance <= 0.5:
            assert data["mode"] == "Walking"
        elif 0.5 < distance <= 2:
            assert data["mode"] == "Bicycle"
        elif 2 < distance <= 5:
            assert data["mode"] == "Bus"
        else:
            assert data["mode"] == "Train"
