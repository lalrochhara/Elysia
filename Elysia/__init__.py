"""Elysia core package."""
# Famhawite-Infosys-License-Identifier: MIT
# Copyright (c) 2019 - 2023 Famhawite Infosys

from subprocess import run

__commit__ = (
    run(["git", "rev-parse", "--short", "HEAD"], capture_output=True)
    .stdout.decode()
    .strip()
    or "None"
)

__version_number__ = (
    run(["git", "rev-list", "--count", "HEAD"], capture_output=True)
    .stdout.decode()
    .strip()
    or "0"
)
