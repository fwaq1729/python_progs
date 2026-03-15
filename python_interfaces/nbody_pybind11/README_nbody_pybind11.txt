Instruction on how to compile  
=============================  
  
0. In directory nbody_pybind11  
> mkdir build;cd build;cmake ..  
In directory build:  
> make  
> cp my_module.cpython-312-x86_64-linux-gnu.so ..  
1. Run pytest nbody_test.py  
In directory nbody_pybind11  
> pytest nbody_test.py  
  
FA-03-15-26
