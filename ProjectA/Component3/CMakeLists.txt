cmake_minimum_required(VERSION 3.28)

project(Component3)

include(CMakePackageConfigHelpers)

set(ExportName ProjectA_${PROJECT_NAME})
set(Version 1.2.0)
set(CMAKE_CXX_STANDARD 20)

set(HEADERS
        helper.h
)

set(SOURCES
        helper.cpp
)

# Library
add_library(${PROJECT_NAME} ${SOURCES})
add_library(ProjectA::${PROJECT_NAME} ALIAS ${PROJECT_NAME})
target_sources(${PROJECT_NAME} PUBLIC FILE_SET HEADERS FILES ${HEADERS})

target_include_directories(${PROJECT_NAME} PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/../..>
        $<INSTALL_INTERFACE:include>
)

#########################################################################################
## CMake install configuration
#########################################################################################

install(TARGETS ${PROJECT_NAME}
        EXPORT ${ExportName}Targets
        ARCHIVE DESTINATION lib/$<CONFIG>
        LIBRARY DESTINATION lib/$<CONFIG>
        RUNTIME DESTINATION bin/$<CONFIG>
        FILE_SET HEADERS DESTINATION include/ProjectA/Component3
        COMPONENT ${ExportName}
)

install(EXPORT ${ExportName}Targets
        FILE ${ExportName}Targets.cmake
        DESTINATION share/${ExportName}
        NAMESPACE ProjectA::
        COMPONENT ${ExportName}
)

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