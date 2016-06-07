from conans import ConanFile
import os
from conans.tools import download
from conans.tools import unzip
from conans import CMake

class tbbConan(ConanFile):
    name = "tbb"
    version = "4.4.20160526"
    ZIP_FOLDER_NAME = "tbb-%s" % version
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    url = "https://github.com/dwerner/conan-tbb"
    license ="https://github.com/google/googletest/blob/master/googletest/LICENSE"
    exports = "FindTbb.cmake", "change_dylib_names.sh"
    unzipped_name = "tbb44_20160526oss"
    zip_name = "%s_src.tgz" % unzipped_name

    def source(self):
        url = "https://www.threadingbuildingblocks.org/sites/default/files/software_releases/source/%s" % self.zip_name
        download(url, self.zip_name)
        unzip(self.zip_name)
        os.unlink(self.zip_name)

    def build(self):
        cd_build = "cd %s" % self.unzipped_name
        self.run("%s && make" % cd_build)

    def package(self):

        if self.settings.os == "Macos" and self.options.shared:
            self.run("bash ./change_dylib_names.sh")

        # Copy findtbb script into project
        self.copy("FindTbb.cmake", ".", ".")

        # Copying headers
        self.copy(pattern="*.h", dst="include/tbb", src="%s/include/tbb" % self.unzipped_name, keep_path=True)
        self.copy(pattern="*.h", dst="include/serial", src="%s/include/serial" % self.unzipped_name, keep_path=True)

        # Copying static and dynamic libs
        self.copy(pattern="*.a", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.dll", dst="bin", src=".", keep_path=False)
        self.copy(pattern="*.so*", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.dylib*", dst="lib", src=".", keep_path=False)      


    def package_info(self):
        self.cpp_info.libs = ['tbb']
