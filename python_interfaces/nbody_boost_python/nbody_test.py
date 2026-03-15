"""
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
"""

import pytest
import json
import my_module

def test_nbody():
  try:
    with open('../../../cpp_progs/oop_example/nbody/nbody_input.json', 'r') as file:
      data = json.load(file)
    with open('../../../cpp_progs/oop_example/nbody/nbody_data_for_test.json', 'r') as file1:
      data1 = json.load(file1)
    tolerance = 1e-6
    ncases = 7;
    for i in range(0, ncases):
      tag = 'case_' + str(i + 1)
      simulator = my_module.Nbody(data[tag])
      energies = simulator.get_energy();
      for en in energies:
        assert en == pytest.approx(data1[tag]["energy"], abs=tolerance)
      c_alpha = simulator.get_c_alpha();
      for ca in c_alpha:
        assert ca == pytest.approx(data1[tag]["c_alpha"], abs=tolerance)
      nbody = simulator.get_nbody();
      ndata = simulator.get_ndata();
      angular_momentum = simulator.get_angular_momentum();
      count = 0
      for j in range(0, ndata):
        for k in range(0, 3):
          assert angular_momentum[count] == pytest.approx(data1[tag]["angular_momentum"][k], abs=tolerance);
          count = count + 1
      angular_momentum_i = simulator.get_angular_momentum_i();
      count = 0
      for j in range(0, ndata):
        for k in range(0, 3 * nbody):
          assert angular_momentum_i[count] == pytest.approx(data1[tag]["angular_momentum_i"][k], abs=tolerance);
          count = count + 1
  except FileNotFoundError:
    print("Error: The file 'nbody_input.json' or 'nbody_data_for_test.json' was not found.")
