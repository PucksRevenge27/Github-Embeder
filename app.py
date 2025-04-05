from flask import Flask, request, render_template, send_file
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

GITHUB_API_URL = 'https://api.github.com/repos/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    repo = request.form['repo']
    try:
        process_index_html(repo)
        return 'Updated index.html has been created.'
    except Exception as e:
        print(e)
        return 'An error occurred. Please check the console for details.'

def fetch_file_content(repo, file_path):
    url = f"{GITHUB_API_URL}{repo}/contents/{file_path}"
    response = requests.get(url, headers={'Accept': 'application/vnd.github.v3.raw'})
    response.raise_for_status()
    return response.text

def process_index_html(repo):
    index_path = 'index.html'
    index_html = fetch_file_content(repo, index_path)
    soup = BeautifulSoup(index_html, 'html.parser')

    src_files = [script['src'] for script in soup.find_all('script', src=True)]
    href_files = [link['href'] for link in soup.find_all('link', href=True)]

    for src in src_files:
        content = fetch_file_content(repo, src)
        script_tag = soup.find('script', src=src)
        script_tag.string = content
        script_tag.attrs.pop('src', None)

    for href in href_files:
        content = fetch_file_content(repo, href)
        link_tag = soup.find('link', href=href)
        style_tag = soup.new_tag('style')
        style_tag.string = content
        link_tag.replace_with(style_tag)

    updated_index_html = str(soup)
    with open('updated_index.html', 'w') as file:
        file.write(updated_index_html)
    print('Updated index.html has been created.')

if __name__ == '__main__':
    app.run(debug=True)
