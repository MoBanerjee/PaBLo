# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:49:36 2023

@author: Aditya Somasundaram
"""

class TrackableObject:
	def __init__(self, objectID, centroid):
		# store the object ID, then initialize a list of centroids
		# using the current centroid
		self.objectID = objectID
		self.centroids = [centroid]
		# initialize a boolean used to indicate if the object has
		# already been counted or not
		self.counted = False