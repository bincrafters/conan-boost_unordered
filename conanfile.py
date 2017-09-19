from conans import ConanFile, tools, os

class BoostUnorderedConan(ConanFile):
    name = "Boost.Unordered"
    version = "1.65.1"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-unordered"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["unordered"]
    requires =  "Boost.Assert/1.65.1@bincrafters/stable", \
                      "Boost.Config/1.65.1@bincrafters/stable", \
                      "Boost.Container/1.65.1@bincrafters/stable", \
                      "Boost.Core/1.65.1@bincrafters/stable", \
                      "Boost.Detail/1.65.1@bincrafters/stable", \
                      "Boost.Functional/1.65.1@bincrafters/stable", \
                      "Boost.Iterator/1.65.1@bincrafters/stable", \
                      "Boost.Move/1.65.1@bincrafters/stable", \
                      "Boost.Predef/1.65.1@bincrafters/stable", \
                      "Boost.Preprocessor/1.65.1@bincrafters/stable", \
                      "Boost.Smart_Ptr/1.65.1@bincrafters/stable", \
                      "Boost.Throw_Exception/1.65.1@bincrafters/stable", \
                      "Boost.Tuple/1.65.1@bincrafters/stable", \
                      "Boost.Type_Traits/1.65.1@bincrafters/stable"

                      #assert1 config0 container7 core2 detail5 functional5 iterator5 move3 predef0 preprocessor0 smart_ptr4 throw_exception2 tuple4 type_traits3

    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()