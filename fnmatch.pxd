
cdef extern from "fnmatch.h":
    int FNM_NOMATCH
    bint fnmatch(const char *pattern, const char *string, int flags)
    int FNM_FILE_NAME
    int FNM_PATHNAME
    int FNM_PERIOD
    int FNM_NOESCAPE
    int FNM_LEADING_DIR
    int FNM_CASEFOLD