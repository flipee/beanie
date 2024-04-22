import asyncio
import functools
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


async def run_in_threadpool(
    func: Callable[P, T], *args: P.args, **kwargs: P.kwargs
) -> T:
    loop = asyncio.get_running_loop()
    if kwargs:  # pragma: no cover
        func = functools.partial(func, **kwargs)

    return await loop.run_in_executor(None, func, *args)
