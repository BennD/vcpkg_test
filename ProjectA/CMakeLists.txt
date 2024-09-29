cmake_minimum_required(VERSION 3.29)
project(ProjectA)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_INSTALL_PREFIX ${CMAKE_SOURCE_DIR}/install)

add_subdirectory(Component2)
add_subdirectory(Component1)
