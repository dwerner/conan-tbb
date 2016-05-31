# Try to find hiredis
# Once done, this will define
#
# TBB_FOUND        - system has hiredis
# TBB_INCLUDE_DIRS - hiredis include directories
# TBB_LIBRARIES    - libraries need to use hiredis

find_path(
	TBB_INCLUDE_DIR
	NAMES tbb.h
	PATHS ${CONAN_INCLUDE_DIRS_TBB}
	)

find_library(
	TBB_LIBRARY
	NAMES tbb 
	PATHS ${CONAN_LIB_DIRS_TBB}
	)

set(TBB_FOUND TRUE)
set(TBB_INCLUDE_DIRS ${TBB_INCLUDE_DIR})
set(TBB_LIBRARIES ${TBB_LIBRARY})

mark_as_advanced(TBB_LIBRARY TBB_INCLUDE_DIR)
