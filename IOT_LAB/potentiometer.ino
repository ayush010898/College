int led = 11;
int resistor = 2;
void setup() {
  pinMode(led,OUTPUT);
  pinMode(resistor,INPUT);
  Serial.begin(9600);
}

void loop() {
  int resistance = analogRead(resistor);
  int brightness = map(resistance,0,1023,0,255);
  Serial.print("input");
  Serial.print("resistance");
  Serial.print("converted");
  Serial.print("brightness");
}
