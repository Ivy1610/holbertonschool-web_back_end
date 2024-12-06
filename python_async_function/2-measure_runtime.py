#!/usr/bin/env python3
"""
2-measure_runtime.py
Ce module contient la fonction `measure_time` pour mesurer
le temps moyen d'exécution de `wait_n`
"""


import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    mesure le temps total pour exécuter `wait_n` et
    retourner le temps moyen par appel

    Args:
        n (int): Nombre d'appels à `wait_random`
        max_delay (int): Délay maximal pour chaque appel

    Returns:
        float: Temps moyen par appel (en seconde)
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    total_time = end_time - start_time
    return total_time / n
