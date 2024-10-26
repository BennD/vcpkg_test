project(LayerApps)
set(ExportName ${PROJECT_NAME}Targets)

add_subdirectory(App)

install(EXPORT ${ExportName}
        FILE ${ExportName}.cmake
        DESTINATION share/${CMAKE_PROJECT_NAME}
        NAMESPACE ${CMAKE_PROJECT_NAME}::${PROJECT_NAME}::
)