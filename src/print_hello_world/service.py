"""Service layer with greeting domain logic."""

from typing import Final

from print_hello_world.dto import GreetingRequest, GreetingResponse

ALLOWED_PUNCTUATION: Final[frozenset[str]] = frozenset({"!", ".", "?"})


class GreetingValidationError(ValueError):
    """Ошибка валидации входных данных приветствия."""


def build_greeting(request: GreetingRequest) -> GreetingResponse:
    """Собрать приветствие на основе запроса."""
    normalized_name = request.name.strip()
    if not normalized_name:
        msg = "Name must not be empty."
        raise GreetingValidationError(msg)

    if request.times < 1:
        msg = "Times must be greater than or equal to 1."
        raise GreetingValidationError(msg)

    if request.punctuation not in ALLOWED_PUNCTUATION:
        allowed = ", ".join(sorted(ALLOWED_PUNCTUATION))
        msg = f"Punctuation must be one of: {allowed}."
        raise GreetingValidationError(msg)

    line = f"Hello, {normalized_name}{request.punctuation}"
    lines = [line for _ in range(request.times)]
    return GreetingResponse(lines=lines)
