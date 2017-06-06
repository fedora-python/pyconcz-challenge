import importlib

import pytest


def pytest_addoption(parser):
    parser.addoption("--module", action="store", default="build_order",
                     help="module to load function from")


@pytest.fixture
def module(request):
    name = request.config.getoption("--module")
    return importlib.import_module(name)
