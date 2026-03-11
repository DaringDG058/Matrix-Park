# 🚗 Matrix Park: Smart Parking System

**Matrix Park** is a high-efficiency parking management solution built to handle multi-floor logistics. It combines a visual 3D representation of a parking structure with a backend optimized for $O(1)$ search performance.

---

## 👥 Team Members
* **K M Dushyanth Gowda** (1MS24IS058)
* **Rohan Joshi** (1MS24IS097)

---

## 🚀 Project Overview
This system manages a parking lot with **3 Floors**, **4 Lanes per floor**, and **10 Slots per lane** (120 slots total). It allows operators to park vehicles, track their duration, calculate automated bills, and sort vehicles by stay duration.

### **Core Functionalities**
* **Real-time Grid:** A 3D visual representation of the building's occupancy.
* **Instant Lookup:** Find any car instantly using its registration number.
* **Smart Billing:** Automated fee calculation based on entry timestamps ($50/hour).
* **Sorting Logic:** Display cars based on who has stayed the longest.

---

## 🛠️ Tech Stack & Architecture

| Component | Technology |
| :--- | :--- |
| **Backend** | Python (Flask) |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) |
| **API** | RESTful JSON API |

### **Data Structures Used**
1. **3D Array (`[[[]]]`):** Used to represent the physical building ($3 \times 4 \times 10$). This allows for precise spatial mapping and UI rendering.
2. **Hash Map (`{} / Dict`):** Used for storing car details. This ensures that operations like "Exit & Bill" happen in **$O(1)$ time complexity**, rather than searching through every floor.
3. **Sorting Algorithms:** Utilizes Timsort (Python's built-in `sorted()`) to organize vehicle stays in $O(n \log n)$ time.

---

## 📸 System Walkthrough

### **1. Main Dashboard**
The main interface displays the live status of all 120 slots across three floors. Red slots indicate occupied spaces.
![Main Dashboard](./Screenshot/2025-12-02103457.png)

### **2. Occupancy Management**
The system tracks specific details for every vehicle, including plate number, color, and body type (SUV/Sedan).
![Occupancy View](./Screenshot/2025-12-02104219.png)

### **3. Duration & Analytics**
The "View Sorted List" feature retrieves data from the Hash Map and sorts it to show which vehicles have been in the lot the longest.
![Sorting View](./Screenshot/2025-12-02104233.png)

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone [https://github.com/your-username/matrix-park.git](https://github.com/your-username/matrix-park.git)
   cd matrix-park
2. **Install Dependencies**
This project requires Python and the Flask web framework.
   ```bash
   pip install flask
3. **Project Structure**
To ensure the application runs correctly, organize your files as follows:
   ```bash
   matrix-park/
    ├── app.py              # Flask Backend Logic
    ├── templates/
    │   └── index.html      # Frontend (HTML, CSS, and JS)
    ├── Screenshot...png    # UI Assets (Keep in root for README visibility)
    └── README.md           # Project Documentation
4. **Run the Application**
Start the local development server:
   ```bash
   python app.py

Once the server is running, open your web browser and navigate to:
http://127.0.0.1:5000

---

## 📊 Performance Analysis

The efficiency of **Matrix Park** is achieved through the strategic combination of two primary data structures. This "Hybrid Approach" ensures the system remains fast even as the parking lot scales.

### **1. 3D Array Representation**
The parking lot is logically modeled as `parking_lot[floor][lane][slot]`.
* **Purpose:** Provides a direct spatial mapping of the physical environment.
* **Complexity:** Accessing a specific slot via coordinates is **$O(1)$**.
* **Benefit:** Simplifies UI rendering by mirroring the building's physical layout.

### **2. Hash Map Optimization**
Vehicle details are mirrored in a Hash Map (`car_map`) where the `Car Registration Number` is the key.
* **The Search Problem:** In a standard 3D array, finding a specific car by its number plate would require a nested loop with **$O(Floor \times Lane \times Slot)$** complexity.
* **The Solution:** By using a Hash Map, we can locate any car and its metadata (entry time, position) in **$O(1)$ constant time**. 
* **Complexity:** Retrieval and deletion are both **$O(1)$**.

### **3. Sorting Algorithm**
The "Longest Stay" feature uses Python’s internal Timsort algorithm.
* **Complexity:** **$O(n \log n)$**, where $n$ is the number of currently parked cars.
* **Logic:** It sorts vehicles based on their Unix entry timestamps to prioritize those who parked earliest.

---

## 🔮 Future Scope

To evolve Matrix Park into a production-grade enterprise solution, the following features are planned:
1.  **Persistent Storage:** Transition from in-memory data structures to a persistent database like **PostgreSQL** or **MongoDB** to prevent data loss on server restarts.
2.  **QR Code Integration:** Generate unique QR codes for tickets that users can scan to view their real-time bill.
3.  **Slot Recommendation:** An algorithm to automatically suggest the "optimal" slot (e.g., closest to the exit or elevator).
4.  **Security Auth:** A dedicated admin login for parking attendants to prevent unauthorized billing changes.

---

## 📄 License
Distributed under the **MIT License**. See `LICENSE` for more information.

---

### 🌟 Acknowledgments
Special thanks to the open-source community for the tools and documentation that made this project possible. If you find this project useful, please consider giving it a ⭐ on GitHub!
