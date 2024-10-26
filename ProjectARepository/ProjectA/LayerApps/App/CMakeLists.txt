project(App)

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE ProjectA::LayerA::LibraryComponent)

#########################################################################################
## CMake install configuration
#########################################################################################

install(TARGETS ${PROJECT_NAME}
        EXPORT ${ExportName}
        ARCHIVE DESTINATION lib/$<CONFIG>
        LIBRARY DESTINATION lib/$<CONFIG>
        RUNTIME DESTINATION bin/$<CONFIG>
)
