#include <Arduino.h>

#define SERIAL_SPEED 115200
#define GAUGE_PIN 10
#define LIGHT_PIN 11


void setup() {
	Serial.begin(SERIAL_SPEED);
}

void loop() {
	if ( Serial.available() >= 2 ) {
		char cmd = Serial.read();
		char value = Serial.read();
		switch ( cmd ) {
			case 0: analogWrite(GAUGE_PIN, value); break;
			case 1: analogWrite(LIGHT_PIN, value); break;
			default: break;
		}
	}
	delay(1);
}
