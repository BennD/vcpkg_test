cmake_minimum_required(VERSION 3.28)

include(CMakePackageConfigHelpers)

project(ProjectA VERSION 1.0.0)

if(NOT CMAKE_TOOLCHAIN_FILE)
	# No toolchain used, set global C++ settings
	set(CMAKE_CXX_STANDARD 20)
endif()

find_package(spdlog REQUIRED CONFIG)

add_subdirectory(ProjectA/LayerSupport)
add_subdirectory(ProjectA/LayerApps)

#########################################################################################
## CMake install configuration
#########################################################################################

# generate the version file for the config file
write_basic_package_Version_file(
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
        VERSION "${PROJECT_VERSION}"
        COMPATIBILITY AnyNewerVersion
)

configure_package_config_file(Config.cmake.in
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
        INSTALL_DESTINATION share/${PROJECT_NAME}
)

install(FILES
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
        DESTINATION share/${PROJECT_NAME}
)
