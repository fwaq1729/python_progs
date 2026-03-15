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

from libcpp.string cimport string
from libcpp.vector cimport vector

cdef extern from "<nlohmann/json.hpp>" namespace "nlohmann":
    cdef cppclass json:
        json()
        @staticmethod
        json parse(string)
        string dump()

cdef extern from "../../../../cpp_progs/oop_example/nbody/nbody.h" namespace "nbody":
    cdef cppclass Nbody[T]:
        Nbody(json data) except +
        int get_nbody()
        int get_ndata()
        vector[double] get_energy()
        vector[double] get_c_alpha()
        vector[double] get_angular_momentum()
        vector[double] get_angular_momentum_i()
