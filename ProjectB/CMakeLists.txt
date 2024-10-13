cmake_minimum_required(VERSION 3.28)

find_package(CMakeHelperModules 1.0 REQUIRED)
include(VersioningHelpers)
include(CMakePackageConfigHelpers)

getPatchVersion(PatchVersion)
project(ProjectB VERSION 1.0.${PatchVersion})

set(CMAKE_CXX_STANDARD 20)

find_package(ProjectA REQUIRED CONFIG)

add_executable(ProjectB main.cpp)
target_link_libraries(ProjectB PRIVATE ProjectA::Component2)
target_link_libraries(ProjectB PRIVATE ProjectA::Component3)
