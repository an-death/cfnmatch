# cython: language_level=3
from cpython cimport bool
from fnmatch cimport (
    fnmatch,
    FNM_NOMATCH,
    FNM_FILE_NAME,
    FNM_PATHNAME,
    FNM_PERIOD,
    FNM_NOESCAPE,
    FNM_LEADING_DIR,
    FNM_CASEFOLD,
    )


cpdef bool cfnmatch(str domain, str pattern, int flag=FNM_CASEFOLD):
    """Documentation: http://man7.org/linux/man-pages/man3/fnmatch.3.html"""
    res = fnmatch(pattern.encode(), domain.encode(), flag)
    if res == 0:
        return True

    if res != FNM_NOMATCH:
        # GNU C fnmatch never occur error,
        # but that is not true for any other realization
        raise ValueError(f'cannot match for pattern {pattern}')
    return False


cpdef patch():
    # patch python module
    import fnmatch as python_fnmatch_module
    python_fnmatch_module.fnmatch = cfnmatch
