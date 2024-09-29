#include <mutex>

#include "LogSingleton.h"
#include "LogWrapper.h"

std::mutex LogSingleton::m_mutex;
LogSingleton LogSingleton::m_instance;
