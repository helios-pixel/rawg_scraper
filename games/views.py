from django.shortcuts import render, redirect

# Create your views here.
from .api import search_games, get_game_details
from .models import Game, UserLibrary, Review

def search(request):
    query=request.GET.get('q')
    results=search_games(query) if query else []
    return render(request, 'games/search.html', {'results': results})

def game_detail(request, game_id):
    details=get_game_details(game_id)
    game, created = Game.objects.get_or_create(
        rawg_id=game_id,
        defaults={'title': details['name'],
                  'description':details['description']}
    )

    if request.method == 'POST' and request.user.is_authenticated:
        UserLibrary.object.create(user=request.user, game=game)
    
    reviews=Review.objects.filter(game=game)
    return render(request, 'games/game_details.html',
                  {'game': game, 'details': details, 'reviews': reviews})

def add_review(request, game_id):
    game=Game.object.get(rawg_id=game_id)
    if request.method == 'POST':
        review_text = request.POST.get('review')
        rating=request.POST,get('rating')
        Review.objects.create(user=request.user, game=game, review=review_text, rating=rating)
        return redirect('game_detail', game_id=game_id)
    return render(request, 'games/add_review.html', {'game':game})