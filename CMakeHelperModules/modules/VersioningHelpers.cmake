function(getPatchVersion OutputVariable)
    # Subversion
    if (EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/.svn")
        MESSAGE(STATUS "Subversion found")
        execute_process(
                COMMAND svn info --show-item revision
                OUTPUT_VARIABLE ${OutputVariable}
                OUTPUT_STRIP_TRAILING_WHITESPACE
        )

        # Git
    elseif (EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/.git")
        MESSAGE(STATUS "Git found")
        execute_process(
                COMMAND git log -1 --format=%H ${CMAKE_CURRENT_SOURCE_DIR}
                COMMAND xargs git rev-list --count
                OUTPUT_VARIABLE ${OutputVariable}
                OUTPUT_STRIP_TRAILING_WHITESPACE
        )

        # Not supported
    else ()
        MESSAGE(WARNING "Can't determine patch version. VCS not found / supported.")
        set(${OutputVariable} "0")
    endif ()

    return(PROPAGATE ${OutputVariable})
endfunction()