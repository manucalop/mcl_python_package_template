from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    app.logger.info("Starting mcl_python_package_template")
    try:
        app.logger.info("mcl_python_package_template finished")
        return ("", 204)
    except Exception as e:
        app.logger.error(e)
        return ("", 500)
