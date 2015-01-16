#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import urllib

from jp.ac.kyoto_su.cse.sh.MVC.Model import OpenGLModel
from jp.ac.kyoto_su.cse.sh.Parts.Polygon import OpenGLPolygon

TRACE = True
DEBUG = False

class DragonModel(object):
	"""ドラゴンのモデル。"""
	
	def __init__(self):
		"""ドラゴンのモデルのコンストラクタ。"""
		if TRACE: print __name__, self.__init__.__doc__
		
		self._triangles = []
		self._eye_point = [-5.5852450791872 , 3.07847342734 , 15.794105252496]
		self._sight_point = [0.27455347776413 , 0.20096999406815 , -0.11261999607086]
		self._up_vector = [0.1018574904194 , 0.98480906061847 , -0.14062775604137]
		self._fovy = 12.642721790235
		self._display_list = None
		self._view = None
		
		filename = os.path.join(os.getcwd(), 'dragon.txt')
		if os.path.exists(filename) and os.path.isfile(filename):
			pass
		else:
			url = 'http://www.cc.kyoto-su.ac.jp/~atsushi/Programs/Dragon/dragon.txt'
			urllib.urlretrieve(url, filename)
		
		with open(filename, "rU") as a_file:
			while True:
				a_string = a_file.readline()
				if len(a_string) == 0: break
				a_list = a_string.split()
				if len(a_list) == 0: continue
				first_string = a_list[0]
				if first_string == "number_of_vertexes":
					number_of_vertexes = int(a_list[1])
				if first_string == "number_of_triangles":
					number_of_triangles = int(a_list[1])
				if first_string == "end_header":
					vertexes = []
					for n in range(number_of_vertexes):
						a_string = a_file.readline()
							a_vertex = map(float, a_string.split())
							vertexes.append(a_vertex)
					for n in range(number_of_triangles):
						a_string = a_file.readline()
							indexes = map(int, a_string.split())
							vertex = map((lambda index: vertexes[index-1]),indexes)
							a_triangle = DragonTriangle(*vertex)
							self._triangles.append(a_triangle)
		return

def default_window_title(self):
	"""ドラゴンのウィンドウのタイトル(ラベル)を応答する。"""
		if TRACE: print __name__, self.default_window_title.__doc__
		
		return "Dragon"




