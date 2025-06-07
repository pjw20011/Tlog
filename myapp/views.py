# myapp/views.py
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from io import BytesIO
import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from matplotlib import rc
from matplotlib.ticker import MaxNLocator
import platform
import matplotlib.pyplot as plt
from PIL import Image
import re
import numpy as np
from wordcloud import WordCloud
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from .models import Main_Crawling, User_Table
import json
nltk.download('punkt')
from django.contrib.auth.decorators import login_required
from .models import User_Table

def life_graph(request):
    stop_word = set(stopwords.words('english'))

    fd_category = {}

    # 지정한 카테고리로 필터링
    category = '라이프'
    
    # 데이터베이스에서 데이터를 가져온 후, 리스트 형태로 변환
    category_data_db = list(Main_Crawling.objects.filter(category=category).values())

    # category_data_db에서 category와 일치하는 데이터 선택
    category_data = [row['subtopic'] for row in category_data_db if row['category'] == category]

    tokens = [word.lower() for sublist in [word_tokenize(d) for d in category_data] for word in sublist]

    fd_category = nltk.FreqDist(tokens)

    # 그래프 출력
    if platform.system() == 'Windows':
        rc('font', family='Malgun Gothic')
    elif platform.system() == 'Darwin':  
        rc('font', family='AppleGothic')
    else:  # Linux
        rc('font', family='NanumGothic')

    fig, ax = plt.subplots(figsize=(4, 4))

    ax.plot(*zip(*fd_category.items()), linestyle='-', marker='o', markersize=4, linewidth=1, color='#FF5733')
    ax.set_title(f'{category} Category')
    ax.set_xlabel('Word')
    ax.set_ylabel('Frequency')
    plt.subplots_adjust(top=0.9, bottom=0.25, left=0.2, right=0.9)

    ax.set_xticks(range(len(fd_category)))
    ax.set_xticklabels(fd_category.keys(), rotation='vertical')
    ax.grid(linestyle="--")
    ax.set_xlim(left=0)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    

    plt.tight_layout()

    # Figure를 이미지로 변환
    plt.switch_backend('Agg')
    canvas = FigureCanvas(fig)
    buffer = BytesIO()
    canvas.print_png(buffer)
    plt.close(fig)

    # 이미지를 HttpResponse로 반환
    return HttpResponse(buffer.getvalue(), content_type='image/png')


def travel_graph(request):
    stop_word = set(stopwords.words('english'))

    fd_category = {}

    # 지정한 카테고리로 필터링
    category = '여행'
    
    # 데이터베이스에서 데이터를 가져온 후, 리스트 형태로 변환
    category_data_db = list(Main_Crawling.objects.filter(category=category).values())

    # category_data_db에서 category와 일치하는 데이터 선택
    category_data = [row['subtopic'] for row in category_data_db if row['category'] == category]

    tokens = [word.lower() for sublist in [word_tokenize(d) for d in category_data] for word in sublist]

    fd_category = nltk.FreqDist(tokens)

    # 그래프 출력
    if platform.system() == 'Windows':
        rc('font', family='Malgun Gothic')
    elif platform.system() == 'Darwin':  
        rc('font', family='AppleGothic')
    else:  # Linux
        rc('font', family='NanumGothic')

    fig, ax = plt.subplots(figsize=(4, 4))

    ax.plot(*zip(*fd_category.items()), linestyle='-', marker='o', markersize=4, linewidth=1, color='#FF5733')
    ax.set_title(f'{category} Category')
    ax.set_xlabel('Word')
    ax.set_ylabel('Frequency')
    plt.subplots_adjust(top=0.9, bottom=0.25, left=0.2, right=0.9)

    ax.set_xticks(range(len(fd_category)))
    ax.set_xticklabels(fd_category.keys(), rotation='vertical')
    ax.grid(linestyle="--")
    ax.set_xlim(left=0)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    

    plt.tight_layout()

    # Figure를 이미지로 변환
    plt.switch_backend('Agg')
    canvas = FigureCanvas(fig)
    buffer = BytesIO()
    canvas.print_png(buffer)
    plt.close(fig)

    # 이미지를 HttpResponse로 반환
    return HttpResponse(buffer.getvalue(), content_type='image/png')

def culture_graph(request):
    stop_word = set(stopwords.words('english'))

    fd_category = {}

    # 지정한 카테고리로 필터링
    category = '문화'
    
    # 데이터베이스에서 데이터를 가져온 후, 리스트 형태로 변환
    category_data_db = list(Main_Crawling.objects.filter(category=category).values())

    # category_data_db에서 category와 일치하는 데이터 선택
    category_data = [row['subtopic'] for row in category_data_db if row['category'] == category]

    tokens = [word.lower() for sublist in [word_tokenize(d) for d in category_data] for word in sublist]

    fd_category = nltk.FreqDist(tokens)

    # 그래프 출력
    if platform.system() == 'Windows':
        rc('font', family='Malgun Gothic')
    elif platform.system() == 'Darwin':  
        rc('font', family='AppleGothic')
    else:  # Linux
        rc('font', family='NanumGothic')

    fig, ax = plt.subplots(figsize=(4, 4))

    ax.plot(*zip(*fd_category.items()), linestyle='-', marker='o', markersize=4, linewidth=1, color='#FF5733')
    ax.set_title(f'{category} Category')
    ax.set_xlabel('Word')
    ax.set_ylabel('Frequency')
    plt.subplots_adjust(top=0.9, bottom=0.25, left=0.2, right=0.9)

    ax.set_xticks(range(len(fd_category)))
    ax.set_xticklabels(fd_category.keys(), rotation='vertical')
    ax.grid(linestyle="--")
    ax.set_xlim(left=0)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    

    plt.tight_layout()

    # Figure를 이미지로 변환
    plt.switch_backend('Agg')
    canvas = FigureCanvas(fig)
    buffer = BytesIO()
    canvas.print_png(buffer)
    plt.close(fig)

    # 이미지를 HttpResponse로 반환
    return HttpResponse(buffer.getvalue(), content_type='image/png')

def IT_graph(request):
    stop_word = set(stopwords.words('english'))

    fd_category = {}

    # 지정한 카테고리로 필터링
    category = 'IT'
    
    # 데이터베이스에서 데이터를 가져온 후, 리스트 형태로 변환
    category_data_db = list(Main_Crawling.objects.filter(category=category).values())

    # category_data_db에서 category와 일치하는 데이터 선택
    category_data = [row['subtopic'] for row in category_data_db if row['category'] == category]

    tokens = [word.lower() for sublist in [word_tokenize(d) for d in category_data] for word in sublist]

    fd_category = nltk.FreqDist(tokens)

    # 그래프 출력
    if platform.system() == 'Windows':
        rc('font', family='Malgun Gothic')
    elif platform.system() == 'Darwin':  
        rc('font', family='AppleGothic')
    else:  # Linux
        rc('font', family='NanumGothic')

    fig, ax = plt.subplots(figsize=(4, 4))

    ax.plot(*zip(*fd_category.items()), linestyle='-', marker='o', markersize=4, linewidth=1, color='#FF5733')
    ax.set_title(f'{category} Category')
    ax.set_xlabel('Word')
    ax.set_ylabel('Frequency')
    plt.subplots_adjust(top=0.9, bottom=0.25, left=0.2, right=0.9)

    ax.set_xticks(range(len(fd_category)))
    ax.set_xticklabels(fd_category.keys(), rotation='vertical')
    ax.grid(linestyle="--")
    ax.set_xlim(left=0)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    

    plt.tight_layout()

    # Figure를 이미지로 변환
    plt.switch_backend('Agg')
    canvas = FigureCanvas(fig)
    buffer = BytesIO()
    canvas.print_png(buffer)
    plt.close(fig)

    # 이미지를 HttpResponse로 반환
    return HttpResponse(buffer.getvalue(), content_type='image/png')

def sports_graph(request):
    stop_word = set(stopwords.words('english'))

    fd_category = {}

    # 지정한 카테고리로 필터링
    category = '스포츠'
    
    # 데이터베이스에서 데이터를 가져온 후, 리스트 형태로 변환
    category_data_db = list(Main_Crawling.objects.filter(category=category).values())

    # category_data_db에서 category와 일치하는 데이터 선택
    category_data = [row['subtopic'] for row in category_data_db if row['category'] == category]

    tokens = [word.lower() for sublist in [word_tokenize(d) for d in category_data] for word in sublist]

    fd_category = nltk.FreqDist(tokens)

    # 그래프 출력
    if platform.system() == 'Windows':
        rc('font', family='Malgun Gothic')
    elif platform.system() == 'Darwin':  
        rc('font', family='AppleGothic')
    else:  # Linux
        rc('font', family='NanumGothic')

    fig, ax = plt.subplots(figsize=(4, 4))

    ax.plot(*zip(*fd_category.items()), linestyle='-', marker='o', markersize=4, linewidth=1, color='#FF5733')
    ax.set_title(f'{category} Category')
    ax.set_xlabel('Word')
    ax.set_ylabel('Frequency')
    plt.subplots_adjust(top=0.9, bottom=0.25, left=0.2, right=0.9)

    ax.set_xticks(range(len(fd_category)))
    ax.set_xticklabels(fd_category.keys(), rotation='vertical')
    ax.grid(linestyle="--")
    ax.set_xlim(left=0)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    

    plt.tight_layout()

    # Figure를 이미지로 변환
    plt.switch_backend('Agg')
    canvas = FigureCanvas(fig)
    buffer = BytesIO()
    canvas.print_png(buffer)
    plt.close(fig)

    # 이미지를 HttpResponse로 반환
    return HttpResponse(buffer.getvalue(), content_type='image/png')

def current_graph(request):
    stop_word = set(stopwords.words('english'))

    fd_category = {}

    # 지정한 카테고리로 필터링
    category = '시사'
    
    # 데이터베이스에서 데이터를 가져온 후, 리스트 형태로 변환
    category_data_db = list(Main_Crawling.objects.filter(category=category).values())

    # category_data_db에서 category와 일치하는 데이터 선택
    category_data = [row['subtopic'] for row in category_data_db if row['category'] == category]

    tokens = [word.lower() for sublist in [word_tokenize(d) for d in category_data] for word in sublist]

    fd_category = nltk.FreqDist(tokens)

    # 그래프 출력
    if platform.system() == 'Windows':
        rc('font', family='Malgun Gothic')
    elif platform.system() == 'Darwin':  
        rc('font', family='AppleGothic')
    else:  # Linux
        rc('font', family='NanumGothic')

    fig, ax = plt.subplots(figsize=(4, 4))

    ax.plot(*zip(*fd_category.items()), linestyle='-', marker='o', markersize=4, linewidth=1, color='#FF5733')
    ax.set_title(f'{category} Category')
    ax.set_xlabel('Word')
    ax.set_ylabel('Frequency')
    plt.subplots_adjust(top=0.9, bottom=0.25, left=0.2, right=0.9)

    ax.set_xticks(range(len(fd_category)))
    ax.set_xticklabels(fd_category.keys(), rotation='vertical')
    ax.grid(linestyle="--")
    ax.set_xlim(left=0)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    

    plt.tight_layout()

    # Figure를 이미지로 변환
    plt.switch_backend('Agg')
    canvas = FigureCanvas(fig)
    buffer = BytesIO()
    canvas.print_png(buffer)
    plt.close(fig)

    # 이미지를 HttpResponse로 반환
    return HttpResponse(buffer.getvalue(), content_type='image/png')

def wordcloud_life(request):

    if platform.system() == 'Windows':
        font_path = r'C:\Windows\Fonts\malgun.ttf'
    elif platform.system() == 'Darwin':  # Mac
        font_path = '/Library/Fonts/AppleGothic.ttf'
    else:  # Linux
        font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'

    mask = np.array(Image.open("myapp/tw.jpg"))
    category='라이프'

    category_data_db = list(Main_Crawling.objects.filter(category=category).values())

    stop_word = set(stopwords.words('english'))

    # 한국어 불용어 리스트 추가
    stop_word_kr = ['및', '이', '그', '그녀', '저', '등', '를']  # 원하는 한국어 불용어를 추가하세요.

    for word in stop_word_kr:
        stop_word.add(word)

    fd_category = {}

    #여기 카테고리만 바꾸면 돼
    category_data = [row['title'] for row in category_data_db if row['category'] == category]
    tokens = [word.lower() for sublist in [word_tokenize(d) for d in category_data] for word in sublist]
    tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens]
    # 특수 문자 제거 및 불용어 제거
    tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens if token not in stop_word_kr]
    tagged = nltk.pos_tag(tokens)
    nouns = [word for word, pos in tagged if pos in ['NN', 'NNS', 'NNP', 'NNPS']]

    fd_category = nltk.FreqDist(nouns)

    wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stop_word,
                mask=mask,  # 워드클라우드의 형태를 결정하는 이미지를 제공합니다.
                prefer_horizontal=0.8,
                font_path = font_path,  # 폰트 경로 설정
                min_font_size = 10).generate_from_frequencies(fd_category)

    # 워드 클라우드 그리기
    fig, ax = plt.subplots(figsize=(4, 4), facecolor='w') 
    ax.imshow(wordcloud, interpolation='bilinear') 
    ax.axis("off")
    plt.tight_layout()

    # Figure를 이미지로 변환
    plt.switch_backend('Agg')
    canvas = FigureCanvas(fig)
    buffer = BytesIO()
    canvas.print_png(buffer)
    plt.close(fig)

    # 이미지를 HttpResponse로 반환
    return HttpResponse(buffer.getvalue(), content_type='image/png')

def wordcloud_culture(request):

    if platform.system() == 'Windows':
        font_path = r'C:\Windows\Fonts\malgun.ttf'
    elif platform.system() == 'Darwin':  # Mac
        font_path = '/Library/Fonts/AppleGothic.ttf'
    else:  # Linux
        font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'

    mask = np.array(Image.open("myapp/tw.jpg"))
    category='문화'

    category_data_db = list(Main_Crawling.objects.filter(category=category).values())

    stop_word = set(stopwords.words('english'))

    # 한국어 불용어 리스트 추가
    stop_word_kr = ['및', '이', '그', '그녀', '저', '등', '를']  # 원하는 한국어 불용어를 추가하세요.

    for word in stop_word_kr:
        stop_word.add(word)

    fd_category = {}

    #여기 카테고리만 바꾸면 돼
    category_data = [row['title'] for row in category_data_db if row['category'] == category]
    tokens = [word.lower() for sublist in [word_tokenize(d) for d in category_data] for word in sublist]
    tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens]
    # 특수 문자 제거 및 불용어 제거
    tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens if token not in stop_word_kr]
    tagged = nltk.pos_tag(tokens)
    nouns = [word for word, pos in tagged if pos in ['NN', 'NNS', 'NNP', 'NNPS']]

    fd_category = nltk.FreqDist(nouns)

    wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stop_word,
                mask=mask,  # 워드클라우드의 형태를 결정하는 이미지를 제공합니다.
                prefer_horizontal=0.8,
                font_path = font_path,  # 폰트 경로 설정
                min_font_size = 10).generate_from_frequencies(fd_category)

    # 워드 클라우드 그리기
    fig, ax = plt.subplots(figsize=(4, 4), facecolor='w') 
    ax.imshow(wordcloud, interpolation='bilinear') 
    ax.axis("off")
    plt.tight_layout()

    # Figure를 이미지로 변환
    plt.switch_backend('Agg')
    canvas = FigureCanvas(fig)
    buffer = BytesIO()
    canvas.print_png(buffer)
    plt.close(fig)

    # 이미지를 HttpResponse로 반환
    return HttpResponse(buffer.getvalue(), content_type='image/png')

def wordcloud_IT(request):

    if platform.system() == 'Windows':
        font_path = r'C:\Windows\Fonts\malgun.ttf'
    elif platform.system() == 'Darwin':  # Mac
        font_path = '/Library/Fonts/AppleGothic.ttf'
    else:  # Linux
        font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'

    mask = np.array(Image.open("myapp/tw.jpg"))
    category='IT'

    category_data_db = list(Main_Crawling.objects.filter(category=category).values())

    stop_word = set(stopwords.words('english'))

    # 한국어 불용어 리스트 추가
    stop_word_kr = ['및', '이', '그', '그녀', '저', '등', '를']  # 원하는 한국어 불용어를 추가하세요.

    for word in stop_word_kr:
        stop_word.add(word)

    fd_category = {}

    #여기 카테고리만 바꾸면 돼
    category_data = [row['title'] for row in category_data_db if row['category'] == category]
    tokens = [word.lower() for sublist in [word_tokenize(d) for d in category_data] for word in sublist]
    tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens]
    # 특수 문자 제거 및 불용어 제거
    tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens if token not in stop_word_kr]
    tagged = nltk.pos_tag(tokens)
    nouns = [word for word, pos in tagged if pos in ['NN', 'NNS', 'NNP', 'NNPS']]

    fd_category = nltk.FreqDist(nouns)

    wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stop_word,
                mask=mask,  # 워드클라우드의 형태를 결정하는 이미지를 제공합니다.
                prefer_horizontal=0.8,
                font_path = font_path,  # 폰트 경로 설정
                min_font_size = 10).generate_from_frequencies(fd_category)

    # 워드 클라우드 그리기
    fig, ax = plt.subplots(figsize=(4, 4), facecolor='w') 
    ax.imshow(wordcloud, interpolation='bilinear') 
    ax.axis("off")
    plt.tight_layout()

    # Figure를 이미지로 변환
    plt.switch_backend('Agg')
    canvas = FigureCanvas(fig)
    buffer = BytesIO()
    canvas.print_png(buffer)
    plt.close(fig)

    # 이미지를 HttpResponse로 반환
    return HttpResponse(buffer.getvalue(), content_type='image/png')

def wordcloud_sports(request):

    if platform.system() == 'Windows':
        font_path = r'C:\Windows\Fonts\malgun.ttf'
    elif platform.system() == 'Darwin':  # Mac
        font_path = '/Library/Fonts/AppleGothic.ttf'
    else:  # Linux
        font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'

    mask = np.array(Image.open("myapp/tw.jpg"))
    category='스포츠'

    category_data_db = list(Main_Crawling.objects.filter(category=category).values())

    stop_word = set(stopwords.words('english'))

    # 한국어 불용어 리스트 추가
    stop_word_kr = ['및', '이', '그', '그녀', '저', '등', '를']  # 원하는 한국어 불용어를 추가하세요.

    for word in stop_word_kr:
        stop_word.add(word)

    fd_category = {}

    #여기 카테고리만 바꾸면 돼
    category_data = [row['title'] for row in category_data_db if row['category'] == category]
    tokens = [word.lower() for sublist in [word_tokenize(d) for d in category_data] for word in sublist]
    tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens]
    # 특수 문자 제거 및 불용어 제거
    tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens if token not in stop_word_kr]
    tagged = nltk.pos_tag(tokens)
    nouns = [word for word, pos in tagged if pos in ['NN', 'NNS', 'NNP', 'NNPS']]

    fd_category = nltk.FreqDist(nouns)

    wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stop_word,
                mask=mask,  # 워드클라우드의 형태를 결정하는 이미지를 제공합니다.
                prefer_horizontal=0.8,
                font_path = font_path,  # 폰트 경로 설정
                min_font_size = 10).generate_from_frequencies(fd_category)

    # 워드 클라우드 그리기
    fig, ax = plt.subplots(figsize=(4, 4), facecolor='w') 
    ax.imshow(wordcloud, interpolation='bilinear') 
    ax.axis("off")
    plt.tight_layout()

    # Figure를 이미지로 변환
    plt.switch_backend('Agg')
    canvas = FigureCanvas(fig)
    buffer = BytesIO()
    canvas.print_png(buffer)
    plt.close(fig)

    # 이미지를 HttpResponse로 반환
    return HttpResponse(buffer.getvalue(), content_type='image/png')

def wordcloud_travel(request):

    if platform.system() == 'Windows':
        font_path = r'C:\Windows\Fonts\malgun.ttf'
    elif platform.system() == 'Darwin':  # Mac
        font_path = '/Library/Fonts/AppleGothic.ttf'
    else:  # Linux
        font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'

    mask = np.array(Image.open("myapp/tw.jpg"))
    category='여행'

    category_data_db = list(Main_Crawling.objects.filter(category=category).values())

    stop_word = set(stopwords.words('english'))

    # 한국어 불용어 리스트 추가
    stop_word_kr = ['및', '이', '그', '그녀', '저', '등', '를']  # 원하는 한국어 불용어를 추가하세요.

    for word in stop_word_kr:
        stop_word.add(word)

    fd_category = {}

    #여기 카테고리만 바꾸면 돼
    category_data = [row['title'] for row in category_data_db if row['category'] == category]
    tokens = [word.lower() for sublist in [word_tokenize(d) for d in category_data] for word in sublist]
    tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens]
    # 특수 문자 제거 및 불용어 제거
    tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens if token not in stop_word_kr]
    tagged = nltk.pos_tag(tokens)
    nouns = [word for word, pos in tagged if pos in ['NN', 'NNS', 'NNP', 'NNPS']]

    fd_category = nltk.FreqDist(nouns)

    wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stop_word,
                mask=mask,  # 워드클라우드의 형태를 결정하는 이미지를 제공합니다.
                prefer_horizontal=0.8,
                font_path = font_path,  # 폰트 경로 설정
                min_font_size = 10).generate_from_frequencies(fd_category)

    # 워드 클라우드 그리기
    fig, ax = plt.subplots(figsize=(4, 4), facecolor='w') 
    ax.imshow(wordcloud, interpolation='bilinear') 
    ax.axis("off")
    plt.tight_layout()

    # Figure를 이미지로 변환
    plt.switch_backend('Agg')
    canvas = FigureCanvas(fig)
    buffer = BytesIO()
    canvas.print_png(buffer)
    plt.close(fig)

    # 이미지를 HttpResponse로 반환
    return HttpResponse(buffer.getvalue(), content_type='image/png')

def wordcloud_current(request):

    if platform.system() == 'Windows':
        font_path = r'C:\Windows\Fonts\malgun.ttf'
    elif platform.system() == 'Darwin':  # Mac
        font_path = '/Library/Fonts/AppleGothic.ttf'
    else:  # Linux
        font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'

    mask = np.array(Image.open("myapp/tw.jpg"))
    category='시사'

    category_data_db = list(Main_Crawling.objects.filter(category=category).values())

    stop_word = set(stopwords.words('english'))

    # 한국어 불용어 리스트 추가
    stop_word_kr = ['및', '이', '그', '그녀', '저', '등', '를']  # 원하는 한국어 불용어를 추가하세요.

    for word in stop_word_kr:
        stop_word.add(word)

    fd_category = {}

    #여기 카테고리만 바꾸면 돼
    category_data = [row['title'] for row in category_data_db if row['category'] == category]
    tokens = [word.lower() for sublist in [word_tokenize(d) for d in category_data] for word in sublist]
    tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens]
    # 특수 문자 제거 및 불용어 제거
    tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens if token not in stop_word_kr]
    tagged = nltk.pos_tag(tokens)
    nouns = [word for word, pos in tagged if pos in ['NN', 'NNS', 'NNP', 'NNPS']]

    fd_category = nltk.FreqDist(nouns)

    wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stop_word,
                mask=mask,  # 워드클라우드의 형태를 결정하는 이미지를 제공합니다.
                prefer_horizontal=0.8,
                font_path = font_path,  # 폰트 경로 설정
                min_font_size = 10).generate_from_frequencies(fd_category)

    # 워드 클라우드 그리기
    fig, ax = plt.subplots(figsize=(4, 4), facecolor='w') 
    ax.imshow(wordcloud, interpolation='bilinear') 
    ax.axis("off")
    plt.tight_layout()

    # Figure를 이미지로 변환
    plt.switch_backend('Agg')
    canvas = FigureCanvas(fig)
    buffer = BytesIO()
    canvas.print_png(buffer)
    plt.close(fig)

    # 이미지를 HttpResponse로 반환
    return HttpResponse(buffer.getvalue(), content_type='image/png')

def get_zipped_data(request):
    category = request.GET.get('category', None)

    # 본인의 데이터에 맞게 수정하세요.
    category_data_db = list(Main_Crawling.objects.filter(category=category).values())

    title_data = [row['title'] for row in category_data_db if row['category'] == category]
    link_data = [row['link'] for row in category_data_db if row['category'] == category]
    author_data = [row['author'] for row in category_data_db if row['category'] == category]
    subtopic_data = [row['subtopic'] for row in category_data_db if row['category'] == category]
    content_data = [row['content'] for row in category_data_db if row['category'] == category]

    zipped_data = list(zip(title_data, link_data, content_data, author_data, subtopic_data))

    return JsonResponse(zipped_data, safe=False)

def home_page(request):
    return render(request,'home_page.html')

def home2_page(request):
    return render(request,'home2_page.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user exists in the database
        try:
            user = User_Table.objects.get(username=username)
        except User_Table.DoesNotExist:
            return JsonResponse({'success': False, 'message': '아이디가 없습니다.'})

        # Check if the password is correct
        if user.password == password:
            # 로그인 성공
            return JsonResponse({'success': True})
        else:
            # 비밀번호가 틀림
            return JsonResponse({'success': False, 'message': '비밀번호가 틀립니다.'})
    else:
        # GET 메서드로 요청이 들어온 경우 로그인 페이지를 렌더링
        if request.method == "GET":
            return render(request, 'login.html')
        else:
            # 잘못된 HTTP 메서드
            return JsonResponse({'success': False, 'message': '잘못된 요청입니다.'})

def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = data.get('name')
        username = data.get('username')
        password = data.get('password')
        passwordck = data.get('passwordck')
        birthdate = data.get('birthdate')

        # 입력 필드가 빈 경우에 대한 처리
        if not (name and username and password and passwordck and birthdate):
            return HttpResponse('모든 필드를 입력해주세요.', status=400)

        # 패스워드 확인
        if password != passwordck:
            return HttpResponse('패스워드가 일치하지 않습니다.', status=400)

        # 동일한 사용자 이름이 이미 있는지 확인
        if User_Table.objects.filter(username=username).exists():
            return HttpResponse('이미 존재하는 사용자 이름입니다.', status=400)

        # 모든 검사를 통과한 경우 데이터베이스에 저장
        user_table = User_Table(name=name, username=username, password=password, birthdate=birthdate)
        user_table.save()

    return render(request, 'signup.html')


from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def get_name_from_db(request):
    user = User_Table.objects.first()  # 첫 번째 사용자 객체 가져오기
    name = user.name if user else ""  # 사용자 객체가 있을 경우 이름 가져오기
    return name