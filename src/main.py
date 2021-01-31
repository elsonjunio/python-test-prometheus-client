import time

import prometheus_client
from flask import Flask, Response
from prometheus_client import Counter, Histogram

app = Flask(__name__)

_INF = float("inf")

graphs = {'c': Counter('python_request_operations_total', 'the total number of processed requests'),
          'h': Histogram('python_request_duration_seconds', 'Histogram for the duration in seconds',
                         buckets=(1, 2, 5, 6, 10, _INF))}


@app.route("/")
def hello():
    start = time.time()
    graphs['c'].inc()

    time.sleep(0.6)
    end = time.time()
    graphs['h'].observe(end - start)
    return "helo word"


@app.route('/metrics')
def requests_count():
    res = []
    for key in graphs:
        res.append(prometheus_client.generate_latest(graphs[key]))
    return Response(res, mimetype="text/plain")


if __name__ == '__main__':
    app.run()
