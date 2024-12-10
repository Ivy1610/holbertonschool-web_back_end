#!/usr/bin/env python3
"""
1-async_comprehension.py

Ce module contient la coroutine `async_comprehension`
qui utilise une compréhension asynchrone pour collecter des données.
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collecte 10 nombres aléatoires générés par `async_generator`
    à l'aide d'une compréhension asynchrone.

    Returns:
        List[float]: Liste de 10 nombres aléatoires.
    """
    return [number async for number in async_generator()]
