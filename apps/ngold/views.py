from django.shortcuts import render, redirect
import random, datetime

def hub(request):
    if not request.session.keys():
        request.session['gold'] = 0
        request.session['message'] = ['']
    info = {
        "gold": request.session['gold'],
        "messages": request.session['message']
    }
    return render(request, "ninjagolddj.html", info)

def process_gold(request, methods = ['POST']):
    request.session['building'] = request.POST['building']
    now = datetime.datetime.now()

    if request.session['building'] == 'farm':
        request.session['getgold'] = random.randrange(10, 21)
        request.session['gold'] = request.session['gold'] + request.session['getgold']
        request.session['message'].append("<p style = 'color: green'>Entered " + request.session['building'] + " and got " + str(request.session['getgold']) + " gold! Yay! (" + str(now) + ") " + "</p>")
        return redirect('/')

    elif request.session['building'] == 'cave':
        request.session['getgold'] = random.randrange(5, 11)
        request.session['gold'] = request.session['gold'] + request.session['getgold']
        request.session['message'].append("<p style = 'color: green'>Entered " + request.session['building'] + " and got " + str(request.session['getgold']) + " gold! Yay! (" + str(now) + ") " + "</p>")
        return redirect('/')
    elif request.session['building'] == 'house':
        request.session['getgold'] = random.randrange(2, 6)
        request.session['gold'] = request.session['gold'] + request.session['getgold']
        request.session['message'].append("<p style = 'color: green'>Entered " + request.session['building'] + " and got " + str(request.session['getgold']) + " gold! Yay! (" + str(now) + ") " + "</p>")
        return redirect('/')
    else:
        request.session['getgold'] = random.randrange(-50, 51)
        request.session['gold'] = request.session['gold'] + request.session['getgold']
        if request.session['getgold'] > 0:
            request.session['message'].append("<p style = 'color: green'>Entered " + request.session['building'] + " and got " + str(request.session['getgold']) + " gold! Lucky! (" + str(now) + ") " + "</p>")
        elif request.session['getgold'] <= 0:
            request.session['message'].append("<p style = 'color: red'>Entered " + request.session['building'] + " and lost " + str(-request.session['getgold']) + " gold. Too bad! (" + str(now) + ") " + "</p>")
        return redirect('/')

def reset(request, methods = ['POST']):
    request.session.clear()
    return redirect("/")

