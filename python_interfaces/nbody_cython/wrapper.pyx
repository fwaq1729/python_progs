"""
  This file is part of nbody_cython.

  Copyright (C) 2026 Fredy W. Aquino

  nbody_cython is free software: you can redistribute it and/or modify it under
  the terms of the GNU Lesser General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  nbody_cython is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public License
  along with nbody_cython.  If not, see <https://www.gnu.org/licenses/>.

  Description : Program to interface C++ program nbody.cc with Python
                using library Cython
  Date        : 03-15-26
"""

# distutils: language = c++

from libcpp.vector cimport vector
from libcpp.string cimport string
cimport nbody as cpp

# This is the Python-visible class
cdef class PyNbody_double:
    cdef cpp.Nbody[double] *c_instance  # Internal pointer to C++ object

    def __cinit__(self, dict data_dict):
        import json as pyjson
        cdef string json_str = pyjson.dumps(data_dict).encode('utf-8')
        cdef cpp.json j = cpp.json.parse(json_str)
        self.c_instance = new cpp.Nbody[double](j)

    def __dealloc__(self):
        del self.c_instance

    def get_nbody_py(self) -> int:
        return self.c_instance.get_nbody()

    def get_ndata_py(self) -> int:
        return self.c_instance.get_ndata()

    def get_c_alpha_py(self) -> list:
        cdef vector[double] cpp_vec = self.c_instance.get_c_alpha()
        # Convert the C++ vector to a Python list
        return [cpp_vec[i] for i in range(cpp_vec.size())]

    def get_energy_py(self) -> list:
        cdef vector[double] cpp_vec = self.c_instance.get_energy()
        # Convert the C++ vector to a Python list
        return [cpp_vec[i] for i in range(cpp_vec.size())]

    def get_angular_momentum_py(self) -> list:
        cdef vector[double] cpp_vec = self.c_instance.get_angular_momentum()
        # Convert the C++ vector to a Python list
        return [cpp_vec[i] for i in range(cpp_vec.size())]

    def get_angular_momentum_i_py(self) -> list:
        cdef vector[double] cpp_vec = self.c_instance.get_angular_momentum_i()
        # Convert the C++ vector to a Python list
        return [cpp_vec[i] for i in range(cpp_vec.size())]
