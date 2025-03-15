from multiprocessing import Pool, pool

from alltheutils import types
from alltheutils.utils import noop


# ================================= Classes ====================================
class PoolTerminate:
    def __init__(self, pool: pool.Pool, callback_fn: types.CallableAny) -> None:
        self.called = False
        self.pool = pool
        self.callback_fn = callback_fn

    def callback(self, result: bool | tuple[bool, *types.Args]) -> None:
        """
        If `to_return` is `True`, then terminate the pool and call the callback.

        Args:
        - to_return (`bool`): If `True`, then terminate the pool and call the callback.
        - args (`types.Args`): Arguments to be passed to the callback.

        Args:
        - result (`bool | tuple[bool,`): The result of the callback.

        Raises:
        - `TypeError`: Raise when the callback does not return a bool, or a tuple with the first item as a bool.

        """

        # Ensure result is a tuple
        if isinstance(result, bool):
            to_return = result
        else:
            to_return, *args = result
            if not isinstance(to_return, bool):
                self.pool.terminate()
                raise TypeError(
                    "Callback must return a bool, or a tuple with the first item as a bool.",
                )

        if to_return and (not self.called):
            self.called = True
            self.pool.terminate()

            # I almost did something stupid LMFAOOO
            # If the function returns a `tuple[bool, *args]`, and the `*args` is a tuple
            # containing a singular, then, it will be unpacked as such.
            # If `*args` is a singular item, it will be returned as such.
            # There is no need to distinguish whether `*args` is actually a tuple with
            # a single item or just a singular item.
            self.callback_fn(*args)


class CallbackGetResult:
    def __init__(self) -> None:
        self.args: types.Args = ()

    def callback(self, *args: types.Args) -> None:
        self.args = args

    def get(self) -> types.Args:
        return self.args


# ============================= Top dependencies ===============================
def run_mp_qir(
    func: types.CallableAny,
    iterable: types.IterAny,
    callback: types.CallableAny,
) -> None:
    """
    `run_mp_qir`: RUN MultiProcessing, then Quit In the first successful Return.

    Iterate over `iterable`, apply iterated item to `func` asynchronously thru `multiprocessing.Pool().map_async()`, then quit in the first successful return.

    This function requires the given function to return a boolean value, or an iterable with its first item as a boolean. Said boolean value will be hereinafter referred to as `to_return`. The first function to return `to_return` as having the value `True` will trigger the callback and terminate the pool.

    Example:
    ```python
    from alltheutils.multi_processing import run_mp_qir

    def process_items(x):
        return True, x * 2

    run_mp_qir(process_items, [1, 2, 3], print)
    ```

    Args:
    - func (`types.CallableAny`): Function to be run on each item in parallel.
    - iterable (`types.IterAny`): Iterable containing items to iterate over and pass to `func`.
    - callback (`types.CallableAny`): Function to be called when a process in the pool returns.

    """
    if callback is None:
        callback = noop
    with Pool() as pool:
        pool_terminate = PoolTerminate(pool, callback)
        for i in iterable:
            pool.apply_async(
                func,
                args=(i,),
                callback=pool_terminate.callback,
            )
        pool.close()
        pool.join()


def run_mp_star_qir(
    func: types.CallableAny,
    iterable: types.IterIterAny,
    callback: types.CallableAny,
) -> None:
    """
    `run_mp_star_qir`: RUN MultiProcessing STAR, then Quit In the first successful Return.

    Iterate over `iterable`, apply iterated iterables to `func` asynchronously thru `multiprocessing.Pool().map_async()` (mimicking `multiprocessing.Pool().starmap_async()`), then quit in the first successful return.

    This function requires the given function to return a boolean value, or an iterable with its first item as a boolean. Said boolean value will be hereinafter referred to as `to_return`. The first function to return `to_return` as having the value `True` will trigger the callback and terminate the pool.

    Example:
    ```py
    from alltheutils.multi_processing import run_mp_star_qir

    def process_items(x, y):
        return True, x + y

    run_mp_star_qir(process_items, [(1, 2), (3, 4), (5, 6)], print)
    ```

    Args:
    - func (`types.CallableAny`): Function to be run on each item in parallel.
    - iterable (`types.IterIterAny`): Iterable containing iterables to iterate over and pass to `func`.
    - callback (`types.CallableAny`): Function to be called when a process in the pool returns.

    """
    if callback is None:
        callback = noop
    with Pool() as pool:
        pool_terminate = PoolTerminate(pool, callback)
        for i in iterable:
            pool.apply_async(func, args=i, callback=pool_terminate.callback)
        pool.close()
        pool.join()


# ================================ Functions ===================================
def run_mp(func: types.CallableAny, iterable: types.IterAny) -> types.ListAny:
    """
    `run_mp`: RUN MultiProcessing.

    Run `multiprocessing.Pool().map()`, then return all the results

    Iterate over `iterable` and apply iterated item to `func` asynchronously.

    Example:
    ```python
    from alltheutils.multi_processing import run_mp

    def process_items(x):
        print(x * 2)

    run_mp(process_items, [1, 2, 3])
    ```

    Args:
    - func (`types.CallableAny`): Function to be run on each item in parallel.
    - iterable (`types.IterAny`): Iterable containing items to iterate over and pass to `func`.

    Returns:
    `types.ListAny`: A list of the results of applying `func` to each item in `iterable`.

    """
    with Pool() as pool:
        return pool.map(func, iterable)


def run_mp_qgr(func: types.CallableAny, iterable: types.IterAny) -> types.TupleAny:
    """
    `run_mp_qgr`: RUN MultiProcessing, Quit in the first successful return, then Get the Results.

    Iterate over `iterable`, apply iterated item to `func` asynchronously thru `multiprocessing.Pool().map_async()`, quit in the first successful return, then return the results of the first succesful return.

    This function requires the given function to return a boolean value, or an iterable with its first item as a boolean. Said boolean value will be hereinafter referred to as `to_return`. The first function to return `to_return` as having the value `True` will trigger the callback and terminate the pool.

    Example:
    ```python
    from alltheutils.multi_processing import run_mp_qgr

    def process_items(x):
        return True, x * 2

    print(run_mp_qgr(process_items, [1, 2, 3]))
    ```

    Args:
    - func (`types.CallableAny`): Function to be run on each item in parallel.
    - iterable (`types.IterAny`): Iterable containing items to iterate over and pass to `func`.

    Returns:
    `types.TupleAny`: A list of the results of applying `func` to each item in `iterable`.

    """
    res_cb = CallbackGetResult()
    run_mp_qir(func, iterable, res_cb.callback)
    return res_cb.get()


def run_mp_star(func: types.CallableAny, iterable: types.IterIterAny) -> types.ListAny:
    """
    `run_mp_star`: RUN MultiProcessing STAR.

    Run `multiprocessing.Pool().starmap()`, then return all the results.

    Iterate over `iterable` and apply iterated iterable item to `func` asynchronously.

    Example:
    ```python
    from alltheutils.multi_processing import run_mp_star

    def process_items(x, y):
        print(x + y)

    run_mp_star(process_items, [(1, 2), (3, 4), (5, 6)])
    ```

    Args:
    - func (`types.CallableAny`): Function to be run on each item in parallel.
    - iterable (`types.IterIterAny`): Iterable containing iterables to iterate over and pass to `func`.

    Returns:
    `types.ListAny`: A list of the results of applying `func` to each item in `iterable`.

    """
    with Pool() as pool:
        return pool.starmap(func, iterable)


def run_mp_star_qgr(
    func: types.CallableAny,
    iterable: types.IterIterAny,
) -> types.TupleAny:
    """
    `run_mp_star_qir`: RUN MultiProcessing STAR, Quit in the first successful return, then Get the Results.

    Iterate over `iterable`, apply iterated iterables to `func` asynchronously thru `multiprocessing.Pool().map_async()` (mimicking `multiprocessing.Pool().starmap_async()`), quit in the first successful return, then return the results of the first succesful return.

    This function requires the given function to return a boolean value, or an iterable with its first item as a boolean. Said boolean value will be hereinafter referred to as `to_return`. The first function to return `to_return` as having the value `True` will trigger the callback and terminate the pool.

    Example:
    ```python
    from alltheutils.multi_processing import run_mp_star_qgr

    def process_items(x, y):
        return True, x + y

    print(run_mp_star_qgr(process_items, [(1, 2), (3, 4), (5, 6)]))
    ```

    Args:
    - func (`types.CallableAny`): Function to be run on each item in parallel.
    - iterable (`types.IterIterAny`): Iterable containing iterables to iterate over and pass to `func`.

    Returns:
    `types.TupleAny`: A list of the results of applying `func` to each item in `iterable`.

    """
    res_cb = CallbackGetResult()
    run_mp_star_qir(func, iterable, res_cb.callback)
    return res_cb.get()
