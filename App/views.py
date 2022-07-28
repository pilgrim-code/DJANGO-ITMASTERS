from msilib.schema import File
from django.shortcuts import redirect, render,HttpResponse
from django.http import HttpResponseRedirect
from matplotlib.cbook import file_requires_unicode
import pandas as pd

import tensorflow as tf
import re
from django.core.files.storage import FileSystemStorage

class FotoIA():
    from keras.models import load_model
    from keras.preprocessing import image
    import json 
    
    
    import tensorflow as tf
    gpuoptions = tf.compat.v1.GPUOptions(allow_growth=True)
    session = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(gpu_options=gpuoptions))
    def list_IA(request):
        return render(request,'ias.html')
   
    def index(request):
        context={'a':1}
        return render(request,'fotoia.html',context)
    def predictImage(request):
        from keras.models import load_model
        import tensorflow as tf
        import keras
        
        from keras.preprocessing import image
      
        import json 
        from tensorflow import Graph
        img_height,img_width =224,224
        with open('App\Models\imagenet_classes.json','r')as f:
            labelInfo=f.read()
        labelInfo=json.loads(labelInfo)
        model_graph = Graph()
    
        modeloF=load_model('App\Models\MobileNetModelImagenet.h5')    
    
        
        img_height,img_width =224,224
        
        print(request)
        print(request.POST.dict())
        fileObj= request.FILES['filePath']
        fs = FileSystemStorage()
        filePathName = fs.save(fileObj.name,fileObj)
        filePathName = fs.url(filePathName)
        testimage ='.'+filePathName
        img = tf.keras.utils.load_img(testimage, target_size=(img_height, img_width))
        x = tf.keras.preprocessing.image.img_to_array(img)
        x=x/255
        x=x.reshape(1,img_height, img_width,3)
       
        predi=modeloF.predict(x)
        
        import numpy as np
        predictedLabel=labelInfo[str(np.argmax(predi[0]))]

        context={'filePathName':filePathName,'predictedLabel':predictedLabel[1]}
        return render(request,'fotoia.html',context) 
       
class IA():
   
    def homeia(request):
        return render(request,"ia.html")
    '''def resultia(request):
        
        model = load_model('modelo_shippuden.h5')
        
        lis = []
        lis.append(request.GET['Input'])
        print(lis)
        
        ans = model.predict([lis])
        return render(request,"resultia.html",{'ans':ans})
    '''
    def predict_class(request):
        from keras.models import load_model
        model = load_model('modelo_shippuden.h5')
        lis = []
        lis.append(request.GET['Input'])
        
        from keras.preprocessing.text import Tokenizer

        from keras_preprocessing.sequence import pad_sequences
        ''' predecimos por texto que sentimiento es'''
        
        sentiment_classes = ['Negativo', 'Positivo']
        max_len=1000
        # Text token
        tokenizer = Tokenizer(num_words=1000, lower=True, split=' ')
        
        # Pasar a integet
       
    
        # 
        xt = tokenizer.texts_to_sequences(lis)
        # 
        xt = pad_sequences(xt, padding='post', maxlen=max_len)
        # 
        yt = model.predict(xt).argmax(axis=1)
        # 
        ans = sentiment_classes[yt[0]]
        print('Este sentimiento es: ', sentiment_classes[yt[0]])
        return render(request,"resultia.html",{'ans':ans})
    
# Create your views here.
