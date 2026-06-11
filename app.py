from flask import Flask, render_template, request, jsonify
from brain import get_hassan_response

app = Flask(__name__)



@app.route('/')
def landing():
   
    return render_template('landing.html')

@app.route('/plan-trip')
def plan_trip():
    return render_template('plan_trip.html')


@app.route('/famous-places') 
def famous_places():
    return render_template('famous_places.html')

@app.route('/chat')
def dashboard():

    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"response": "I didn't hear anything!"})
    
    try:
        bot_response = get_hassan_response(user_message)
        return jsonify({"response": bot_response})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(port=5001, debug=True)