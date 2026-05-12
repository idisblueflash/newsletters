import pytest
from dotenv import load_dotenv

load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--draft", required=True, help="Path to draft.md to evaluate")


@pytest.fixture(scope="session")
def draft_content(request):
    path = request.config.getoption("--draft")
    with open(path, encoding="utf-8") as f:
        return f.read()
