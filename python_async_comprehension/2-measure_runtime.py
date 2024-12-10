#!/usr/bin/env python3
"""
2-measure_runtime.py
Ce module mesure le temps d'exécution de `async_comprehension`
exécuté 4 fois en parallèle.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Exécute `async_comprehension` quatre fois en parallèle
    et mesure le temps total d'exécution.

    Returns:
        float: Temps total d'exécution.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()

    return end_time - start_time
