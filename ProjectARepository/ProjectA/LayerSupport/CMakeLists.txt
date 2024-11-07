project(LayerSupport)
set(ExportName ${PROJECT_NAME}Targets)

add_subdirectory(HeaderOnlyComponent)
add_subdirectory(LibraryComponent)

install(EXPORT ${ExportName}
        FILE ${ExportName}.cmake
        DESTINATION share/${CMAKE_PROJECT_NAME}
        NAMESPACE ${CMAKE_PROJECT_NAME}::${PROJECT_NAME}::
)