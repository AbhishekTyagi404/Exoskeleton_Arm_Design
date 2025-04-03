// --- Exoskeleton Arm Arduino Code ---
// Version: 1.1
// Author: Abhishek Tyagi
// Description: Button + EMG-based control with runtime safety, smoothing, and feedback

// --- Pin Definitions ---
const int liftButtonPin = 2;
const int lowerButtonPin = 3;
const int emgInputPin = A0;
const int motorIn1 = 8;
const int motorIn2 = 9;
const int enablePin = 10;
const int ledPin = 13; // Also used as mode indicator

// --- Configuration ---
bool useEMG = false;                    // Set true to use EMG instead of buttons
const int emgThreshold = 300;           // Activation threshold
const float alpha = 0.1;                // EMA smoothing factor
unsigned long maxRunTime = 5000;        // Max actuator time (ms)

// --- State ---
unsigned long startTime = 0;
bool isLifting = false;
float smoothedEMG = 0;

// --- Setup ---
void setup() {
  pinMode(liftButtonPin, INPUT_PULLUP);
  pinMode(lowerButtonPin, INPUT_PULLUP);
  pinMode(motorIn1, OUTPUT);
  pinMode(motorIn2, OUTPUT);
  pinMode(enablePin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  digitalWrite(ledPin, LOW);
}

// --- Main Loop ---
void loop() {
  int liftBtn = digitalRead(liftButtonPin);
  int lowerBtn = digitalRead(lowerButtonPin);
  int emgRaw = analogRead(emgInputPin);

  // Smooth the EMG using exponential moving average
  smoothedEMG = alpha * emgRaw + (1 - alpha) * smoothedEMG;

  // Show control mode via LED blink
  if (useEMG) {
    digitalWrite(ledPin, millis() % 1000 < 100);  // Blinks every second
  }

  // --- Control Logic ---
  if (useEMG && smoothedEMG > emgThreshold) {
    lift();
  } else if (!useEMG && liftBtn == LOW) {
    lift();
  } else if (!useEMG && lowerBtn == LOW) {
    lower();
  } else {
    stopMotor();
  }

  // --- Safety Cutoff ---
  if (isLifting && (millis() - startTime > maxRunTime)) {
    stopMotor();
    Serial.println("Safety Stop Triggered");
  }

  // --- Debug Output ---
  Serial.print("EMG_RAW:");
  Serial.print(emgRaw);
  Serial.print("  EMG_SMOOTH:");
  Serial.print(smoothedEMG);
  Serial.print("  State:");
  Serial.println(isLifting ? "LIFTING" : "IDLE");
}

// --- Actuation Functions ---
void lift() {
  digitalWrite(motorIn1, HIGH);
  digitalWrite(motorIn2, LOW);
  analogWrite(enablePin, 200);
  if (!isLifting) {
    startTime = millis();
    isLifting = true;
  }
}

void lower() {
  digitalWrite(motorIn1, LOW);
  digitalWrite(motorIn2, HIGH);
  analogWrite(enablePin, 180);
  if (!isLifting) {
    startTime = millis();
    isLifting = true;
  }
}

void stopMotor() {
  digitalWrite(motorIn1, LOW);
  digitalWrite(motorIn2, LOW);
  analogWrite(enablePin, 0);
  isLifting = false;
}
