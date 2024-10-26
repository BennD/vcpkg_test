from conan import ConanFile

import subprocess
import os
import re


class AConanFile(ConanFile):
    branch = None
    conanfile = None

    def __init__(self, display_name=""):
        super().__init__(display_name)
        if self.conanfile is None:
            raise ValueError("`conanfile` must be set in the derived class. Add `Conanfile.conanfile = __file__`")
        self.version = self.get_version()

    def get_version(self):
        try:
            root = os.path.dirname(self.conanfile)
            cmake_file = os.path.join(root, "CMakeLists.txt")
            version = extract_version_from_cmake(cmake_file)
            patch = self.get_patch_version(root)
            return f"{version}-{self.branch}.{patch}" if self.branch is not None else f"{version}.{patch}"

        except Exception as e:
            self.output.error(f"ERROR: Could not extract version from CMakeLists.txt: {e}")
            return "0.0.0"

    def get_patch_version(self, root):
        is_git_repo = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        ).returncode == 0

        is_svn_repo = subprocess.run(
            ["svn", "info", "--show-item", "revision"],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        ).returncode == 0

        if is_svn_repo:
            result = subprocess.run(
                ["svn", "info", "--show-item", "revision"],
                cwd=root,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            return result.stdout.decode().strip()

        elif is_git_repo:
            result = subprocess.run(
                ["git", "log", "-1", "--format=%H"],
                cwd=root,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            commit_hash = result.stdout.decode().strip()
            result = subprocess.run(
                ["git", "rev-list", "--count", commit_hash],
                cwd=root,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            return result.stdout.decode().strip()

        else:
            self.output.error("Can't determine patch version. VCS not found / supported.")
            return "0"


def extract_version_from_cmake(cmake_file):
    with open(cmake_file, "r") as f:
        return re.search(r"project\(.* VERSION ([\d.]+).*\)", f.read()).group(1)
