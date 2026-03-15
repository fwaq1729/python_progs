g++ -O3 -std=c++20 -shared -fPIC -o my_module.so binding.cc \
	../../../cpp_progs/oop_example/nbody/nbody.cc \
	-I/usr/include/boost \
	-I/usr/include/python3.12 \
	-lboost_python312 \
	-lpython3.12
