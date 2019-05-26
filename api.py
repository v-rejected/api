from flask import Flask
from flask_restful import abort, Api, Resource
from fibonacci import fibonacci_calc, Max_Value

app = Flask(__name__)
api = Api(app)


'''
    Check input on invalid arguments returns appropiate error message, on valid arguments returns result
'''
def abort_if_parameter_exceeds_max_value(id):
    try:
        val = int(id)
    except:
        abort(500, message="The requested value is: {} Enterer value isn't positive integer.".format(id))
    if val < 0:
        abort(500, message="The value requested is {} however function calculates if input is positive integer. ".format(id))
    elif val > Max_Value:
        abort(500, message="The value of {} is bigger than {} ".format(id, Max_Value))
    elif val == 0:
       abort(500, message="The value of {} is NULL. ".format(id))

# Fib
# returns the Fibonacci list of values calculated for the passed parameter
class Fib(Resource):
    def get(self, id):
        abort_if_parameter_exceeds_max_value(id)
        return fibonacci_calc(id)


api.add_resource(Fib, '/api/<string:id>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
