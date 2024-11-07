cmake_minimum_required(VERSION 3.28)

include(CMakePackageConfigHelpers)

project(ProjectA)

if (NOT CMAKE_TOOLCHAIN_FILE)
    # No toolchain used, set global C++ settings
    set(CMAKE_CXX_STANDARD 20)
endif ()

find_package(spdlog REQUIRED CONFIG)

add_subdirectory(ProjectA/LayerSupport)
add_subdirectory(ProjectA/LayerApps)

#########################################################################################
## CMake install configuration
#########################################################################################

configure_package_config_file(Config.cmake.in
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
        INSTALL_DESTINATION share/${PROJECT_NAME}
)

install(FILES
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
        DESTINATION share/${PROJECT_NAME}
)
