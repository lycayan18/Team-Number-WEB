from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

comments = []


@app.route('/comments', methods=['GET'])
def get_comments():
    print(comments)
    return render_template('comment.html', comments=comments)


@app.route('/comments', methods=['POST'])
def add_comment():
    data = request.get_json()
    try:
        comment = {
            'name': data[0]['name'],
            'body': data[0]['body'],
            'time': data[0]['time']
        }
        comments.append(comment)
        response = {
            'success': True,
            'message': 'Комментарий успешно добавлен'
        }
        return jsonify(response)
    except IndexError:
        return ""

if __name__ == '__main__':
    app.run()