#!/usr/bin/env python3
"""
0-basic_async_syntax.py

Ce module contient une coroutine asynchrone `wait_random`
qui attend un délai aléatoire avant de retourner ce délai.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Coroutine qui attend un délai aléatoire (entre 0 et
    max_delay) en secondes,puis retourne ce délai.

    Args:
        max_delay (int): La valeur maximale (en secondes)
        pour le délai aléatoire. Par défaut : 10.

    Returns:
        float: Le délai aléatoire qui a été attendu.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
