import pytest
import itertools as it
import networkx as nx
import hypernetx as hnx
import numpy as np


class TriLoop():
    """Example hypergraph with 2 two 1-cells and 1 2-cell forming a loop"""

    def __init__(self):
        A, B, C, D = 'A', 'B', 'C', 'D'
        AB, BC, ACD = 'AB', 'BC', 'ACD'
        self.edgedict = {AB: {A, B}, BC: {B, C}, ACD: {A, C, D}}
        self.hypergraph = hnx.Hypergraph(self.edgedict, name='TriLoop')


class Fish():
    """Example hypergraph with 2 two 1-cells and 1 2-cell forming a loop"""

    def __init__(self):
        A, B, C, D, E, F, G, H = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'
        AB, BC, ACD, BEH, CF, AG = 'AB', 'BC', 'ACD', 'BEH', 'CF', 'AG'
        self.edgedict = {AB: {A, B}, BC: {B, C}, ACD: {A, C, D}, BEH: {B, E, H}, CF: {C, F}, AG: {A, G}}
        self.hypergraph = hnx.Hypergraph(self.edgedict, name='Fish')


class SixByFive():
    """Example hypergraph with 6 nodes and 5 edges"""

    def __init__(self):
        mat = np.array([[1, 1, 1, 0, 0, 0], [1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 0], [1, 1, 1, 1, 0, 0]]).transpose()
        self.hypergraph = hnx.Hypergraph.from_numpy_array(mat)


@pytest.fixture
def triloop():
    return TriLoop()


@pytest.fixture
def fish():
    return Fish()


@pytest.fixture
def sixbyfive():
    return SixByFive()
