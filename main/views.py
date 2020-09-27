from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import customFunctions

#audio-file.png
resourceData = customFunctions.condenseFiles(settings.EXT_VARIABLES['projectDir'])

def mainPage(request):
	return render(request,'main/index.html',{})

def basicFlow(request):
	return JsonResponse(settings.EXT_VARIABLES)

def previewPage(request):
	context = {
		'data' 	: 0,
		'type'	: 'Unknown',
	}
	print(resourceData)
	if(request.method=='GET'):
		print(request.GET)
		page = request.GET.get('f')
		if(page):
			context['type'] = page
			if(page in resourceData):
				if(resourceData[page]):
					context['data'] = 1
					context['files'] = resourceData[page]
					context['icon'] = page+'-f.png'
	return render(request, 'main/preview.html',context)

def videoPreview(request):
	context = {}
	if(request.method=='GET'):
		context['fileName'] = request.GET.get('v')
		print(request.GET)
	return render(request,'main/videoPreview.html',context)

def audioPreview(request):
	context = {}
	if(request.method=='GET'):
		context['fileName'] = request.GET.get('v')
		print(request.GET)
	return render(request,'main/audioPreview.html',context)
