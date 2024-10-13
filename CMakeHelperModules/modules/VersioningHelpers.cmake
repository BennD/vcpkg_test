function(getPatchVersion OutputVariable)
    # Determine the VCS used
    execute_process(
            COMMAND git rev-parse --is-inside-work-tree
            WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
            RESULT_VARIABLE IsGitRepo
            OUTPUT_QUIET
            ERROR_QUIET
    )
    execute_process(
            COMMAND svn info --show-item revision
            WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
            RESULT_VARIABLE IsSvnRepo
            OUTPUT_QUIET
            ERROR_QUIET
    )

    # Set the patch version
    if (IsSvnRepo EQUAL "0")
        MESSAGE(DEBUG "Subversion repository found")
        execute_process(
                COMMAND svn info --show-item revision
                WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
                OUTPUT_VARIABLE ${OutputVariable}
                OUTPUT_STRIP_TRAILING_WHITESPACE
        )

    elseif (IsGitRepo EQUAL "0")
        MESSAGE(DEBUG "Git repository found")
        execute_process(
                COMMAND git log -1 --format=%H ${CMAKE_CURRENT_SOURCE_DIR}
                COMMAND xargs git rev-list --count
                WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
                OUTPUT_VARIABLE ${OutputVariable}
                OUTPUT_STRIP_TRAILING_WHITESPACE
        )

    else ()
        MESSAGE(WARNING "Can't determine patch version. VCS not found / supported.")
        set(${OutputVariable} "0")
    endif ()

    return(PROPAGATE ${OutputVariable})
endfunction()