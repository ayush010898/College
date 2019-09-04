int BUZZER = 7;
int flame_sensor = 4;
void setup()
{
  Serial.begin(9600);
  pinMode(BUZZER, OUTPUT);
  pinMode(flame_sensor, INPUT);
}
void loop()
{
  int flame_detected = digitalRead(flame_sensor);
  if (flame_detected == 0)
  {
    Serial.println("Flame detected");
    digitalWrite(BUZZER, HIGH);
    delay(200);
    digitalWrite(BUZZER, LOW);
    delay(200);
  }
  else
  {
    Serial.println("No flame");
    digitalWrite(BUZZER, LOW);
  }
  delay(1000);
}
