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

from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        "wrapper",                                # Name of the Python module
        sources=["wrapper.pyx", "../../../cpp_progs/oop_example/nbody/nbody.cc"], # Cython and C++ source files
        language="c++",                           # Specify C++ mode
        extra_compile_args=["-Wall", "-Wpedantic", "-Wextra", "-Werror", "-std=c++20", "-DNDEBUG", "-O3"], # Optional: specify C++ standard
    )
]

setup(
    name="MyCppModule",
    ext_modules=cythonize(extensions, build_dir="build", language_level="3"),
    zip_safe=False,
)
