cmake_minimum_required(VERSION 3.28)

project(ProjectB)

if(NOT CMAKE_CXX_STANDARD)
	set(CMAKE_CXX_STANDARD 20)
endif()

find_package(spdlog REQUIRED CONFIG)
find_package(ProjectA REQUIRED CONFIG)

add_executable(${PROJECT_NAME} ProjectB/main.cpp)
target_link_libraries(ProjectB PRIVATE ProjectA::LayerSupport::LibraryComponent)
