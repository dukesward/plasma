####### setup project and cmake #######

set(CMAKE_LEGACY_CYGWIN_WIN32 0)

# Project name
project (socket)

# CMake version requirement
cmake_minimum_required(VERSION 3.0)

# this is depending on where the python src is
# set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)

# this is used to specify module path for find_packages
set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake/macros")

message( STATUS "Looking for Python.h..." )
find_package(Python)
include_directories(${PYTHON_INCLUDE_DIR})

set(py_execute execute.cpp)
add_executable(py_exe_test ${py_execute})
