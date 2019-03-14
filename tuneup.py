#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "jhoelzer"

import cProfile
import pstats
import timeit


def profile(func):
    """A function that can be used as a decorator to meausre performance"""
    def profile_function(*args, **kwargs):
        prof = cProfile.Profile()
        prof.enable()
        result = func(*args, **kwargs)
        prof.disable()
        sort_by = 'cumulative'
        prof_stats = pstats.Stats(prof).sort_stats(sort_by)
        prof_stats.print_stats()
        return result
    return profile_function


def read_movies(src):
    """Read a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Case insensitive search within a list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicate_movies = []
    movie_dict = {}
    for movie in movies:
        if movie in movie_dict:
            duplicate_movies.append(movie)
        else:
            movie_dict[movie] = None
    return duplicate_movies


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer("find_duplicate_movies('movies.txt')",
                     setup='from __main__ import find_duplicate_movies')
    repeat = 7
    number = 3
    result = t.repeat(repeat=repeat, number=number)
    print('Best time across {} repeats of {} runs per repeat: {} sec'.format(
        repeat, number, result))


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    timeit_helper()
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
