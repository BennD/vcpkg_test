project(Component1)

set(CMAKE_CXX_STANDARD 20)

add_executable(Component1 main.cpp)
target_link_libraries(Component1 PRIVATE ProjectA::Component2)

#########################################################################################
## CMake install configuration
#########################################################################################
