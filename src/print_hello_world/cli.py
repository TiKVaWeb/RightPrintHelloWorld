"""CLI-адаптер для пакета print_hello_world."""

import sys
from argparse import ArgumentError, ArgumentParser
from collections.abc import Sequence

from print_hello_world.dto import GreetingRequest
from print_hello_world.service import GreetingValidationError, build_greeting


def build_parser() -> ArgumentParser:
    """Сконфигурировать парсер аргументов."""
    parser = ArgumentParser(
        prog="print-hello-world",
        description="Печатает максимально overengineered Hello World.",
        exit_on_error=False,
    )
    parser.add_argument(
        "--name",
        default="World",
        help="Имя для приветствия.",
    )
    parser.add_argument(
        "--times",
        default=1,
        type=int,
        help="Количество повторов приветствия (>=1).",
    )
    parser.add_argument(
        "--punctuation",
        default="!",
        help="Знак препинания в конце: !, . или ?",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Точка входа CLI, возвращает код завершения."""
    parser = build_parser()
    try:
        parsed = parser.parse_args(argv)
    except ArgumentError as exc:
        print(f"Argument error: {exc}", file=sys.stderr)
        return 2

    request = GreetingRequest(
        name=str(parsed.name),
        times=int(parsed.times),
        punctuation=str(parsed.punctuation),
    )
    try:
        response = build_greeting(request)
    except GreetingValidationError as exc:
        print(f"Validation error: {exc}", file=sys.stderr)
        return 1

    for line in response.lines:
        print(line)
    return 0


def run() -> None:
    """Запуск CLI как исполняемой команды."""
    raise SystemExit(main())
