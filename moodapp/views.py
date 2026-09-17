from django.shortcuts import render

MOOD_DATA = {
    'happy': {
        'title': 'Happy 😊',
        'theme_class': 'theme-happy',
        'quote': '“Happiness is contagious! Spread it everywhere you go today.”',
        'songs': [
            {'title': 'Happy', 'artist': 'Pharrell Williams', 'url': 'https://open.spotify.com/track/60nZ122Rm9LSt3y10R31R2'},
            {'title': 'Can\'t Stop the Feeling!', 'artist': 'Justin Timberlake', 'url': 'https://open.spotify.com/track/1uv13S1c557672'},
            {'title': 'Good Life', 'artist': 'OneRepublic', 'url': 'https://open.spotify.com/track/71360633'}
        ],
        'watch': ['The Lego Movie', 'Inside Out', 'Despicable Me'],
        'eat': ['🍦 A big scoop of ice cream', '🍉 Fresh watermelon slices'],
        'activities': ['Draw a picture with bright colors', 'Dance around your room']
    },
    'sad': {
        'title': 'Sad 😢',
        'theme_class': 'theme-sad',
        'quote': '“It’s okay to feel sad sometimes. Rainbows only appear after the rain!”',
        'songs': [
            {'title': 'You\'ve Got a Friend in Me', 'artist': 'Randy Newman', 'url': 'https://open.spotify.com/search/You%27ve%20Got%20a%20Friend%20in%20Me'},
            {'title': 'Fix You', 'artist': 'Coldplay', 'url': 'https://open.spotify.com/search/Fix%20You%20Coldplay'},
            {'title': 'Try Everything', 'artist': 'Shakira', 'url': 'https://open.spotify.com/search/Try%20Everything%20Shakira'}
        ],
        'watch': ['Paddington 2', 'Finding Nemo', 'My Neighbor Totoro'],
        'eat': ['🍫 A piece of chocolate', '🥛 A glass of warm milk'],
        'activities': ['Hug a soft pillow', 'Talk to a friend or parent']
    },
    'tired': {
        'title': 'Tired 😴',
        'theme_class': 'theme-tired',
        'quote': '“Even super-heroes need time to recharge their batteries!”',
        'songs': [
            {'title': 'A Whole New World', 'artist': 'Zayn & Zhavia', 'url': 'https://open.spotify.com/search/A%20Whole%20New%20World'},
            {'title': 'Count on Me', 'artist': 'Bruno Mars', 'url': 'https://open.spotify.com/search/Count%20on%20Me%20Bruno%20Mars'},
            {'title': 'Sunflower', 'artist': 'Post Malone', 'url': 'https://open.spotify.com/search/Sunflower%20Post%20Malone'}
        ],
        'watch': ['Winnie the Pooh', 'WALL-E', 'The Secret Life of Pets'],
        'eat': ['🍌 A fresh banana', '🥣 A warm bowl of oatmeal'],
        'activities': ['Rest your eyes for 15 minutes', 'Drink a big glass of water']
    },
    'motivated': {
        'title': 'Motivated 😎',
        'theme_class': 'theme-motivated',
        'quote': '“You are capable of amazing things when you try your best!”',
        'songs': [
            {'title': 'Eye of the Tiger', 'artist': 'Survivor', 'url': 'https://open.spotify.com/search/Eye%20of%20the%20Tiger'},
            {'title': 'Believer', 'artist': 'Imagine Dragons', 'url': 'https://open.spotify.com/search/Believer%20Imagine%20Dragons'},
            {'title': 'Unstoppable', 'artist': 'Sia', 'url': 'https://open.spotify.com/search/Unstoppable%20Sia'}
        ],
        'watch': ['Kung Fu Panda', 'Cars', 'How to Train Your Dragon'],
        'eat': ['🍇 Fresh grapes and cheese', '🍊 Juicy orange slices'],
        'activities': ['Build something awesome with Legos', 'Finish your daily goal']
    }
}

def home(request):
    return render(request, 'home.html')

def mood_detail(request, mood_name):
    data = MOOD_DATA.get(mood_name.lower(), MOOD_DATA['happy'])
    return render(request, 'mood.html', {'data': data})