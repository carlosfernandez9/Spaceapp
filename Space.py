# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, jsonify, request
import time


app = Flask(__name__)

# Global variables to track turns and timer
turns_remaining = 4
start_time = None


@app.route('/')
def home():
    return ("Bienvenido a la API de Combate Espacial. Usa las rutas disponibles para interactuar con la API.", 200)

# First GET /status to get the damaged system
# @app.route('/status', methods=['GET'])
# def status():
#     global damaged_system
#     # You can choose the damaged system randomly, for example:
#     damaged_system = random.choice(list(systems.keys()))  # Or pick it dynamically based on your logic
    
#     # Return the damaged system as JSON
#     return jsonify({"damaged_system": damaged_system}), 200

@app.route('/perform-turn', methods=['POST'])
def send_data():
    global turns_remaining, start_time
    
    if start_time is None:
        start_time = time.time()
        turns_remaining = 4
    
    # Get JSON data from the incoming request
    incoming_data = request.get_json()
    
    attack_position = incoming_data.get("attack_position", {})
    x = attack_position.get("x")  # x is a string
    y = attack_position.get("y")  # y is an integer
    
    if turns_remaining > 0 and (600 - (time.time() - start_time)) > 0:
        turns_remaining = turns_remaining - 1
        
        # Check if the action is "radar"
        if incoming_data.get("action") == "radar":
            # Return the predefined response format when action is "radar"
            response = {
                "performed_action": "radar",
                "turns_remaining": turns_remaining,
                "time_remaining": 600 - (time.time() - start_time),
                "action_result": "a01b01c01d01e01f01g01h01|a02b02c02d02e$2f02g02h02|a03b03c03d03e03f03g03h$3|a04b04c04d04e04f04g04h04|a05b05c05d05e$5f05g^5h05|a06b06c06d06e$6f06g06h06|a07b07c07d07e07f07g07h07|a08b08c08d08e08f#8g08h08|",
                "message": "a01b01c01d01e01f01g01h01|a02b02c02d02e$2f02g02h02|a03b03c03d03e03f03g03h$3|a04b04c04d04e04f04g04h04|a05b05c05d05e$5f05g^5h05|a06b06c06d06e$6f06g06h06|a07b07c07d07e07f07g07h07|a08b08c08d08e08f#8g08h08|",
            }
            return jsonify(response)
        else:
            turns_remaining = 0
            response = {
                "performed_action": "attack",
                "turns_remaining": 0,
                "time_remaining": 600 - (time.time() - start_time),
                "action_result": "Attacked",
                "message": f'Attack position: x={x}, y={y}',
            }
            return jsonify(response)
    else:
        turns_remaining = 4
        start_time = None
            

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)