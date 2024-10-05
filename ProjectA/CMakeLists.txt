cmake_minimum_required(VERSION 3.28)

project(ProjectA)

include(GNUInstallDirs)
include(CMakePackageConfigHelpers)

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
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
        VERSION "${version}"
        COMPATIBILITY AnyNewerVersion
)

configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
        INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}
)

install(FILES
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}
        COMPONENT ${PROJECT_NAME}
)
