#pragma once

class LogWrapper {
public:
    explicit LogWrapper(std::shared_ptr<spdlog::logger> logger) : m_logger(std::move(logger)) {
        if (!m_logger) {
            throw std::runtime_error("Logger initialization failed");
        }
    }

    [[nodiscard]] const std::shared_ptr<spdlog::logger> &operator->() const {
        return m_logger;
    }

    [[nodiscard]] spdlog::logger &operator*() const {
        return *m_logger;
    }

private:
    std::shared_ptr<spdlog::logger> m_logger;
};
