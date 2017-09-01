#include "hardware.h"

Servo s0, s1;

/*
    Sets the appropriate pin modes for all sensors and 
    initializes the servo objects.
 */
void init_hardware()
{
    #ifdef DEBUG
    Serial.println("Setting pin modes for hardware."
    #endif
    pinMode(ULTRASOUND0_PIN, OUTPUT);
    pinMode(ULTRASOUND1_PIN, OUTPUT);
    pinMode(ULTRASOUND2_PIN, OUTPUT);
    pinMode(ULTRASOUND3_PIN, OUTPUT);
    pinMode(IR0_PIN, INPUT_PULLUP);
    pinMode(IR1_PIN, INPUT_PULLUP);
    pinMode(IR2_PIN, INPUT_PULLUP);
    s0.attach(SERV0_PIN);
    s1.attach(SERV1_PIN);
}

/*
    Sets the pulse width on the specified servo PWM.
 */
void servo(char* data)
{
    short* microseconds = (short*)(void*)&data[1];
    #ifdef DEBUG
    if(data[0] > 1 || data[0] < 0) 
    {
        Serial.println("Servo number must be between 0-1");
        return;
    }
    else
    {
        Serial.print("Setting servo: ");
        Serial.print(data[0]);
        Serial.print(" PWM to pulse width ");
        Serial.print(microseconds);
        Serial.println(" microseconds.");
    }
    #endif

    (data[0] == 0) ? s0.writeMicroseconds(microseconds):s1.writeMicroseconds(microseconds);
}

void ir_sensor(char data)
{
    
}

void ultrasonic(char data)
{
    long duration;
    double cm;
    char pin;

    switch(data)
    {
        case 0:
            pin = ULTRASOUN0_PIN;
            break;
        case 1:
            pin = ULTRASOUN1_PIN;
            break;
        case 2:
            pin = ULTRASOUN2_PIN;
            break;
        case 3:
            pin = ULTRASOUN3_PIN;
            break;
        default:
            #ifdef DEBUG
            Serial.print("Invalid sensor number (0-3)");
            #endif
            break;
    }
    
    #ifdef DEBUG
    Serial.print("Pinging on Ultrasonic ");
    Serial.print(data);
    Serial.print(": ");
    #endif
    pinMode(pin, OUTPUT);
    digitalWrite(pin, LOW);
    delayMicroseconds(2);
    digitalWrite(pin, HIGH);
    delayMicroseconds(5);
    pinMode(pin, INPUT);
    duration = pulseIn(pin, HIGH);
    cm = ((double)duration)/29.0/2.0;
    #ifdef DEBUG
    Serial.println(cm);
    #else
    Serial.write(cm);
    #endif

    return cm;
}

