#!/usr/bin/env python3
"""
3-tasks.py
Ce module contient la fonction `task_wait_random`
qui retourne une tâche asyncio
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Crée une tâche asyncio pour exécuter `wait_random`.

    Args:
        max_delay (int): Délai maximal pour l'appel à `wait_random`.

    Returns:
        asyncio.Task: Une tâche asyncio pour exécuter `wait_random`.
    """
    return asyncio.create_task(wait_random(max_delay))
