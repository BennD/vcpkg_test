cmake_minimum_required(VERSION 3.28)
project(ProjectB)

set(CMAKE_CXX_STANDARD 20)

find_package(ProjectA REQUIRED CONFIG)

add_executable(ProjectB main.cpp)
target_link_libraries(ProjectB PRIVATE ProjectA_Component2)
target_link_libraries(ProjectB PRIVATE ProjectA_Component3)
