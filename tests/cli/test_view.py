from typer.testing import CliRunner

from ravan.cli.view import app
from tests.common import create_one_session, memory_engine  # noqa: F401


def test_view(create_one_session):  # noqa: F811
    runner = CliRunner()
    result = runner.invoke(app, ["1"])
    assert result.exit_code == 0
