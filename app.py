from flask import Flask, render_template
import requests

app = Flask(__name__, static_url_path='/static')


class Planet:

    def __init__(self, name, status):
        self.name = name.title()
        self.symbol = self.get_unicode()
        self.status = status

    def __str__(self):
        return self.name

    def get_unicode(self):

        if self.name == 'Mercury':
            return '\u263F'
        elif self.name == 'Venus':
            return '\u2640'


@app.route('/')
def retrograde():
    # Fetch retrograde information from the API

    # response = requests.get('https://api.example.com/retrograde')
    # retrograde_data = response.json()

    retrograde_data = {
        'mercury': False,
        'venus': True,
        # 'earth': True,
        # 'mars': False
    }

    planets = []

    for k, v in retrograde_data.items():
        p = Planet(k, v)
        print(p)
        planets.append(p)

    print(retrograde_data)

    # Render ther retrograde.html template with the fetched data
    return render_template('retrograde.html', planets=planets)


if __name__ == '__main__':
    app.run(debug=True)
