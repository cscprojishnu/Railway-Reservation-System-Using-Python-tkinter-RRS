# Railway-Reservation-System-Using-Python-tkinter

# 🚆 Train Ticket Booking System (Python + MySQL GUI)

A GUI-based Train Ticket Booking System developed using **Python (Tkinter)** for the front-end and **MySQL** for the back-end. This project was designed with the goal of learning by building — from scratch, without referencing prior systems.

📌 **Published in**: *Journal of Electrical Electronics Engineering, Vol 4, Issue 3 (2025)*  
📅 **Published Date**: June 11, 2025  
👤 **Author**: Jishnu Teja Dandamudi, Amrita School of Artificial Intelligence

---

## 📌 Features

### 👨‍💼 Admin Mode
- **Add Train**: Enter train number, name, and running days
- **Assign Seats**: Configure Sleeper (SL), 2A, 3A coaches
- **Add Train Route**: Add station codes, names, and timings
- **Reservation Chart**: View passengers' booking details
- **Delete Train**: Safely remove train and associated data

### 👤 User Mode
- **Book Ticket**: Browse trains, book seats, generate PNR
- **PNR Enquiry**: Retrieve ticket and passenger info
- **Cancel Ticket**: Cancel ticket using PNR
- **Booking History**: Export and view past bookings in `.txt`

---

## 🧱 Tech Stack

| Layer     | Technology          |
|-----------|---------------------|
| Frontend  | Python (Tkinter)    |
| Backend   | MySQL (via Connector) |
| File I/O  | Text files for logs |
| Language  | Python 3.x          |

---

## 🗂 Database Structure

### 🔧 Tables Used

- **`trains`**  
  Stores metadata (number, name, days)

- **`user_bookings`**  
  Contains passenger details, ticket status, PNR, and journey info

- **Dynamic Train Tables**  
  Each train has a unique table storing its route info

---

