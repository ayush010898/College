
int GREEN = 6;
int YELLOW = 5;
int RED = 4;

void setup() {
  pinMode(GREEN, OUTPUT);
  pinMode(YELLOW, OUTPUT);
  pinMode(RED, OUTPUT);
}

void loop() {
  green_light();
  delay(5000);
  yellow_light();
  delay(2000);
  red_light();
  delay(5000);
}

void green_light()
{
  digitalWrite(GREEN, HIGH);
  digitalWrite(YELLOW, LOW);
  digitalWrite(RED, LOW);
}

void yellow_light(){
  digitalWrite(YELLOW, HIGH);
  digitalWrite(GREEN, LOW);
  digitalWrite(RED, LOW);
}

void red_light(){
  digitalWrite(RED, HIGH);
  digitalWrite(GREEN, LOW);
  digitalWrite(YELLOW, LOW);
}

