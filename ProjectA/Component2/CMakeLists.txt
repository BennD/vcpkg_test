cmake_minimum_required(VERSION 3.29)
project(Component2)

include(GNUInstallDirs)

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
add_library(Component2 ${SOURCES})
add_library(ProjectA::Component2 ALIAS Component2)
target_sources(Component2 PUBLIC FILE_SET HEADERS FILES ${HEADERS})

target_include_directories(Component2 PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/../..>
        $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

# Dependencies
target_link_libraries(Component2 PUBLIC spdlog::spdlog)

install(TARGETS Component2
        EXPORT Component2Targets
        ARCHIVE DESTINATION "${CMAKE_INSTALL_LIBDIR}"
        LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}"
        RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}"
        FILE_SET HEADERS DESTINATION include/ProjectA/Component2
)

install(EXPORT Component2Targets
        FILE Component2Targets.cmake
        NAMESPACE ProjectA::
        DESTINATION share/Component2
)

file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/Component2Config.cmake"
        "include(CMakeFindDependencyMacro)\n"
        "find_dependency(spdlog CONFIG REQUIRED)\n"
        "include(\"\${CMAKE_CURRENT_LIST_DIR}/Component2Targets.cmake\")\n"
)

install(FILES "${CMAKE_CURRENT_BINARY_DIR}/Component2Config.cmake"
        DESTINATION share/Component2)