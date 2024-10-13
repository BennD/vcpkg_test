getPatchVersion(PatchVersion)
project(Component1 VERSION 1.0.${PatchVersion})

set(CMAKE_CXX_STANDARD 20)

add_executable(Component1 main.cpp)
target_link_libraries(Component1 PRIVATE ProjectA::Component2)

#########################################################################################
## CMake install configuration
#########################################################################################
