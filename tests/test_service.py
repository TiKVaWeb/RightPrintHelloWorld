"""Тесты сервисного слоя."""

import pytest

from print_hello_world.dto import GreetingRequest
from print_hello_world.service import GreetingValidationError, build_greeting


def test_build_greeting_default_values() -> None:
    request = GreetingRequest(name="World", times=1, punctuation="!")
    response = build_greeting(request)
    assert response.lines == ["Hello, World!"]


def test_build_greeting_with_trimmed_name() -> None:
    request = GreetingRequest(name="  Nikita  ", times=1, punctuation="!")
    response = build_greeting(request)
    assert response.lines == ["Hello, Nikita!"]


def test_build_greeting_repeats_lines() -> None:
    request = GreetingRequest(name="Team", times=3, punctuation="?")
    response = build_greeting(request)
    assert response.lines == ["Hello, Team?"] * 3


@pytest.mark.parametrize("punctuation", [".", "!", "?"])
def test_build_greeting_accepts_supported_punctuation(punctuation: str) -> None:
    request = GreetingRequest(name="World", times=1, punctuation=punctuation)
    response = build_greeting(request)
    assert response.lines == [f"Hello, World{punctuation}"]


def test_build_greeting_rejects_empty_name() -> None:
    request = GreetingRequest(name="   ", times=1, punctuation="!")
    with pytest.raises(GreetingValidationError, match="Name must not be empty"):
        build_greeting(request)


def test_build_greeting_rejects_non_positive_times() -> None:
    request = GreetingRequest(name="World", times=0, punctuation="!")
    with pytest.raises(
        GreetingValidationError, match="Times must be greater than or equal to 1"
    ):
        build_greeting(request)


def test_build_greeting_rejects_unsupported_punctuation() -> None:
    request = GreetingRequest(name="World", times=1, punctuation=",")
    with pytest.raises(GreetingValidationError, match="Punctuation must be one of"):
        build_greeting(request)
