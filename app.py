from flask import Flask, render_template
import requests

app = Flask(__name__, static_url_path='/static')


def planet_unicode(planet_name):
    if planet_name == 'mercury':
        return '\u263F'
    elif planet_name == 'venus':
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

    retrograde_data_unicode = {}

    for k, v in retrograde_data.items():
        print(planet_unicode(k))
        retrograde_data_unicode[planet_unicode(k)] = v

    print(retrograde_data)

    # Render ther retrograde.html template with the fetched data
    return render_template('retrograde.html', retrograde_data=retrograde_data_unicode)


if __name__ == '__main__':
    app.run(debug=True)
