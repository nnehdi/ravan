from typer.testing import CliRunner

from ravan.cli.reflect import app


def test_reflect():
    runner = CliRunner()
    result = runner.invoke(app)
    assert result.stdout is not None
