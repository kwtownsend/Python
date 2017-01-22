#!/usr/bin/python

# author: Kendall Townsend
# email: kendallcar@csu.fullerton.edu
# description: this file implements the park and miller prng formula z=(a * z) % m with a = minimum m = maximum and z is the seed

import math, time, random, getopt
 
class MyPRNG:
    #didn't want to use getopts because i'm unfamiliar with the operation and this is the only way I could get it work even though you requested a zero-arg constructor
    def __init__(self, low = 0, high = 0):
        self.m_min = low
        self.m_max = high

 
    def seed(self, seed):
    #  Seed the generator with 'seed'
        self.m_seed = seed
 
    def next_prn(self):
    #     Return the next random number using an algorithm based on the
    #        Park & Miller paper "RANDOM NUMBER GENERATORS: GOOD ONES ARE
    #        HARD TO FIND"
        a = 16807
        m = 2147483647
	
    #use test to make sure seed can never hit zero
        test = (a * self.m_seed) % m
	while(test == 0):
		self.m_seed += 1
		test = ( a * self.m_seed) % m


	self.m_seed = (a * self.m_seed) % m
	if(self.m_seed < self.m_min):
		self.m_seed += self.m_min
	if(self.m_seed > self.m_max):
		self.m_seed = self.m_seed % self.m_max
	return self.m_seed
