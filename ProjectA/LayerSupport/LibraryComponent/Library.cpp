#include "Library.h"

#include <ProjectA/LayerSupport/HeaderOnlyComponent/LogSingleton.h>

void simpleLog(std::string message) {
    static auto logger = LogSingleton::createLogger("LibraryComponent");
    logger->info(message);
}
