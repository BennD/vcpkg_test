cmake_minimum_required(VERSION 3.29)
project(ProjectA_Component2)

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
add_library(${PROJECT_NAME} ${SOURCES})
target_sources(${PROJECT_NAME} PUBLIC FILE_SET HEADERS FILES ${HEADERS})

target_include_directories(${PROJECT_NAME} PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/../..>
        $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

# Dependencies
target_link_libraries(${PROJECT_NAME} PUBLIC spdlog::spdlog)

install(TARGETS ${PROJECT_NAME}
        EXPORT ${PROJECT_NAME}Targets
        ARCHIVE DESTINATION "${CMAKE_INSTALL_LIBDIR}"
        LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}"
        RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}"
        FILE_SET HEADERS DESTINATION include/ProjectA/Component2
        COMPONENT ${PROJECT_NAME}
)

install(EXPORT ${PROJECT_NAME}Targets
        FILE ${PROJECT_NAME}Targets.cmake
        DESTINATION share/${PROJECT_NAME}
        COMPONENT ${PROJECT_NAME}
)

file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
        "include(CMakeFindDependencyMacro)\n"
        "find_dependency(spdlog CONFIG REQUIRED)\n"
        "include(\"\${CMAKE_CURRENT_LIST_DIR}/${PROJECT_NAME}Targets.cmake\")\n"
)

install(FILES "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
        DESTINATION share/${PROJECT_NAME}
        COMPONENT ${PROJECT_NAME}
)