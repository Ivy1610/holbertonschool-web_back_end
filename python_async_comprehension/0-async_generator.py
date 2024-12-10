#!/usr/bin/env python3
"""
0-async_generator.py

Ce module contient la coroutine `async_generator`
qui génère des nombres aléatoires
"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    coroutine qui génère 10 nombres aléatoires entre 0 et 10,
    avec une pause de 1 seconde entre chaque generation

    Returns:
        AsyncGenerator[float, None]: Générateur
        asynchrone de nombres aléatoires
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
