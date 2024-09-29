cmake_minimum_required(VERSION 3.29)
project(Component1)

set(CMAKE_CXX_STANDARD 20)

#find_package(ProjectA::Component2 REQUIRED CONFIG)

add_executable(Component1 main.cpp)
# TODO private
target_link_libraries(Component1 PUBLIC ProjectA::Component2)
