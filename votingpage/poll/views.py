from django.shortcuts import render, redirect
from django.http import HttpResponse

# from .forms import CreatePollForm
from .models import GoodPoll
from .models import BadPoll


def home(request):
    pollsGood = GoodPoll.objects.all()
    pollsBad = BadPoll.objects.all()
    context = {
        'pollsGood': pollsGood,
        'pollsBad': pollsBad,
    }
    return render(request, 'poll/home.html', context)


# def create(request):
#     if request.method == 'POST':
#         form = CreatePollForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = CreatePollForm()
#     context = {
#         'form' : form
#     }
#     return render(request, 'poll/create.html', context)

# def vote(request, poll_id):
#     poll = Poll.objects.get(pk=poll_id)
#
#     if request.method == 'POST':
#
#         selected_option = request.POST['poll']
#         if selected_option == 'option1':
#             poll.option_one_count += 1
#         elif selected_option == 'option2':
#             poll.option_two_count += 1
#         elif selected_option == 'option3':
#             poll.option_three_count += 1
#         else:
#             return HttpResponse(400, 'Invalid form')
#
#         poll.save()
#
#         return redirect('results', poll.id)
#
#     context = {
#         'poll' : poll
#     }
#     return render(request, 'poll/vote.html', context)

def voteGood(request, poll_id):
    poll = GoodPoll.objects.get(pk=poll_id)

    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_1 += 1
        elif selected_option == 'option2':
            poll.option_2 += 1
        elif selected_option == 'option3':
            poll.option_3 += 1
        elif selected_option == 'option4':
            poll.option_4 += 1
        elif selected_option == 'option5':
            poll.option_5 += 1
        elif selected_option == 'option6':
            poll.option_6 += 1
        elif selected_option == 'option7':
            poll.option_7 += 1
        elif selected_option == 'option8':
            poll.option_8 += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        # return redirect('resultsGood', poll.id)

    context = {
        'poll': poll
    }
    return render(request, 'poll/voteGood.html', context)


def voteBad(request, poll_id):
    poll = BadPoll.objects.get(pk=poll_id)

    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_1 += 1
        elif selected_option == 'option2':
            poll.option_2 += 1
        elif selected_option == 'option3':
            poll.option_3 += 1
        elif selected_option == 'option4':
            poll.option_4 += 1
        elif selected_option == 'option5':
            poll.option_5 += 1
        elif selected_option == 'option6':
            poll.option_6 += 1
        elif selected_option == 'option7':
            poll.option_7 += 1
        elif selected_option == 'option8':
            poll.option_8 += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        # return redirect('resultsBad', poll.id)
    0
    context = {
        'poll': poll
    }
    return render(request, 'poll/voteBad.html', context)


def resultsGood(request, poll_id):
    poll = GoodPoll.objects.get(pk=poll_id)
    context = {
        'poll': poll
    }

    all_fields = poll._meta.get_fields()

    best_index = 0
    best_value = poll.option_1
    i = -1

    for field in all_fields:
        # Skip id
        if i == -1:
            i += 1
            continue

        val = getattr(poll, field.name)
        print(val, field.name)
        if val > best_value:
            best_index = i
            best_value = val
        i += 1

    return HttpResponse(f"{best_index}")


def resultsBad(request, poll_id):
    poll = BadPoll.objects.get(pk=poll_id)
    context = {
        'poll': poll
    }

    all_fields = poll._meta.get_fields()

    best_index = 0
    best_value = poll.option_1
    i = -1

    for field in all_fields:
        # Skip id
        if i == -1:
            i += 1
            continue

        val = getattr(poll, field.name)
        print(val, field.name)
        if val > best_value:
            best_index = i
            best_value = val
        i += 1

    return HttpResponse(f"{best_index}")


def resetPolls(request, poll_id):
    pollGood = GoodPoll.objects.get(pk=poll_id)
    pollBad = BadPoll.objects.get(pk=poll_id)

    all_fields = pollGood._meta.get_fields()

    i = -1
    for field in all_fields:
        # Skip id
        if i == -1:
            i += 1
            continue
        a = getattr(pollGood, field.name)
        print(a)
        setattr(pollGood, field.name, 0)
        i += 1

    pollGood.save()

    all_fields = pollBad._meta.get_fields()

    i = -1
    for field in all_fields:
        # Skip id
        if i == -1:
            i += 1
            continue

        setattr(pollBad, field.name, 0)
        i += 1
        
    pollBad.save()

    return HttpResponse(200, "Okie Dokie buddy")
