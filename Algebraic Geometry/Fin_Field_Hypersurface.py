#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Fin_Field_Hypersurface.py
#  
#  Copyright 2019 Ben Church <ben@ben-XPS-13-9360>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from collections import OrderedDict 
char = 2
total_degree = 4

def print_coeffs(coeffs):
	for key in coeffs:
		if coeffs[key] != 0:
			i = key[1]
			j = key[2]
			k = key[3]
			print coeffs[key], "x_0^", total_degree - i - j - k, "x_1^", i, " x_2^", j, " x_3^", k
	print ""

def eval_at(coeffs, pt):
	s = 0 
	for key in coeffs:
		l = key[0]
		i = key[1]
		j = key[2]
		k = key[3]
		s += coeffs[key] * pt[0]**l * pt[1]**i * pt[2]**j * pt[3]**k % char
	return s % char

def eval_deriv(coeffs, pt, n):
	s = 0 
	for key in coeffs:
		l = key[0]
		i = key[1]
		j = key[2]
		k = key[3]
		if n == 0 and l > 0:
			s += l * coeffs[key] * pt[0]**(l-1) * pt[1]**i * pt[2]**j * pt[3]**k % char
		elif n == 1 and i > 0:
			s += i * coeffs[key] * pt[0]**l * pt[1]**(i-1) * pt[2]**j * pt[3]**k % char
		elif n == 2 and j > 0:
			s += j * coeffs[key] * pt[0]**l * pt[1]**i * pt[2]**(j-1) * pt[3]**k % char
		elif n == 3 and k > 0:
			s += k * coeffs[key] * pt[0]**l * pt[1]**i * pt[2]**j * pt[3]**(k-1) % char
	return s % char
	
def check_smooth(coeffs):
	for a in range(char):
		for b in range(char):
			for c in range(char):
				for d in range(char):
					if not (a == 0 and b == 0 and c == 0 and d == 0):
						print (a,b,c,d), eval_at(coeffs, [a,b,c,d]), eval_deriv(coeffs, [a,b,c,d], 0), eval_deriv(coeffs, [a,b,c,d], 1), eval_deriv(coeffs, [a,b,c,d], 2), eval_deriv(coeffs, [a,b,c,d], 3)
						if eval_at(coeffs, [a,b,c,d]) == 0 and eval_deriv(coeffs, [a,b,c,d], 0) == 0 and eval_deriv(coeffs, [a,b,c,d], 1) == 0 and eval_deriv(coeffs, [a,b,c,d], 2) == 0 and eval_deriv(coeffs, [a,b,c,d], 3) == 0:
							print "not smooth at: ", [a,b,c,d]
							return 0
	return 1

def generate_monomials():
	l = list()
	for i in range(total_degree + 1):
		for j in range(total_degree + 1 - i):
			for k in range(total_degree + 1 - i - j):
				l.append((i,j,k, total_degree - i - j - k))
	return l

def get_digit(number, n):
    return number // 2**n % 2


def run():
	coeffs = OrderedDict()
	mon = generate_monomials()
	for num in range(1000000):
		i = 0
		for key in mon:
			coeffs[key] = get_digit(num, i)
			i += 1
		if check_smooth(coeffs):
			print_coeffs(coeffs)


def main(args):
	coeffs = OrderedDict()
	coeffs[(1,3,0,0)] = 1
	coeffs[(0,1,3,0)] = 1
	coeffs[(0,0,1,3)] = 1
	coeffs[(4,0,0,0)] = 1
	print_coeffs(coeffs)
	print eval_at(coeffs, [0,0,0,1])
	print eval_at(coeffs, [1,1,1,1]), eval_deriv(coeffs, [1,1,1,1], 0), eval_deriv(coeffs, [1,1,1,1], 1), eval_deriv(coeffs, [1,1,1,1], 2), eval_deriv(coeffs, [1,1,1,1], 3) 
	print check_smooth(coeffs)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
