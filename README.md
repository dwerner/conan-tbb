[![Build Status](https://travis-ci.org/dwerner/conan-tbb.svg)](https://travis-ci.org/dwerner/conan-tbb)


# conan-tbb

[Conan.io](https://conan.io) package for tbb library

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py
    
## Upload packages to server

    $ conan upload tbb/4.4.20160526@dwerner/stable --all
    
## Reuse the packages

### Basic setup

    $ conan install tbb/4.4.20160526@dwerner/stable
    
### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    tbb/4.4.20160526@dwerner/testing

    [options]
    tbb:shared=true # false
    
    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.
