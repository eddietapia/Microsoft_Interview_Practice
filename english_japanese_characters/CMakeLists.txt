cmake_minimum_required(VERSION 3.6)
project(english_japanese_characters)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp)
add_executable(english_japanese_characters ${SOURCE_FILES})