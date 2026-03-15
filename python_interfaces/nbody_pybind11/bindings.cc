/*
  This file is part of nbody_pybind11.

  Copyright (C) 2026 Fredy W. Aquino

  nbody_pybind11 is free software: you can redistribute it and/or modify it under
  the terms of the GNU Lesser General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  nbody_pybind11 is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public License
  along with nbody_pybind11.  If not, see <https://www.gnu.org/licenses/>.

  Description : Program to interface C++ program nbody.cc with Python
                using library pybind11
  Date        : 03-15-26
*/

#include <memory>
#include <vector>
#include <algorithm>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <nlohmann/json.hpp>
#include "../../../cpp_progs/oop_example/nbody/nbody.h"

namespace py = pybind11;

PYBIND11_MODULE(my_module, m) {
    m.doc() = "pybind11 nbody plugin"; // Optional module docstring

    // Bind the nbody class
    py::class_<nbody::Nbody<double>>(m, "Nbody")
        .def(py::init([](py::dict dict) {  // Expose the constructor
            // Convert py::dict to std::string then to json
            auto json_str = py::str(dict);
            std::string val = static_cast<std::string>(json_str);
            std::replace(val.begin(), val.end(), '\'', '"');
            nlohmann::json j = nlohmann::json::parse(val);
            return std::make_unique<nbody::Nbody<double>>(j);
        }))
        .def("get_nbody", &nbody::Nbody<double>::get_nbody, "Get number of bodies")
        .def("get_ndata", &nbody::Nbody<double>::get_ndata, "Get ndata")
        .def("get_c_alpha", &nbody::Nbody<double>::get_c_alpha, "Get c_alpha")
        .def("get_energy", &nbody::Nbody<double>::get_energy, "Get energies")
        .def("get_angular_momentum", &nbody::Nbody<double>::get_angular_momentum, "Get angular momentum")
        .def("get_angular_momentum_i", &nbody::Nbody<double>::get_angular_momentum_i, "Get angular momentum per body");
}
