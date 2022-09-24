int Echo = A4;
int Trig = A5;

#define ENA 5
#define ENB 6
#define IN1 7
#define IN2 8
#define IN3 9
#define IN4 11
int rightDistance = 0;
int leftDistance = 0;
int middleDistance = 0;
int carSpeed = 0;

void forward() {
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  Serial.println("Forward");
}

void back() {
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  Serial.println("Back");
}

void left() {
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  Serial.println("Left");
}

void right() {
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  Serial.println("Right");
}

void stop() {
  digitalWrite(ENA, LOW);
  digitalWrite(ENB, LOW);
  Serial.println("Stop!");
}

void setup() {
  Serial.begin(9600);
  pinMode(Echo, INPUT);
  pinMode(Trig, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  stop();
}

void loop() {
  // Read and execute commands from serial port
  if (Serial.available()) {  // check for incoming serial data

    // read command from serial port until terminator character
    String command = Serial.readString();

    // LED commands
    if (command == "led_on") {  // turn on LED
      digitalWrite(LED_BUILTIN, HIGH);
    } else if (command == "led_off") {  // turn off LED
      digitalWrite(LED_BUILTIN, LOW);
    } else if (command == "read_a0") {  // read and send A0 analog value
      Serial.println(analogRead(A0));
    }

    // Movement commands
    else if (command.substring(0,5) == "speed") {
      int speed = command.substring(5, command.length()).toInt();
      int carSpeed = speed;
    }
    else if (command == "forward") {
      Serial.println("Forward");
      forward();
    } else if (command == "back") {
      Serial.println("Back");
      back();
    } else if (command == "left") {
      Serial.println("Left");
      left();
    } else if (command == "right") {
      Serial.println("Right");
      right();
    } else if (command == "stop") {
      Serial.println("Stop");
      stop();
    }
  }
}
