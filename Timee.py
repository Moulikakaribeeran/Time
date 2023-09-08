import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/latest.stories', methods=['GET'])
def latest_stories():
    try:

        url = 'https://time.com/'


        response = requests.get(url)


        if response.status_code == 200:

            par_ele = BeautifulSoup(response.text, 'html.parser')


            ele = par_ele.find_all('li', class_='latest-stories__item')


            latest_stories = []


            for story in ele[:6]:
                tit = story.text.strip()
                lnk = story.find('a')['href']


                latest_stories.append({
                    'TITLE': tit,
                    'LINK': lnk
                })


            return jsonify({'STORIES IN THE WEB PAGES ARE': latest_stories})

        else:
            return jsonify({'error': 'Failed to fetch data from Time.com'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
