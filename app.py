
from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle

# laoding models
df = pickle.load(open('df.song','rb'))
similarity = pickle.load(open('similarity.song','rb'))


def recommendation(song_df):
    idx = df[df['song'] == song_df].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])

    songs = []
    for m_id in distances[1:21]:
        songs.append(df.iloc[m_id[0]].song)

    return songs


# flask app
app = Flask(__name__)
# paths
@app.route('/')
def index():
    names = list(df['song'].values)
    return render_template('new.html',name = names)
@app.route('/recom',methods=['POST'])
def mysong():
    user_song = request.form['names']
    songs = recommendation(user_song)

    return render_template('new.html',songs=songs)


# python
if __name__ == "__main__":
    app.run(debug=True)