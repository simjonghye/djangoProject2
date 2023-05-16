from django.shortcuts import render
import random
# Create your views here.

def lotto_index(request): #로또 html 응답
    return render(request, 'demos/lotto_index.html')

def lotto_result(request):
    lotto_number = list()
    game = request.GET.get('game', 1) #GET:속성, get:함수 (name=game 속성을 가져옴)
    pull_number = [index for index in range(1, 46)] #for문 결과를 리스트 형식으로 저장

    for _ in range(int(game)): #game 수만큼 반복
        lotto_number.append(random.sample(pull_number, 6)) #pull_number라는 변수(여기선 리스트)에서 6개의 값

    return render(request, 'demos/lotto_result.html', {'lotto_number': lotto_number, 'game': game}) #html에서 사용하기 위해 딕셔너리로 구현
