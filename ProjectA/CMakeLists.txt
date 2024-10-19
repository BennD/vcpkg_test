cmake_minimum_required(VERSION 3.28)

include(CMakePackageConfigHelpers)

project(ProjectA VERSION 1.0.0)

set(CMAKE_CXX_STANDARD 20)

add_subdirectory(LayerSupport)
add_subdirectory(LayerApps)

#########################################################################################
## CMake install configuration
#########################################################################################

# generate the version file for the config file
write_basic_package_Version_file(
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
        VERSION "${PROJECT_VERSION}"
        COMPATIBILITY AnyNewerVersion
)

configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
        INSTALL_DESTINATION share/${PROJECT_NAME}
)

install(FILES
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
        DESTINATION share/${PROJECT_NAME}
)
