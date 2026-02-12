"""Тесты CLI-адаптера."""

import pytest

from print_hello_world.cli import main


def test_cli_success(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main(["--name", "Nikita", "--times", "2", "--punctuation", "?"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.err == ""
    assert captured.out == "Hello, Nikita?\nHello, Nikita?\n"


def test_cli_returns_validation_error_for_blank_name(
    capsys: pytest.CaptureFixture[str],
) -> None:
    exit_code = main(["--name", "   "])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert "Validation error: Name must not be empty." in captured.err
    assert captured.out == ""


def test_cli_returns_validation_error_for_bad_punctuation(
    capsys: pytest.CaptureFixture[str],
) -> None:
    exit_code = main(["--punctuation", ","])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert "Validation error: Punctuation must be one of" in captured.err
    assert captured.out == ""


def test_cli_returns_argument_error_for_invalid_times(
    capsys: pytest.CaptureFixture[str],
) -> None:
    exit_code = main(["--times", "NaN"])
    captured = capsys.readouterr()
    assert exit_code == 2
    assert "Argument error: argument --times: invalid int value: 'NaN'" in captured.err
    assert captured.out == ""
