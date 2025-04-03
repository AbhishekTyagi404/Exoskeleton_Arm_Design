# 💪 Exoskeleton Arm Design and Development

This repository contains the complete hardware, software, and documentation for the **Low-Cost, Wearable Upper Limb Exoskeleton Arm** designed by **Abhishek Tyagi**. The system is intended for **rehabilitation**, **strength augmentation**, and **assistive robotics** applications.

---

## 📌 Project Overview

The Exoskeleton Arm is a lightweight, untethered, battery-powered system designed to:
- Aid patients in physical therapy or post-injury rehabilitation
- Reduce physical strain in industrial lifting jobs
- Provide portable, ergonomic support for upper-limb augmentation

The system uses an **Arduino microcontroller**, **DC motor with linear actuator**, and **button or EMG-based control interface**, all mounted in a wearable backpack frame.

---

## 🧠 Features

- Button-based interface for **lifting and lowering**
- EMG (Electromyography) sensor compatibility for **muscle-controlled actuation**
- Low-cost design using **aluminum frame**, **Toyota Glass Motor**, and **Arduino UNO**
- Modular and backpack-mounted for **easy mobility**
- Tested lifting capacity: **up to 20 kg** beyond human capability
- MATLAB simulations for torque & kinematic validation

---

## 📂 Repository Structure

```
exoskeleton-arm-design/
│
├── README.md                      ← You are here
├── docs/                          ← Final Report & IEEE Research Paper
├── hardware/                      ← CAD designs, BOM, frame overview
├── firmware/                      ← Arduino code + signal processing logic
├── simulations/                   ← MATLAB models for torque & kinematics
├── data/                          ← Sample EMG & motion data
└── images/                        ← Diagrams, GIFs, project photos
```

---

## 🔧 Hardware Components

| Component              | Description                        |
|------------------------|------------------------------------|
| Arduino Uno R3         | Main controller board              |
| 12V Toyota Glass Motor | High torque actuator (elbow joint) |
| Linear Actuator        | Elbow bending assistance           |
| L298N Driver Module    | Dual H-Bridge motor controller     |
| MyoWare EMG Sensor     | Muscle signal input (optional)     |
| 12V Battery Pack       | Power source (7.2Ah recommended)   |
| Aluminium Frame        | Arm structure and shoulder support |

---

## ⚙️ Software Tools

- **Arduino IDE** – Firmware development
- **MATLAB (Robotics Toolbox)** – Kinematic & torque modeling
- **Fusion 360 / SolidWorks** – CAD design
- **Python (optional)** – Signal filtering for EMG inputs

---

## 🧪 Testing & Results

- **Response Time**: < 100 ms (button to actuation)
- **Lifting Capacity**: 5–20 kg verified loads
- **Operation Time**: ~2.5 hours on 12V battery
- **Volunteer Testing**: No fatigue reported after 20+ min

---

## 📈 Future Work

- Replace buttons with real-time EMG signal-based control
- Brain-Computer Interface (BCI) control support
- Real-time load feedback and adaptive actuation
- Integrate telemetry for motion capture and cloud monitoring

---

## 👨‍🔬 Author

**Abhishek Tyagi**  
Mechatronics Engineering – GGSIPU  
`mechatronics.abhishek@gmail.com`  
Collaborated with DRDO INMAS under the guidance of Dr. Sushil Chandra

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---
