#include "Python.h"
#include <stdio.h>

int main(int argc, char *argv[])
{
	// declare python objects
	PyObject *pModule, *pDict, *pFunc, *pValue;

	// initialize python interpretor
	Py_Initialize();

	// build python name project
	// this is no longer available in python 3
	// pName = PyString_FromString(argv[1]);
	//pName = PyBytes_FromString("plasma");

	// load python module object
	pModule = PyImport_ImportModule("plasma.entry");

	if(pModule == 0)
	{
		PyErr_Print();
		printf("Could not load python module: plasma.entry\n");
	}
	else
		printf("Found python module: plasma\n");

	// get dict borrowed reference from module
	pDict = PyModule_GetDict(pModule);

	// get func borrowed reference from dict
	pFunc = PyDict_GetItemString(pDict, "test");

	if(PyCallable_Check(pFunc))
	{
		// if func is callable, call python function
		printf("Found python callable function: plasma.entry.test\n");
		pValue = PyObject_CallObject(pFunc, NULL);
	}
	else
	{
		printf("Python function: plasma.entry.test is not callable\n");
		PyErr_Print();
	}

	// no need to decref borrowed references
	Py_DECREF(pModule);
	//Py_DECREF(pName);
	Py_DECREF(pValue);
	// call finalize function
	Py_Finalize();

	return 0;
}