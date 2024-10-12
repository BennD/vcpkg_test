cmake_minimum_required(VERSION 3.28)

project(ProjectA)

include(CMakePackageConfigHelpers)

set(ExportName ${PROJECT_NAME})
set(Version 1.1.0)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_DEBUG_POSTFIX "d")

add_subdirectory(Component3)
add_subdirectory(Component2)
add_subdirectory(Component1)

#########################################################################################
## CMake install configuration
#########################################################################################

# generate the version file for the config file
write_basic_package_Version_file(
        "${CMAKE_CURRENT_BINARY_DIR}/${ExportName}ConfigVersion.cmake"
        VERSION "${Version}"
        COMPATIBILITY AnyNewerVersion
)

configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
        "${CMAKE_CURRENT_BINARY_DIR}/${ExportName}Config.cmake"
        INSTALL_DESTINATION share/cmake/${ExportName}
)

install(FILES
        "${CMAKE_CURRENT_BINARY_DIR}/${ExportName}Config.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/${ExportName}ConfigVersion.cmake"
        DESTINATION share/${ExportName}
        COMPONENT ${ExportName}
)
