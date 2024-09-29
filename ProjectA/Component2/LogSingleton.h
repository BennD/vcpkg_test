#pragma once

#include <memory>
#include <spdlog/spdlog.h>
#include <spdlog/sinks/stdout_color_sinks.h>

#include "LogWrapper.h"

class LogSingleton {
    LogSingleton()
        : m_stdout_sink(std::make_shared<spdlog::sinks::stdout_color_sink_mt>()) {
    }

    static LogSingleton &instance() {
        return m_instance;
    }

public:
    static LogWrapper createLogger(const std::string &taskName) {
        const auto logger = std::make_shared<spdlog::logger>(taskName);

        logger->sinks().emplace_back(instance().m_stdout_sink);

        spdlog::register_logger(logger);

        return LogWrapper(logger);
    }

private:
    static std::mutex m_mutex;
    static LogSingleton m_instance;

    std::shared_ptr<spdlog::sinks::stdout_color_sink_mt> m_stdout_sink;
};
