project(LibraryComponent)

set(HEADERS
        Library.h
)

set(SOURCES
        Library.cpp
)

# Library
add_library(${PROJECT_NAME})
add_library(ProjectA::LayerA::${PROJECT_NAME} ALIAS ${PROJECT_NAME})
target_sources(${PROJECT_NAME} PUBLIC FILE_SET HEADERS FILES ${HEADERS})
target_sources(${PROJECT_NAME} PRIVATE ${SOURCES})

target_include_directories(${PROJECT_NAME} PUBLIC
        $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/..>
        $<INSTALL_INTERFACE:include>
)

target_link_libraries(${PROJECT_NAME} PUBLIC ProjectA::LayerA::HeaderOnlyComponent)

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