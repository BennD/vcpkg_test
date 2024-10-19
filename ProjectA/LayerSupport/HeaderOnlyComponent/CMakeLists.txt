project(HeaderOnlyComponent)

find_package(spdlog REQUIRED CONFIG)

set(HEADERS
        LogSingleton.h
        LogWrapper.h
)

# Library
add_library(${PROJECT_NAME} INTERFACE)
add_library(ProjectA::LayerA::${PROJECT_NAME} ALIAS ${PROJECT_NAME})
target_sources(${PROJECT_NAME} INTERFACE FILE_SET HEADERS FILES ${HEADERS})

target_include_directories(${PROJECT_NAME} INTERFACE
        $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/..>
        $<INSTALL_INTERFACE:include>
)

# Dependencies
target_link_libraries(${PROJECT_NAME} INTERFACE spdlog::spdlog)

#########################################################################################
## CMake install configuration
#########################################################################################

install(TARGETS ${PROJECT_NAME}
        EXPORT ${ExportName}
        ARCHIVE DESTINATION lib/$<CONFIG>
        LIBRARY DESTINATION lib/$<CONFIG>
        RUNTIME DESTINATION bin/$<CONFIG>
        FILE_SET HEADERS DESTINATION include/ProjectA/LayerSupport/${PROJECT_NAME}
)