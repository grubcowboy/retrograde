from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/api')
def retrograde():
    # Fetch retrograde information from the API

    # response = requests.get('https://api.example.com/retrograde')
    # retrograde_data = response.json()

    retrograde_data = {
        'mercury': False,
        'venus': True,
        'earth': True,
        'mars': False
    }

    # Render ther retrograde.html template with the fetched data
    return render_template('retrograde.html', retrograde_data=retrograde_data)


if __name__ == '__main__':
    app.run(debug=True)
