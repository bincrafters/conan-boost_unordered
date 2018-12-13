#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostUnorderedConan(base.BoostBaseConan):
    name = "boost_unordered"
    url = "https://github.com/bincrafters/conan-boost_unordered"
    lib_short_names = ["unordered"]
    header_only_libs = ["unordered"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_container",
        "boost_container_hash",
        "boost_core",
        "boost_detail",
        "boost_move",
        "boost_predef",
        "boost_preprocessor",
        "boost_smart_ptr",
        "boost_throw_exception",
        "boost_tuple",
        "boost_type_traits"
    ]
