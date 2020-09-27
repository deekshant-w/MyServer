import glob
import os
from random import randint
from urllib.parse import urlencode

def extension(file):
	return file.split('.')[-1]

def condenseFiles(fileDir):
	# files -> audio -> []0 -> relativeUrl,modifiedTime
	files = {
		'audio' : [],
		'video' : [],
		'pdf' 	: [],
		'other' : []
	}
	extensions = {
		'audio' : ['3gp', 'aa', 'aac', 'aax', 'act', 'aiff', 'alac', 'amr', 'ape', 'au', 'awb', 'dct', 'dss', 'dvf', 'flac', 'gsm', 'iklax', 'ivs', 'm4a', 'm4b', 'm4p', 'mmf', 'mp3', 'mpc', 'msv', 'nmf', 'ogg', 'oga', 'mogg', 'opus', 'ra', 'rm', 'raw', 'rf64', 'sln', 'tta', 'voc', 'vox', 'wav', 'wma', 'wv', 'webm', '8svx', 'cda'],
		'video' : ['webm', 'mkv', 'flv', 'flv', 'vob', 'ogv', 'ogg', 'drc', 'gif', 'gifv', 'mng', 'avi', 'mts', 'm2ts', 'ts', 'mov', 'qt', 'wmv', 'yuv', 'rm', 'rmvb', 'viv', 'asf', 'amv', 'mp4', 'm4p', 'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'mpg', 'mpeg', 'm2v', 'm4v', 'svi', '3gp', '3g2', 'mxf', 'roq', 'nsv', 'flv', 'f4v', 'f4p', 'f4a', 'f4b']
	}

	allfiles = glob.glob(f'{fileDir}\\**/*.*',recursive=True)

	for file in allfiles:
		mtime = os.path.getctime(file)
		fileType = None
		fileName = file.replace(fileDir,'').replace('\\','/')[1:]
		filePath = 'static/'+file.replace(fileDir,'').replace('\\','/')[1:]
		if(extension(file) in extensions['audio']):
			fileType = 'audio'
			filePath = f'./{fileType}Preview?' + urlencode({'v':fileName})
		elif(extension(file) in extensions['video']):
			fileType = 'video'
			filePath = f'./{fileType}Preview?' + urlencode({'v':fileName})
		elif(extension(file)=='pdf'):
			fileType = 'pdf'
		else:
			fileType = 'other'
		
		files[fileType].append({
				'relativeUrl' 	: filePath,
				'fileName' 		: fileName,
				'modifiedTime' 	: mtime,
				'class' 		: f'imageColor{randint(1,10)}',
			})

	data = {}
	for fileType in files:
		data[fileType] = sorted(files[fileType],key=lambda x:x['modifiedTime'],reverse=True)

	rowFactor = 6
	rowFactor+= 1 
	files = {
		'audio' : [],
		'video' : [],
		'pdf' 	: [],
		'other' : []
	}
	for fileType in files:
		row = []
		count = 1
		for file in data[fileType]:
			if(count%rowFactor):
				row.append(file)
			else:
				files[fileType].append(row)
				row = []
				row.append(file)
				count = 1
			count+=1
		if(row):
			files[fileType].append(row)

	return(files)

# print(condenseFiles(r'C:\Users\Deekshant\Desktop\myServer\data'))