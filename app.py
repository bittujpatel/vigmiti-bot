from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('resume.html')

@app.route('/timeline')
def timeline():
    # Fetch timeline data from a database or data file
    timeline_data = [
        # Your timeline events here
    ]
    return jsonify(timeline_data)

if __name__ == '__main__':
    app.run(debug=True)
