"""DTO-объекты доменной области приветствий."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GreetingRequest:
    """Входные параметры для генерации приветствия."""

    name: str
    times: int
    punctuation: str


@dataclass(frozen=True, slots=True)
class GreetingResponse:
    """Результат генерации приветствия."""

    lines: list[str]
