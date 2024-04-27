from flask import Flask, request, render_template

app = Flask(__name__)

movies = {
    "1": {
        "title": "Manjummel Boys",
        "showtimes": ["10:00 AM", "3:00 PM", "6:30 PM"],
        "seats": 300
    },
    "2": {
        "title": "Article 370",
        "showtimes": ["11:00 AM", "4:00 PM", "7:30 PM"],
        "seats": 250
    },
    "3": {
        "title": "Operation Valentine",
        "showtimes": ["2:00 PM", "5:30 PM", "9:00 PM"],
        "seats": 120
    }
}


@app.route('/')
def index():
    return render_template('index.html', movies=movies)


@app.route('/book', methods=['POST'])
def book():
    movie_id = request.form['movie_id']
    showtime = request.form['showtime']
    num_tickets = int(request.form['num_tickets'])

    if movie_id not in movies:
        return render_template('error.html', message='Movie not found')

    if showtime not in movies[movie_id]['showtimes']:
        return render_template('error.html', message='Showtime not available')

    if num_tickets <= 0:
        return render_template('error.html', message='Invalid no of tickets')

    al_seat = movies[movie_id]['seats']
    if num_tickets > al_seat:
        return render_template('error.html', message='Seats rem:'+str(al_seat))

    movies[movie_id]['seats'] -= num_tickets
    rem_seats = movies[movie_id]['seats']

    return render_template('success.html', message='Done', rem_seats=rem_seats)


if __name__ == '__main__':
    app.run(debug=True)
