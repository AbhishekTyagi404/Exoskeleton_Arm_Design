// --- Exoskeleton Arm Arduino Code ---
// Version: 1.0
// Author: Abhishek Tyagi
// Description: Button + EMG-based control for elbow joint actuation

// Pin Definitions
const int liftButtonPin = 2;       // Push button to lift
const int lowerButtonPin = 3;      // Push button to lower
const int emgInputPin = A0;        // EMG analog input (optional)
const int motorIn1 = 8;            // L298N IN1
const int motorIn2 = 9;            // L298N IN2
const int enablePin = 10;          // L298N ENA (PWM)
const int ledPin = 13;             // Status LED

// Configuration
bool useEMG = false;               // Set to true to enable EMG control
const int emgThreshold = 300;      // Threshold for EMG activation
unsigned long maxRunTime = 5000;   // Max motor run time in ms (safety cutoff)

// State
unsigned long startTime = 0;
bool isLifting = false;

void setup() {
  pinMode(liftButtonPin, INPUT_PULLUP);
  pinMode(lowerButtonPin, INPUT_PULLUP);
  pinMode(motorIn1, OUTPUT);
  pinMode(motorIn2, OUTPUT);
  pinMode(enablePin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int liftBtn = digitalRead(liftButtonPin);
  int lowerBtn = digitalRead(lowerButtonPin);
  int emgVal = analogRead(emgInputPin);

  if (useEMG && emgVal > emgThreshold) {
    lift();
  } else if (liftBtn == LOW) {
    lift();
  } else if (lowerBtn == LOW) {
    lower();
  } else {
    stopMotor();
  }

  // Safety Cutoff
  if (isLifting && (millis() - startTime > maxRunTime)) {
    stopMotor();
  }
}

void lift() {
  digitalWrite(motorIn1, HIGH);
  digitalWrite(motorIn2, LOW);
  analogWrite(enablePin, 200); // ~80% speed
  digitalWrite(ledPin, HIGH);
  if (!isLifting) {
    startTime = millis();
    isLifting = true;
  }
}

void lower() {
  digitalWrite(motorIn1, LOW);
  digitalWrite(motorIn2, HIGH);
  analogWrite(enablePin, 180); // ~70% speed
  digitalWrite(ledPin, HIGH);
  if (!isLifting) {
    startTime = millis();
    isLifting = true;
  }
}

void stopMotor() {
  digitalWrite(motorIn1, LOW);
  digitalWrite(motorIn2, LOW);
  analogWrite(enablePin, 0);
  digitalWrite(ledPin, LOW);
  isLifting = false;
}
