#include <ProjectA/LayerSupport/HeaderOnlyComponent/LogSingleton.h>
#include <ProjectA/LayerSupport/LibraryComponent/Library.h>

#include <thread>

int main() {
    std::thread t1([] {
        int a = 100;
        const auto logger = LogSingleton::createLogger("MainTask");
        while (a >= 0) {
            SPDLOG_LOGGER_INFO(logger, "No more!");
            std::this_thread::sleep_for(std::chrono::milliseconds(1));
            a--;
        }
    });
    std::thread t2([] {
        int a = 100;
        const auto logger = LogSingleton::createLogger("Kirk");
        while (a >= 0) {
            SPDLOG_LOGGER_WARN(logger, "Arghhh!");
            std::this_thread::sleep_for(std::chrono::milliseconds(1));
            a--;
        }
    });
    std::thread t3([] {
        int a = 100;
        const auto logger = LogSingleton::createLogger("Ero");
        while (a >= 0) {
            SPDLOG_LOGGER_ERROR(logger, "Logging in {}", "test");
            std::this_thread::sleep_for(std::chrono::milliseconds(1));
            a--;
        }
    });
    std::thread t4([] {
        int a = 100;
        while (a >= 0) {
            simpleLog("Simple log using LibraryComponent");
            std::this_thread::sleep_for(std::chrono::milliseconds(1));
            a--;
        }
    });

    t1.join();
    t2.join();
    t3.join();
    t4.join();
}
