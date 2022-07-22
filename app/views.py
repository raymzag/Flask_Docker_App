from flask import Blueprint, jsonify, render_template, current_app
from app import app

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/test_unleash')
def test_unleash():
    unleash = current_app.extensions['Unleash']
    print(f"Unleash check: {unleash.client.is_enabled('gunicorn')}")

    return jsonify({'status': 'success', 'gunicorn': unleash.client.is_enabled('gunicorn')})
