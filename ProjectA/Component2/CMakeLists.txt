cmake_minimum_required(VERSION 3.28)

project(Component2)

include(GNUInstallDirs)
include(CMakePackageConfigHelpers)

set(export_name ProjectA_${PROJECT_NAME})
set(version 1.1.1)
set(CMAKE_CXX_STANDARD 20)

find_package(spdlog REQUIRED CONFIG)

set(HEADERS
        LogSingleton.h
        LogWrapper.h
)

set(SOURCES
        temp.cpp
)

# Library
add_library(${PROJECT_NAME} ${SOURCES})
add_library(ProjectA::${PROJECT_NAME} ALIAS ${PROJECT_NAME})
target_sources(${PROJECT_NAME} PUBLIC FILE_SET HEADERS FILES ${HEADERS})

target_include_directories(${PROJECT_NAME} PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/../..>
        $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

# Dependencies
target_link_libraries(${PROJECT_NAME} PUBLIC spdlog::spdlog)

#########################################################################################
## CMake install configuration
#########################################################################################

install(TARGETS ${PROJECT_NAME}
        EXPORT ${export_name}Targets
        ARCHIVE DESTINATION "$<$<CONFIG:Debug>:debug/>${CMAKE_INSTALL_LIBDIR}"
        LIBRARY DESTINATION "$<$<CONFIG:Debug>:debug/>${CMAKE_INSTALL_LIBDIR}"
        RUNTIME DESTINATION "$<$<CONFIG:Debug>:debug/>${CMAKE_INSTALL_BINDIR}"
        FILE_SET HEADERS DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/ProjectA/Component2
        COMPONENT ${export_name}
)

install(EXPORT ${export_name}Targets
        FILE ${export_name}Targets.cmake
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/share/${export_name}
        NAMESPACE ProjectA::
        COMPONENT ${export_name}
)

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
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/share/${export_name}
        COMPONENT ${export_name}
)