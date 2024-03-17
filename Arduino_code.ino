int lm36Pin = A0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600) ;
}

void loop() {
  // put your main code here, to run repeatedly:
  int analogValue;
  float temperature;

  // read our temperature sensor
    analogValue = analogRead(lm36Pin);

    // convert the 10bit analog value to mT
    float mT = 0.097*analogValue-50;
    //temperature = (mV - 500) / 10;
    Serial.println(mT);
    //Serial.print("mV  ");
    // print the temperature over serial
    //Serial.print("Temp: ");
    //Serial.print(temperature);
    //Serial.println("C");
    
    // wait 1s before reading the temperature again
    delay(2000);
}
