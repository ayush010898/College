
int led = 13;

void setup() {
  pinMode(led,OUTPUT);
}

void loop() {
  for (int fadeValue = 0 ; fadeValue <= 255; fadeValue += 5) {
    analogWrite(led, fadeValue);
    delay(30);
  }

  for (int fadeValue = 255 ; fadeValue >= 0; fadeValue -= 5) {
    analogWrite(led, fadeValue);
    delay(30);
  }
}
