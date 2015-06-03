#coding=utf-8
from numpy import *
import operator
import os
from PIL import Image

hwLabels = []
trainingMat = zeros((0,0))

def kNNClassify(inputX):
		dataSetSize = trainingMat.shape[0]
		
		diffMat = tile(inputX, (dataSetSize, 1)) - trainingMat
		sqDiffMat = diffMat ** 2
		sqDistances = sqDiffMat.sum(axis=1)
		distances = sqDistances ** 0.5

		sortedDistance = distances.argsort()
		classCount = {}
		for i in xrange(3):
			voteLabel = hwLabels[sortedDistance[i]]
			classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
		res = max(classCount)
		return res

def img2vec(filename):
	vec = zeros((1,400))
	im = Image.open(filename)
	pixdata = im.load()
	for i in xrange(20):
		for j in xrange(20):
			vec[0, 20*i+j] = pixdata[j, i]
	return vec

def createDataSet():
	global hwLabels
	global trainingMat
	trainingFileList = os.listdir('dataSet')
	m = len(trainingFileList)
	trainingMat = zeros((m,400))
	for i in range(m):
	    fileName = trainingFileList[i]
	    fileStr = fileName.split('.')[0]
	    classNumStr = fileStr.split('_')[0]
	    hwLabels.append(classNumStr)
	    trainingMat[i,:] = img2vec('dataSet/'+fileName)
	# testFileList = os.listdir(testFloder)
	# errorCount = 0.0
	# mTest = len(testFileList)
	# for i in range(mTest):
	#     fileName = testFileList[i]
	#     fileStr = fileName.split('.')[0]
	#     classNumStr = int(fileStr.split('_')[0])
	#     vectorUnderTest = img2vec(testFloder+'/'+fileName)
	#     classifierResult = kNNclassify(vectorUnderTest, trainingMat, hwLabels, K)
	#     #print classifierResult,' ',classNumStr
	#     if classifierResult != classNumStr:
	#         errorCount +=1
	# print 'tatal error ',errorCount
	# print 'error rate',errorCount/mTest

def getResult():
	resultStr = ''
	result = 0
	for i in range(1, 6):
		filename = 'crop' + str(i) + '.jpg'
		vectorUnderTest = img2vec(filename)
		classifierResult = kNNClassify(vectorUnderTest)
		resultStr += classifierResult

	if resultStr[1] == 'x':
		result += int(resultStr[0]) * int(resultStr[2])
		if resultStr[3] == 'x':
			result *= int(resultStr[4])
		elif resultStr[3] == '+':
			result += int(resultStr[4])
		elif resultStr[3] == '-':
			result -= int(resultStr[4])
		return result
	if resultStr[3] == 'x':
		result += int(resultStr[2]) * int(resultStr[4])
		if resultStr[1] == 'x':
			result *= int(resultStr[0])
		elif resultStr[1] == '+':
			result += int(resultStr[0])
		elif resultStr[1] == '-':
			result = int(resultStr[0]) - result
		return result
	if resultStr[1] == '+':
		result += int(resultStr[0]) + int(resultStr[2])
		if resultStr[3] == '+':
			result += int(resultStr[4])
		elif resultStr[3] == '-':
			result -= int(resultStr[4])
	elif resultStr[1] == '-':
		result += int(resultStr[0]) - int(resultStr[2])
		if resultStr[3] == '+':
			result += int(resultStr[4])
		elif resultStr[3] == '-':
			result -= int(resultStr[4])
	return result

def main():
	createDataSet()
	test()

if __name__ == '__main__':
	main()

