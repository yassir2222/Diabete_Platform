from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login,logout
from django.contrib import messages
from DiabetSys.settings import GENERATIVE_AI_KEY
from Diabet.models import ChatMessage
import google.generativeai as genai
import markdown

def home(request):
    return render(request, 'home.html', {})

def login_user(request):
   
    if request.method == "POST":
        username = request.POST['username' ]
        password = request.POST['password' ]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Logged In!"))
            print("authenticated")
            return redirect('main')
        else:
            messages.success(request, ("Error Try again!"))
            print("not authenticated")
            return redirect('login')
    else:
        return render(request, 'login.html', {})
    

def logout_user(request):
    pass

def main(request):
    return render(request, 'main.html', {})

def send_message(request):
    if request.method == 'POST':
        genai.configure(api_key=GENERATIVE_AI_KEY)
        model = genai.GenerativeModel("gemini-pro")

        user_message = request.POST.get('user_message')
        bot_response = model.generate_content(user_message)
        html = markdown.markdown(bot_response.text)
        ChatMessage.objects.create(user_message=user_message, bot_response=html)

    return redirect('list_messages')

def list_messages(request):
    messages = ChatMessage.objects.all()
    return render(request, 'list_messages.html', { 'messages': messages })