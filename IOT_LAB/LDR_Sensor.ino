int led = 11;
int ldr = A0;
void setup() {
  pinMode(led,OUTPUT);
  pinMode(ldr,INPUT);
  Serial.begin(9600);
}

void loop() {
  int sensedValue = analogRead(ldr);
  if(sensedValue > 200)
  {
    digitalWrite(led,HIGH);
    Serial.println(sensedValue);
    delay(100);
  }
  else
  {  
    digitalWrite(led,LOW);
    Serial.println(sensedValue);
    delay(100);
  }

}
