/*
  This file is part of nbody_boost_python.

  Copyright (C) 2026 Fredy W. Aquino

  nbody_boost_python is free software: you can redistribute it and/or modify it under
  the terms of the GNU Lesser General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  nbody_boost_python is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public License
  along with nbody_boost_python.  If not, see <https://www.gnu.org/licenses/>.

  Description : Program to interface C++ program nbody.cc with Python
                using library boost.python
  Date        : 03-15-26
*/

#include <nlohmann/json.hpp>
#include <boost/python.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>
#include "../../../cpp_progs/oop_example/nbody/nbody.h"

using namespace boost::python;

struct json_from_python {
    // 1. Register the converter
    json_from_python() {
        boost::python::converter::registry::push_back(
            &convertible, &construct, boost::python::type_id<nlohmann::json>());
    }

    // 2. Check if the Python object can be converted (e.g., it's a dict or list)
    static void* convertible(PyObject* obj_ptr) {
        // You can add stricter checks here if needed
        return obj_ptr;
    }

    // 3. Perform the actual conversion
    static void construct(PyObject* obj_ptr,
                         boost::python::converter::rvalue_from_python_stage1_data* data) {
        // Extract string representation or use Python C API to parse
        boost::python::handle<> handle(boost::python::borrowed(obj_ptr));
        boost::python::object obj(handle);

        // Simple approach: Convert Python object to JSON string, then parse
        std::string s = boost::python::extract<std::string>(boost::python::import("json").attr("dumps")(obj));

        void* storage = ((boost::python::converter::rvalue_from_python_storage<nlohmann::json>*)data)->storage.bytes;
        new (storage) nlohmann::json(nlohmann::json::parse(s));
        data->convertible = storage;
    }
};

template<typename T>
void wrap_vector(const char* name) {
    class_<std::vector<T>>(name)
        .def(vector_indexing_suite<std::vector<T>>());
}

// Define the module
BOOST_PYTHON_MODULE(my_module) {
    wrap_vector<double>("DoubleVector");

    // Expose the DataProcessor class within the 'my_namespace' scope in Python
    scope current_scope = scope(); // Get the current module scope
    current_scope.attr("nbody") = current_scope; // Create a nested namespace in Python if desired, or just use the current scope

    json_from_python();
    class_<nbody::Nbody<double>>("Nbody", init<nlohmann::json>())
        .def("get_nbody", &nbody::Nbody<double>::get_nbody)
        .def("get_ndata", &nbody::Nbody<double>::get_ndata)
        .def("get_c_alpha", &nbody::Nbody<double>::get_c_alpha, return_internal_reference<>())
        .def("get_energy", &nbody::Nbody<double>::get_energy, return_internal_reference<>())
        .def("get_angular_momentum", &nbody::Nbody<double>::get_angular_momentum, return_internal_reference<>())
        .def("get_angular_momentum_i", &nbody::Nbody<double>::get_angular_momentum_i, return_internal_reference<>());
}
