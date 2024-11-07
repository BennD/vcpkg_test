from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class ProjectA(ConanFile):
    name = "projecta-trunk"
    version = "1.0.0"

    # Metadata
    license = "MIT"
    author = "Benno Doerr bencayd@gmail.com"
    url = "https://github.com/BennD/vcpkg_test/tree/main/ProjectARepository"
    description = "Despite the name, this is a testing project for cmake and package managers"
    topics = ("cmake", "c++")

    # Settings
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    exports_sources = ["CMakeLists.txt", "Config.cmake.in", "ProjectA/*"]

    def requirements(self):
        self.requires("spdlog/1.14.1", transitive_headers=True)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.user_presets_path = False
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def layout(self):
        cmake_layout(self, build_folder="conan-build")

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        # No information provided, only the in-package .cmake is used here
        # Other build systems or CMake via CMakeDeps will fail
        self.cpp_info.builddirs = ["share/ProjectA"]
        self.cpp_info.set_property("cmake_find_mode", "none")
