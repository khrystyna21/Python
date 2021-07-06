from flask import Flask, render_template, request, jsonify
import pymysql.cursors


app = Flask(__name__)


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root-root21',
                             database='imdb',
                             cursorclass=pymysql.cursors.DictCursor)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/ajaxlivesearch",methods=["POST","GET"])
def ajaxlivesearch():
    cur = connection.cursor()
    if request.method == 'POST':
        search_word = request.form['query']
        print(search_word)
        if search_word == '':
            query = "SELECT * from movies ORDER BY movie_id DESC"
            cur.execute(query)
            movie = cur.fetchall()
        else:
            query = "SELECT * from movies WHERE movie_name LIKE '%{}%' OR movie_year LIKE '%{}%' OR director LIKE '%{}%' ORDER BY movie_id DESC".format(search_word,search_word,search_word)
            cur.execute(query)
            numrows = int(cur.rowcount)
            movie = cur.fetchall()
            print(numrows)
    return jsonify({'htmlresponse': render_template('response.html', movie=movie, numrows=numrows)})


if __name__ == "__main__":
    app.run(port=8000)