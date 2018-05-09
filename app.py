# -*- coding: utf8 -*-
from flask import Flask
from flask import render_template
from simplejson import dumps
from jd_spider import jd_specification_spider

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route("/jd/specification/<keyword>")
def jd_specification(keyword):
    data = jd_specification_spider(keyword)
    return render_template(
        "specification.html", data=dumps(data, ensure_ascii=False))


if __name__ == "__main__":
    app.debug = True
    app.run()
