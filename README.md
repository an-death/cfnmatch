# Cfnmatch
Replace Python `fnmatch` with fast GNU C implementation.

Increase performance x200 times see benchmarks here: 

[python-benchmarks][https://github.com/an-death/domain-match/tree/master/python]


[https://github.com/an-death/domain-match/tree/master/python]: python-benchmarks


#### Install:
```bash
pip3 install cfnmatch
```

##### Replace standart python fnmatch function
Before
```python
from fnmatch import fnmatch
fnmatch("some.ext", "some.*")
```
Replace import
```python
from cfnmatch import cfnmatch as fnmatch
fnmatch("some.ext", "some.*")
```
Patch python version `fnmatch` to C version

```python
from cfnmatch import patch
patch()
```

In simple example at least x3-6 times faster
```python
>>> import timeit 
>>> timeit.timeit("fnmatch('some.ext', 'some.*')", number=10**6, setup='from fnmatch import fnmatch')
3.4916188770148437
>>> timeit.timeit("fnmatch('some.ext', 'some.*')", number=10**6, setup='from cfnmatch import cfnmatch as fnmatch')
0.5683430910285097
>>> timeit.timeit("fnmatch('some.ext', 'some.*')", number=10**6, setup='from fnmatch import fnmatch; from cfnmatch import patch; patch()')
0.5757535599987023
```

But if you need compile massive dynamic set of templates in runtime
(like in benchmark examples) the difference in performance will grow exponentially
 because the Python version of the `fnmatch` uses a small lru-cache for
 repeated calls to compile patterns. See: 
 [cpython/fnmatch.py][https://github.com/python/cpython/blob/3.8/Lib/fnmatch.py#L38]
 
[https://github.com/python/cpython/blob/3.8/Lib/fnmatch.py#L38]: cpython/fnmatch.py

### Requires

- CPython >= 3.5
- Cython  >= 0.29