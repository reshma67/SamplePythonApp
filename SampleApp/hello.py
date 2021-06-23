from flask import Flask
myapp = Flask(__name__)
# myapp.config.from_envvar('APP_SETTINGS')


@myapp.route("/", methods=['GET', 'POST'])
def uploadFile():
    return "Hello Flask, on Azure App Service for Linux"


if __name__ == '__main__':
    myapp.run(debug=True)
