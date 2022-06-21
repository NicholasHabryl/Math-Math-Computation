void setup(){ 
    pinMode(11, INPUT); 
    pinMode(2, INPUT);
    pinMode(3, INPUT);
    pinMode(4, INPUT);
    pinMode(5, INPUT);
    pinMode(6, INPUT);
    pinMode(7, INPUT);
    pinMode(8, INPUT);
  Serial.begin(9600); 
  Serial.print("setup \n"); 
  
}

void loop(){
  
  if (digitalRead(11) ==LOW) {
    Serial.print("1\n");
    delay(250);
  }
  else if(digitalRead(2) ==LOW) {
    Serial.print("2\n");
    delay(250);
  }
 else if(digitalRead(3) ==LOW) {
    Serial.print("3\n");
    delay(250);
  } 
  else if(digitalRead(4) ==LOW) {
    Serial.print("4\n");
    delay(250);
  }
else if(digitalRead(5) ==LOW) {
    Serial.print("5\n");
    delay(250);
  }
else if(digitalRead(6) ==LOW) {
    Serial.print("6\n");
    delay(250);
  }
else if(digitalRead(7) ==LOW) {
    Serial.print("7\n");
    delay(250);
  }
else if(digitalRead(8) ==LOW) {
    Serial.print("8\n");
    delay(250);
  }



  
}
