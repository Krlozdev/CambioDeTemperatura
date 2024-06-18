from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here

    return 'Hello World!'
@app.route('/clase')
def clase():
    return '<h1><center>Clase de fundamentos de programacion</center></h1>'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'



if __name__ == '__main__':
    app.run()
