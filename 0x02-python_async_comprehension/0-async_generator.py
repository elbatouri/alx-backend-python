#!/usr/bin/env python3
'''Task 0's couroutine loops with 1 s wait.
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Generates 10 numbers sequence.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
