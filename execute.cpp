#include "Python.h"

int main(int argc, char *argv[])
{
	// declare python objects
	PyObject *pName, *pModule, *pDict, *pFunc, *pValue;

	// usage: exe_name, python_src, func_name
	if(argc == 3)
	{
		// initialize python interpretor
		Py_initialize();

		// build python name project
		pName = PyString_FromString(argv[1]);

		// load python module object
		pModule = PyImport_Import(pName);

		// get dict borrowed reference from module
		pDict = PyModule_GetDict(pModule);

		// get func borrowed reference from dict
		pFunc = PyDict_GetItemString(pDict, argv[2]);

		if(PyCallable_Check(pFunc))
			// if func is callable, call python function
			PyObject_CallObject(pFunc, NULL);
		else
			PyErr_Print();

		// no need to decref borrowed references
		Py_DECREF(pModule);
		Py_DECREF(pName);

		// call finalize function
		Py_Finalize();

		return 0;
	}
}