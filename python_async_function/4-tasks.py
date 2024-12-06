#!/usr/bin/env python3
"""
4-tasks.py

Ce module contient la fonction `task_wait_n` qui
exécute plusieurs taches syncio
"""


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Lancer `task_wait_random` n fois avec un délai
    max spécifié,et retourner la liste des délais
    dans l'ordre croissant.

    Args:
        n (int): Nombre de fois à exécuter `task_wait_random`.
        max_delay (int): Délai maximal pour chaque appel.

    Returns:
        List[float]: Liste des délais triés par ordre croissant.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed_tasks = await asyncio.gather(*tasks)
    return sorted(completed_tasks)
