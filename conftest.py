import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    return Mock(spec=Bun)


@pytest.fixture
def mock_ingredient():
    return Mock(spec=Ingredient)
