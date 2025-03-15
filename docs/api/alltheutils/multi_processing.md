# Module alltheutils.multi_processing

[← Go back to `alltheutils`](./index.md)

## Functions

### `run_mp`

```python
(func: Callable[..., typing.Any], iterable: Iterable[typing.Any]) → list[typing.Any]
```

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

### `run_mp_qgr`

```python
(func: Callable[..., typing.Any], iterable: Iterable[typing.Any]) → tuple[None] | tuple[typing.Any] | tuple[typing.Any, ...]
```

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

### `run_mp_qir`

```python
(func: Callable[..., typing.Any], iterable: Iterable[typing.Any], callback: Callable[..., typing.Any]) → None
```

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

### `run_mp_star`

```python
(func: Callable[..., typing.Any], iterable: Iterable[Iterable[typing.Any]]) → list[typing.Any]
```

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

### `run_mp_star_qgr`

```python
(func: Callable[..., typing.Any], iterable: Iterable[Iterable[typing.Any]]) → tuple[None] | tuple[typing.Any] | tuple[typing.Any, ...]
```

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

### `run_mp_star_qir`

```python
(func: Callable[..., typing.Any], iterable: Iterable[Iterable[typing.Any]], callback: Callable[..., typing.Any]) → None
```

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

## Classes

### `CallbackGetResult`

#### Methods

##### `callback`

```python
(self, *args: tuple[typing.Any, ...]) → None
```

##### `get`

```python
(self) → tuple[typing.Any, ...]
```

### `PoolTerminate`

```python
(pool: multiprocessing.pool.Pool, callback_fn: Callable[..., typing.Any])
```

#### Methods

##### `callback`

```python
(self, result: bool | tuple[bool, *tuple[typing.Any, ...]]) → None
```

If `to_return` is `True`, then terminate the pool and call the callback.

Args:
- to_return (`bool`): If `True`, then terminate the pool and call the callback.
- args (`types.Args`): Arguments to be passed to the callback.

Args:
- result (`bool | tuple[bool,`): The result of the callback.

Raises:
- `TypeError`: Raise when the callback does not return a bool, or a tuple with the first item as a bool.

---

[← Go back to `alltheutils`](./index.md)