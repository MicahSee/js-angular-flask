from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/<user_id>')
def index(user_id):
    return render_template('index.html')

@app.route('/api/v1/form', methods=['POST'])
def form():
    post_data = request.get_json()
    print(post_data['new_password'])
    print(post_data['user_id'])
    return 'https://www.google.com'


app.run()
