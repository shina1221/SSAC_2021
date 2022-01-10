# polls.views.py
# View: 사용자 요청을 처리하는 로직
#   HTTP요청(기능) 당 하나의 함수(FBV)/Class(CBV)
#   View - urls.py 등록
# View의 일반적인 로직
#  1. 사용자가 보낸 요청파라미터/Path 파라미터를 읽는다.
#  2. 사용자가 보낸 값을 검증한다.
#  3. Business logic을 처리한다. 
#  4. 처리 결과를 응답한다.

from django.shortcuts import render, redirect
from .models import Question, Choice
from django.urls import reverse #View에서 urls.py의 path설정 이름을 이용해 url을 조회.
# Generic View들을 import 
from django.views.generic import ListView, DetailView, View




# 설문처리 
# 설문처리 2단계 - 하나의 url로 처리(구현은 하나의 View)
# GET 요청 : 설문 양식 응답(FBV-vote_form)
# POST 요청: 설문 처리(FBV-vote)
class VoteView(View):
    # kwargs: path parameter를 조회.
    def get(self, request, *args, **kwargs):
        # get 방식 요청 처리 코드를 재정의 하는 메소드
        print('========= GET 처리')
        # path parameter로 넘어온 question_id 조회 : kwargs
        question_id = kwargs['question_id']
        try:
            question = Question.objects.get(pk=question_id)
            # 응답처리
            return render(request, "polls/vote_form.html", {"question":question})
        except:
            #오류->error_page로 이동
            return render(request, "polls/error.html", {"error_message":"없는 설문 번호입니다."})

    def post(self, request, *args, **kwargs):
        # post 방식 요청 처리 코드를 재정의 하는 메소드
        print("============POST 처리")
        choice_id = request.POST.get('choice')
        # question_id = request.POST.get('question_id')
        question_id = kwargs['question_id'] #path parameter

        # choice_id가 없으면(None-user가 선택하지 않고 투표) vote_form으로 이동 -> error메세지 전송
        if choice_id == None:
            # question_id로 Question을 조회해서 반환.
            question = Question.objects.get(pk=question_id)
            return render(request, 
                        'polls/vote_form.html', 
                        {'error_message':'보기를 선택하세요', 
                        'question':question})
        # 정상처리(사용자가 보기를 선택하고 요청한 경우) => vote값을 1증가(update)
        choice = Choice.objects.get(pk=choice_id) #Choice를 조회
        choice.vote = choice.vote + 1 #1을 증가
        choice.save() #update

        url_str = reverse("polls:vote_result", args=[question_id]) #args: path parameter값 등록
        print(url_str)
        return redirect(url_str)



  

# 한 문제에 대한 설문결과를 응답하는 View - 1개 데이터에 대한 상세정보 출력: DetailView
# pk를 받아서 모델에서 조회 후 템플릿으로 응답
# DetailView: primary key(pk)값을 path parameter.
#                            urls.py에서 url 매핑 설정: <type:pk>  (변수명: pk)
# class QuestionDetailView(DetailView):
#     model = Question #조회할 모델 클래스
#     template_name = 'polls/vote_result.html' #응답할 template 경로


# # 설문 목록 조회 기능 - N개의 data를 조회->template 전달 : ListView를 상속
# # 특정 테이블에서 전체 조회 -> 어떤 모델(테이블)에서 조회할지
# # 조회결과를 template에 전달하면서 호출 -> 어떤 template을 호출할지 
# class QuestionListView(ListView):
#     model = Question # 어떤 모델(테이블)에서 조회할지
#     template_name = "polls/list.html" #어떤 template을 호출할지 
#     # 조회결과를 template에 전달 - 이름-QuerySet : 이름 - object_list, 모델클래스명(소문자)_list(question_list)
#     # 원하는 다른 이름으로 전달: context_object_name = "원하는이름"
#     # context_object_name = 'q_list'