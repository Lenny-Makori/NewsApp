from flask import render_template
from app import app
from .requests import get_source, get_article

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    entertainment = get_source('entertainment')
    business = get_source('business')
    general = get_source('general')
    health = get_source('health')
    science = get_source('science')
    sports = get_source('sports')
    technology = get_source('technology')

    
    # https://newsapi.org/v2/sources?apiKey=3a1f09f201904834870e3fdbb44430ee
    title="Home-Welcome to NEWS sources Website"
    return render_template('index.html', entertainment = entertainment, business = business, general = general, health = health, science = science, sports =sports, technology = technology, title = title)

