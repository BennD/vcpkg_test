cmake_minimum_required(VERSION 3.28)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/modules")
include(VersioningHelpers)
getPatchVersion(PatchVersion)

project(CMakeHelperModules VERSION 1.0.${PatchVersion})

# Install the CMake modules
set(Modules "${CMAKE_CURRENT_SOURCE_DIR}/modules")
install(DIRECTORY ${Modules}/
        DESTINATION share/${PROJECT_NAME}/modules
        FILES_MATCHING PATTERN "*.cmake"
)

# Export the package configuration
include(CMakePackageConfigHelpers)

write_basic_package_version_file(
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
        VERSION ${PROJECT_${PROJECT_NAME}_VERSION}
        COMPATIBILITY AnyNewerVersion
)

file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake" "
list(APPEND CMAKE_MODULE_PATH \"\${CMAKE_CURRENT_LIST_DIR}/modules\")
")

install(FILES
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
        DESTINATION share/${PROJECT_NAME}
)