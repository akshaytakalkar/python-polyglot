from flask import Flask, flash, url_for, request, jsonify
# from process import do_calculation

app = Flask(__name__)

def do_calculation(number1):
    # isPrime = check_prime(number1)
    if check_prime(number1): 
        # return "It is prime number"
        index = 10
        for i in range(1, len(str(number1))):
            tmp = number1 % index
            if check_prime(tmp) == False: return "Not prime in left trunket"
            index = index * 10
        index = 10
        for i in range(1, len(str(number1))):
            tmp = number1 / index
            if check_prime(int(tmp)) == False: return "Not prime in Right trunket"
            index = index * 10
        return "It is double side prime number"
    else:
        return "Not prime number "
    

def check_prime(number1):
    if number1 > 1:
        for i in range(2, number1):
            if (number1 % i) == 0:
                return False
        else:
            return True

@app.route('/')
def homepage():
    return "You should now this relm"

@app.route('/prime/')
def prime():
    return "provide number in Path"

@app.route('/prime/<number>')
def print_number(number):
    # check_int = isinstance(number, str)
    check_int = number.isnumeric()
    if check_int:
        try:
            result = do_calculation(int(number))
            return " " + result
        except Exception as e:
            return "Exception " + str(e)
    else:
        return "Provided is not valid numeric value"

#ERROR
@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == "__main__":
    app.run()
