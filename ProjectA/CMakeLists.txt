cmake_minimum_required(VERSION 3.28)

find_package(CMakeHelperModules 1.0 REQUIRED)
include(VersioningHelpers)
include(CMakePackageConfigHelpers)

getPatchVersion(PatchVersion)
project(ProjectA VERSION 1.0.${PatchVersion})

set(CMAKE_CXX_STANDARD 20)

add_subdirectory(Component3)
add_subdirectory(Component2)
add_subdirectory(Component1)