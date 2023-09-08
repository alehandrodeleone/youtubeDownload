from django.shortcuts import render
from pytube import YouTube
from django.http import FileResponse
from .models import *




def download_video(request):
    if request.method == 'POST':
        video_url = request.POST.get('video_url')
        save_link=links(Links=video_url)
        save_link.save()
        try:
            yt = YouTube(video_url)#получаем ссылку на видео из поля ввода
            stream = yt.streams.get_highest_resolution()#выбираем наивысшее разрешение и перелаем в переменную stream
            
            video_path = stream.download()#Используя метод download() объекта stream, скачиваем видео и сохраняем его в локальный файл с именем video_path.
            video_file = open(video_path, 'rb')#Открываем скачанный файл видео в двоичном режиме и сохраняем его в переменную video_file.
            
            response = FileResponse(video_file)#Создаем объект FileResponse, который будет использоваться для отправки файла видео в ответе сервера
            response['Content-Disposition'] = 'attachment; filename="video.mp4"'#Устанавливаем заголовок Content-Disposition для указания, что содержимое ответа должно быть вложенным файлом с именем "video.mp4".
       
            return response #Возвращаем обьект который оправляет фаил на скачивание
  
        except Exception as e:
            error_message = f'Ошибка при скачивании видео: {str(e)}'
            return render(request, 'start_page.html', {'error_message': error_message})
    
    return render(request, 'start_page.html')

def api_page(request):
    return render(request,"api.html")

from rest_framework.generics import ListAPIView,RetrieveAPIView
from .serializers import list_serializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from .permissions import *
class Custom_pagination(PageNumberPagination):
    page_size = 4
    max_page_size = 100
    page_size_query = 'page_size'

class api_list(ListAPIView):
    queryset = links.objects.all()
    serializer_class = list_serializer
    pagination_class = Custom_pagination
    

class api_retrive(RetrieveAPIView):
    queryset = links.objects.all()
    serializer_class = list_serializer

class api_Crud(ModelViewSet):
    queryset = links.objects.all()
    serializer_class = list_serializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]



