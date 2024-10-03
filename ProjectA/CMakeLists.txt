cmake_minimum_required(VERSION 3.29)
project(ProjectA)

set(CMAKE_CXX_STANDARD 20)

add_subdirectory(Component2)
add_subdirectory(Component1)
add_subdirectory(Component3)

# TODO adjust this to only search for requested components
file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
        "include(CMakeFindDependencyMacro)\n"
        "find_dependency(ProjectA_Component2 CONFIG REQUIRED)\n"
        "find_dependency(ProjectA_Component3 CONFIG REQUIRED)\n"
)

install(FILES "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
        DESTINATION share/${PROJECT_NAME}
        COMPONENT ${PROJECT_NAME}
)
