<h1 id=""><a href="#">Module alltheutils.multi_processing</a></h1>

[← Go back to `alltheutils`](./index.md)

<h2 id="functions"><a href="#functions">Functions</a></h2>

<h3 id="functions-prerun_mppre"><a href="#functions-prerun_mppre"><pre>run_mp</pre></a></h3>

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

<h3 id="functions-prerun_mp_qgrpre"><a href="#functions-prerun_mp_qgrpre"><pre>run_mp_qgr</pre></a></h3>

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

<h3 id="functions-prerun_mp_qirpre"><a href="#functions-prerun_mp_qirpre"><pre>run_mp_qir</pre></a></h3>

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

<h3 id="functions-prerun_mp_starpre"><a href="#functions-prerun_mp_starpre"><pre>run_mp_star</pre></a></h3>

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

<h3 id="functions-prerun_mp_star_qgrpre"><a href="#functions-prerun_mp_star_qgrpre"><pre>run_mp_star_qgr</pre></a></h3>

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

<h3 id="functions-prerun_mp_star_qirpre"><a href="#functions-prerun_mp_star_qirpre"><pre>run_mp_star_qir</pre></a></h3>

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

<h2 id="classes"><a href="#classes">Classes</a></h2>

<h3 id="classes-precallbackgetresultpre"><a href="#classes-precallbackgetresultpre"><pre>CallbackGetResult</pre></a></h3>

<h4 id="classes-precallbackgetresultpre-methods"><a href="#classes-precallbackgetresultpre-methods">Methods</a></h4>

<h5 id="classes-precallbackgetresultpre-methods-precallbackpre"><a href="#classes-precallbackgetresultpre-methods-precallbackpre"><pre>callback</pre></a></h5>

```python
(self, *args: tuple[typing.Any, ...]) → None
```

<h5 id="classes-precallbackgetresultpre-methods-pregetpre"><a href="#classes-precallbackgetresultpre-methods-pregetpre"><pre>get</pre></a></h5>

```python
(self) → tuple[typing.Any, ...]
```

<h3 id="classes-prepoolterminatepre"><a href="#classes-prepoolterminatepre"><pre>PoolTerminate</pre></a></h3>

```python
(pool: multiprocessing.pool.Pool, callback_fn: Callable[..., typing.Any])
```

<h4 id="classes-prepoolterminatepre-methods"><a href="#classes-prepoolterminatepre-methods">Methods</a></h4>

<h5 id="classes-prepoolterminatepre-methods-precallbackpre"><a href="#classes-prepoolterminatepre-methods-precallbackpre"><pre>callback</pre></a></h5>

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