from django.shortcuts import render, redirect
import pandas as pd
from .sustain import model


def handler(request):
    result = [-1]
    if request.method == 'POST':
        af = request.POST['artist_familiarity']
        ah = request.POST['artist_hotness']
        duration = request.POST['duration']
        loudness = request.POST['loudness']
        sh = request.POST['song_hotness']
        stfo = request.POST['start_to_fade_out']
        tempo = request.POST['tempo']
        ts = request.POST['time_signature']
        tsc = request.POST['time_sign_confidence']
        df = pd.DataFrame(columns=['artist_familiarity', 'artist_hotness', 'duration',
                                     'loudness', 'song_hotness', 'start_to_fade_out'
                                     , 'tempo', 'time_signature', 'time_sign_confidence'])

        df2 = {'artist_familiarity': float(af), 'artist_hotness': float(ah), 'duration': float(duration),
                'loudness': float(loudness), 'song_hotness': float(sh), 'start_to_fade_out': float(stfo)
                , 'tempo': float(tempo), 'time_signature': float(ts), 'time_sign_confidence': float(tsc)}

        data = df.append(df2, ignore_index=True)
        result = predict(data)
    else:
        result = [-1]
    return render(request, "index.html", {'response': result[0]})


def predict(data):
    res = model.predict(data)
    print(res)
    return res