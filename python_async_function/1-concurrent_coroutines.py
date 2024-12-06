#!/usr/bin/env python3
"""
1-concurrent_coroutines.py

Ce module contient la coroutine `wait_n` pour exécuter
plusieurs appels à `wait_random` en parallèle.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Lancer `wait_random` n fois avec un délai max spécifié,
    et retourner la liste des délais dans l'ordre croissant.

    Args:
        n (int): Nombre de fois à exécuter `wait_random`.
        max_delay (int): Délai maximal pour chaque appel.

    Returns:
        List[float]: Liste des délais triés par ordre croissant.
    """
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))

    completed_tasks = await asyncio.gather(*delays)
    return sorted(completed_tasks)
