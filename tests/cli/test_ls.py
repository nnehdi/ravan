from typer.testing import CliRunner

from ravan.cli.ls import app


def test_ls():
    runner = CliRunner()
    result = runner.invoke(app)
    assert result.exit_code == 0
