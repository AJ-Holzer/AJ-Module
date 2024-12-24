import numba as nb
from typing import Any, Callable

def run_on_gpu(func: Callable[..., Any], nopython: bool=True, parallel: bool=False, *args, **kwargs) -> Any:
    """
    Runs a given function on the GPU using CuPy.

    :param nopython (bool): Uses no python while running on the gpu.
    :param parallel (bool): Uses parallel processing while running on the gpu.
    :param func (callable): The function to be executed on the GPU.
    :param *args: Variable number of positional arguments to be passed to the function.
    :param **kwargs: Variable number of keyword arguments to be passed to the function.

    :return (Any): The result of the function execution.
    """

    gpu_func = nb.jit(nopython=nopython, parallel=parallel)(func)

    # Run the function on the GPU
    result = gpu_func(*args, **kwargs)

    return result