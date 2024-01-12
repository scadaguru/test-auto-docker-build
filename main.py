# third party imports which needs installation
import yaml # pip install pyyaml
from flask import Flask, render_template, request, Response # pip install flask
from flask_classful import FlaskView, route # pip install flask-classful

# standard imports
import logging

flask_app = Flask(__name__, template_folder='.')

class dockerBuildTest(FlaskView):
    def __init__(self):
        try:
            if self.setupLogger() == False:
                return
            if self.loadConfig() == False:
                return
            self.logger.info(f"Init done!")
        except Exception as ex:
            print(f"Init failed, exception: {ex}")

    def index(self):
        self.counter_index += 1
        return f"Hello World - index! {self.counter_index}"
    
    @route('/test')
    def entry_point(self):
        self.counter_test += 1
        self.logger.info("route =>'/test' - hit!")
        #return render_template('base.html')
        return f"Hello World from the test! {self.counter_test}"

    def setupLogger(self):
        status = False
        try:
            #logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S', filename = "dockerBuildTest.log", level=logging.INFO)
            logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S', filename = "/logs/dockerBuildTest.log", level=logging.INFO)
            self.logger = logging.getLogger(__name__)
            self.logger.info(f"app started!")
            status = True
        except Exception as ex:
            print(f"Init failed, exception: {ex}")
        return status

    def loadConfig(self):
        status = False
        try:
            self.config = {}
            #with open("config.yaml", "r") as stream:
            with open("/config/config.yaml", "r") as stream:
                self.config = yaml.safe_load(stream)
                self.counter_index = self.config["app"]["index"]
                self.counter_test = self.config["app"]["test"]
                self.logger.info(f"Config values {self.counter_index}, {self.counter_test} loaded!")
                status = True
        except Exception as ex:
            self.logger.error(f"Config load failed, exception: {ex}")
        return status
        
dockerBuildTest.register(flask_app, route_base = '/')
if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', debug=True) 
