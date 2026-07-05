from flask import Flask, render_template
import os
app = Flask(__name__)

# ========== ENGLISH PAGES ==========
@app.route('/')
def home_en():
    return render_template('home_en.html')

@app.route('/secretariat')
def secretariat_en():
    return render_template('secretariat_en.html')

@app.route('/committees')
def committees_en():
    return render_template('committees_en.html')

@app.route('/social-event')
def social_en():
    return render_template('social_en.html')

@app.route('/food')
def food_en():
    return render_template('food_en.html')

@app.route('/news')
def news_en():
    return render_template('news_en.html')

@app.route('/contact')
def contact_en():
    return render_template('contact_en.html')

# ========== POLISH PAGES ==========
@app.route('/pl')
def home_pl():
    return render_template('home_pl.html')

@app.route('/pl/sekretariat')
def secretariat_pl():
    return render_template('secretariat_pl.html')

@app.route('/pl/komitety')
def committees_pl():
    return render_template('committees_pl.html')

@app.route('/pl/wydarzenie')
def social_pl():
    return render_template('social_pl.html')

@app.route('/pl/jedzenie')
def food_pl():
    return render_template('food_pl.html')

@app.route('/pl/aktualnosci')
def news_pl():
    return render_template('news_pl.html')

@app.route('/pl/kontakt')
def contact_pl():
    return render_template('contact_pl.html')

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)