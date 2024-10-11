cmake_minimum_required(VERSION 3.28)

project(ProjectA)

include(CMakePackageConfigHelpers)

set(export_name "${PROJECT_NAME}")
set(version 1.1.0)
set(CMAKE_CXX_STANDARD 20)

add_subdirectory(Component3)
add_subdirectory(Component2)
add_subdirectory(Component1)

#########################################################################################
## CMake install configuration
#########################################################################################

# generate the version file for the config file
write_basic_package_version_file(
        "${CMAKE_CURRENT_BINARY_DIR}/${export_name}ConfigVersion.cmake"
        VERSION "${version}"
        COMPATIBILITY AnyNewerVersion
)

configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
        "${CMAKE_CURRENT_BINARY_DIR}/${export_name}Config.cmake"
        INSTALL_DESTINATION share/cmake/${export_name}
)

install(FILES
        "${CMAKE_CURRENT_BINARY_DIR}/${export_name}Config.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/${export_name}ConfigVersion.cmake"
        DESTINATION share/${export_name}
        COMPONENT ${export_name}
)
