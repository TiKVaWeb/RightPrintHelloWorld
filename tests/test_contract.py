"""Контрактные и smoke-тесты."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from print_hello_world.dto import GreetingRequest, GreetingResponse
from print_hello_world.service import build_greeting


def test_dto_service_contract() -> None:
    request = GreetingRequest(name="Contract", times=2, punctuation=".")
    response = build_greeting(request)

    assert isinstance(response, GreetingResponse)
    assert response.lines == ["Hello, Contract.", "Hello, Contract."]


def test_module_smoke_run() -> None:
    project_root = Path(__file__).resolve().parents[1]
    src_path = project_root / "src"
    current_pythonpath = os.environ.get("PYTHONPATH")
    pythonpath = str(src_path)
    if current_pythonpath:
        pythonpath = f"{pythonpath}{os.pathsep}{current_pythonpath}"

    env = dict(os.environ)
    env["PYTHONPATH"] = pythonpath

    completed = subprocess.run(
        [sys.executable, "-m", "print_hello_world", "--name", "Smoke"],
        cwd=project_root,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )

    assert completed.returncode == 0
    assert completed.stdout == "Hello, Smoke!\n"
    assert completed.stderr == ""
