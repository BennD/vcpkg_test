cmake_minimum_required(VERSION 3.29)
project(ProjectA_Component3)

include(GNUInstallDirs)

set(CMAKE_CXX_STANDARD 20)

set(HEADERS
        helper.h
)

set(SOURCES
        helper.cpp
)

# Library
add_library(${PROJECT_NAME} ${SOURCES})
target_sources(${PROJECT_NAME} PUBLIC FILE_SET HEADERS FILES ${HEADERS})

target_include_directories(${PROJECT_NAME} PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/../..>
        $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

install(TARGETS ${PROJECT_NAME}
        EXPORT ${PROJECT_NAME}Targets
        ARCHIVE DESTINATION "${CMAKE_INSTALL_LIBDIR}"
        LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}"
        RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}"
        FILE_SET HEADERS DESTINATION include/ProjectA/Component3
)

install(EXPORT ${PROJECT_NAME}Targets
        FILE ${PROJECT_NAME}Targets.cmake
        DESTINATION share/${PROJECT_NAME}
)

file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
        "include(CMakeFindDependencyMacro)\n"
        "include(\"\${CMAKE_CURRENT_LIST_DIR}/${PROJECT_NAME}Targets.cmake\")\n"
)

install(FILES "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
        DESTINATION share/${PROJECT_NAME})