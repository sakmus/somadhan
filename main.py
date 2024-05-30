from flask import Flask, render_template, request
import wolframalpha, dotenv, os

dotenv.load_dotenv(override=True)
client = wolframalpha.Client(os.getenv("APP_ID"))
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        response = client.query(query)
        if 'plot' in query.lower():

            img = handle(response)
            return render_template('index.html', src=img[0], alt=img[1], query=query)

        result = next(response.results).text.replace("integral", "int").replace("constant", "const")
        return render_template('index.html', result=result, query=query)

    return render_template('index.html')


def handle(res):
    for pod in res.pods:
        if pod.title == 'Plots':
            src = pod.subpod[0].img.src
            alt = pod.subpod[0].img.alt
            break

    return [src, alt]


if __name__ == "__main__":
    app.run()
