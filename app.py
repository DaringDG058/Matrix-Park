from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# --- DATA STRUCTURES ---

# 1. THE 3D ARRAY (Represents the Building)
# Structure: [Floor][Row][Col]
# Dimensions: 3 Floors, 4 Rows (A,B,C,D), 10 Columns
parking_lot = [[[None for _ in range(10)] for _ in range(4)] for _ in range(3)]

# 2. THE HASH MAP (Represents the Database for fast lookup)
# Key: Car Number, Value: Location & Details
car_map = {}

# Constants
HOURLY_RATE = 50  # 50 Rupees per hour

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/park', methods=['POST'])
def park_car():
    data = request.json
    car_no = data.get('car_no')
    color = data.get('color')
    body_type = data.get('type')
    
    # Coordinates from user input
    f = int(data.get('floor')) - 1  # 0-indexed
    r = int(data.get('row')) - 1    # 0-indexed
    c = int(data.get('col')) - 1    # 0-indexed

    # Check if slot is empty
    if parking_lot[f][r][c] is not None:
        return jsonify({"success": False, "message": "Slot already occupied!"})
    
    # Check if car already exists
    if car_no in car_map:
        return jsonify({"success": False, "message": "Car already inside!"})

    # Create Car Object
    entry_time = time.time()
    car_details = {
        "number": car_no,
        "color": color,
        "type": body_type,
        "floor": f + 1,
        "row": r + 1,
        "col": c + 1,
        "entry_time": entry_time
    }

    # UPDATE DATA STRUCTURES
    parking_lot[f][r][c] = car_details  # Add to 3D Array
    car_map[car_no] = car_details       # Add to Hash Map

    return jsonify({"success": True, "message": "Car Parked Successfully!"})

@app.route('/api/status')
def get_status():
    # Send the whole 3D array to the frontend
    return jsonify(parking_lot)

@app.route('/api/leave', methods=['POST'])
def leave_car():
    data = request.json
    car_no = data.get('car_no')

    if car_no not in car_map:
        return jsonify({"success": False, "message": "Car not found!"})

    # Get details using Hash Map (O(1) complexity)
    car = car_map[car_no]
    f, r, c = car['floor']-1, car['row']-1, car['col']-1

    # Calculate Bill
    duration_sec = time.time() - car['entry_time']
    duration_min = round(duration_sec / 60, 2) # Representing minutes for demo
    bill_amount = max(10, round((duration_min / 60) * HOURLY_RATE)) # Min 10 Rs

    # REMOVE FROM DATA STRUCTURES
    parking_lot[f][r][c] = None # Clear Grid
    del car_map[car_no]         # Clear Map

    return jsonify({
        "success": True, 
        "message": f"Car Left! Duration: {duration_min} mins. Bill: ₹{bill_amount}"
    })

@app.route('/api/sorted')
def get_sorted_cars():
    # Requirement: List cars by time stayed (Descending)
    # We convert values of Hash Map to a list and sort
    current_cars = list(car_map.values())
    
    # Sort by entry_time (Smallest entry time = Longest stay)
    sorted_cars = sorted(current_cars, key=lambda x: x['entry_time'])
    
    return jsonify(sorted_cars)

if __name__ == '__main__':
    app.run(debug=True)
    