cmake_minimum_required(VERSION 3.28)

project(Component3)

include(GNUInstallDirs)
include(CMakePackageConfigHelpers)

set(export_name ProjectA_${PROJECT_NAME})
set(version 1.2.0)
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
        $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

#########################################################################################
## CMake install configuration
#########################################################################################

install(TARGETS ${PROJECT_NAME}
        EXPORT ${export_name}Targets
        ARCHIVE DESTINATION "${CMAKE_INSTALL_LIBDIR}"
        LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}"
        RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}"
        FILE_SET HEADERS DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/ProjectA/Component3
        COMPONENT ${export_name}
)

install(EXPORT ${export_name}Targets
        FILE ${export_name}Targets.cmake
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${export_name}
        NAMESPACE ProjectA::
        COMPONENT ${export_name}
)

set_property(TARGET ${PROJECT_NAME} PROPERTY VERSION ${version})
set_property(TARGET ${PROJECT_NAME} PROPERTY SOVERSION 3)
set_property(TARGET ${PROJECT_NAME} PROPERTY INTERFACE_${PROJECT_NAME}_MAJOR_VERSION 3)
set_property(TARGET ${PROJECT_NAME} APPEND PROPERTY COMPATIBLE_INTERFACE_STRING ${PROJECT_NAME}_MAJOR_VERSION)

# generate the version file for the config file
write_basic_package_version_file(
        "${CMAKE_CURRENT_BINARY_DIR}/${export_name}ConfigVersion.cmake"
        VERSION "${version}"
        COMPATIBILITY AnyNewerVersion
)

configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
        "${CMAKE_CURRENT_BINARY_DIR}/${export_name}Config.cmake"
        INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${export_name}
)

install(FILES
        "${CMAKE_CURRENT_BINARY_DIR}/${export_name}Config.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/${export_name}ConfigVersion.cmake"
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${export_name}
        COMPONENT ${export_name}
)