// Copyright (c) 2017 Oleg Bulkin
// MIT License (https://opensource.org/licenses/MIT)

// Signal to the Python API that the string lengths returned below should be of
// type Py_ssize_t intead of int. This is recommended in the docs
#define PY_SSIZE_T_CLEAN 

// Include necessary headers
#include <Python.h>
#include <math.h>
#include "levenshtein_shared.h"

// Computes the restricted Damerau-Levenshtein distance (a.k.a. the optimal
// string alignment distance) between two given strings. This method is
// intended to be called from Python, so it accepts Python objects
// (self and a tuple of positional arguments) and returns a Python object
PyObject *rdlevenshtein(PyObject *self, PyObject *args)
{
    // Create needed vars
    Py_UNICODE *source, *target;
    Py_ssize_t s_len, t_len;

    // Use Python API to parse argument object into two Unicode strings and 
    // their lengths. If this process fails (e.g. due to missing arguments),
    // return NULL (a Python exception will also be raised by the API)
    if (!PyArg_ParseTuple(args, "u#u#", &source, &s_len, &target, &t_len))
    {
        return NULL;
    }

    // Compute restricted Damerau-Levenshtein distance using helper function
    int distance = levenshtein_compute(source, target, s_len, t_len, 1);

    // Return computed distance as Python int
    return PyLong_FromLong(distance);
}

// Computes the normalized restricted Damerau-Levenshtein distance (a.k.a. the
// normalized optimal string alignment distance) between two given strings. The
// output is a float in the range [0.0, 1.0], where 1.0 corresponds to the 
// largest possible distance for strings with these lengths
PyObject *rdlevenshtein_norm(PyObject *self, PyObject *args)
{
    // Create needed vars
    Py_UNICODE *source, *target;
    Py_ssize_t s_len, t_len;

    // Use Python API to parse argument object into two Unicode strings and 
    // their lengths. If this process fails (e.g. due to missing arguments),
    // return NULL (a Python exception will also be raised by the API)
    if (!PyArg_ParseTuple(args, "u#u#", &source, &s_len, &target, &t_len))
    {
        return NULL;
    }

    // Compute restricted Damerau-Levenshtein distance using helper function.
    // The max is always just the length of the longer string and is normalized
    // to 1.0
    int distance = levenshtein_compute(source, target, s_len, t_len, 1);
    double norm_dist = distance / fmax(s_len, t_len);

    // Return computed distance as Python float
    return PyFloat_FromDouble(norm_dist);
}
