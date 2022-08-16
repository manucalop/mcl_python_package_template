from flask import Flask

from mcl_python_package_template.app import App

app = Flask(__name__)

application = App()


@app.route("/", methods=["GET", "POST"])
def main():
    app.logger.info("Starting mcl_python_package_template")
    try:
        application.run()
        app.logger.info("mcl_python_package_template finished correctly.")
        return {
            "code": 200,
            "status": "ok",
            "message": "mcl_python_package_template finished correctly.",
            "data": {},
            "errors": [],
        }
    except Exception as e:
        app.logger.error(e)
        return {
            "code": 500,
            "status": "error",
            "message": "mcl_python_package_template finished with errors.",
            "data": {},
            "errors": [str(e)],
        }


if __name__ == "__main__":
    app.run(debug=True)
