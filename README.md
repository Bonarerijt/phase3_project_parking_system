# Parking Management System

#### Date: 2025/12/05

#### By *Judy Ogachi*

## Project Overview
The **Parking Management System** is a Python-based **Command Line Interface (CLI) application** designed to manage parking operations efficiently.  
It tracks vehicles entering and leaving a parking lot, assigns available slots, calculates parking fees, and maintains organized records of all parking activities.  

The CLI allows users to interact with the system in a **menu-driven interface**, making operations straightforward even without a graphical interface.

---

## CLI Functionality
The CLI menu provides the following options:

1. **Park Vehicle** – Enter a vehicle into the system by specifying the license plate. The system automatically assigns the next available slot.  
2. **Exit Vehicle** – Remove a vehicle from the parking lot, record the exit time, and calculate the parking fee based on duration.  
3. **View Parking Status** – Display current slot availability for all groups, showing whether each slot is free or occupied, along with the vehicle plate and duration.  
4. **View Parking History** – List all past parking sessions including entry and exit times, assigned slots, and total fees paid.  
5. **Quit** – Exit the application.

The CLI is **interactive and user-friendly**, ensuring smooth operations and quick access to all essential features.

---

## Core Functions
The system supports the following core functionalities:

- **Vehicle Registration** – Tracks all vehicles that use the parking lot.  
- **Slot Assignment** – Automatically assigns available slots when a vehicle enters.  
- **Session Tracking** – Monitors each parking session from entry to exit.  
- **Fee Calculation** – Calculates parking fees based on duration using a pre-defined rate per minute.  
- **Parking History** – Maintains a detailed record of all past parking sessions for accountability and reporting.

---

## Database Models
The system uses **SQLite** with **SQLAlchemy ORM** to define its database structure. The main models are:

1. **ParkingSlot** – Represents each parking slot and its availability.  
2. **ParkingHistory** – Records each parking session, including vehicle, slot, entry/exit times, and total fees.  

This structure ensures data consistency, scalability, and easy querying for real-time slot availability and reporting.

---

## Technologies Used
- **Python 3** – Core programming language.  
- **SQLite3** – Lightweight relational database for storing all parking data.  
- **SQLAlchemy ORM** – Handles database operations in an object-oriented way.  
- **Command Line Interface (CLI)** – Interactive menu system for managing the parking system.

---

## Usage
1. Run the application using:
    ```bash
    python3 app.py
    ```

## Live Link
[Git]https://github.com/Bonarerijt/phase3_project_parking_system.git


## 🎥 Demo
Watch the demo here: [Video](https://www.veed.io/view/a5a8e7f6-dab8-4b3d-92c5-2894441c3645?source=Homepage&panel=share)


## Future Enhancements
- Add **different vehicle types** with different rates   
- Expand to a **web-based or GUI version** for more usability 


## Support and contact details
github.com/Bonarerijt

### License
MIT License

Copyright (c) 2025 Bonarerijt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

