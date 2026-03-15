cmake_minimum_required(VERSION 3.12)
project(my_module)

find_package(nlohmann_json 3.11.3 REQUIRED)
# Find or add pybind11
find_package(pybind11 CONFIG QUIET)
if(NOT pybind11_FOUND)
    # If not found, you can add it as a subdirectory (e.g., if you cloned it)
    add_subdirectory(external/pybind11)
endif()

# Add your C++ library
add_library(nbody_lib STATIC ../../../../cpp_progs/oop_example/nbody/nbody.cc ../../../../cpp_progs/oop_example/nbody/nbody.h)
target_compile_options(nbody_lib PRIVATE -Wall -Wpedantic -Wextra -Werror -Wshadow -std=c++20 -DNDEBUG -O3 -fPIC)

# Create the Python module
pybind11_add_module(my_module bindings.cc)

# Link your module to your C++ library
target_link_libraries(my_module PRIVATE nbody_lib)
