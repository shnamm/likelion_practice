from django.shortcuts import render
import random
# Create your views here.
def lotto_index(request):
    return render(request, 'lotto_index.html')

def lottoGenerator(request):
    lotto_list = []
    game = request.GET.get('game', 1)
    pull_number = [i for i in range(1,46)]

    for _ in range(int(game)):
        lotto_list.append(random.sample(pull_number,6))
    return render(request, 'lotto_result.html', {'lotto_list':lotto_list, 'game':game})
