#include "create.h"
#include <arduino.h>

SoftwareSerial create_link(RX, TX);

void create_init()
{
    create_link.begin(BAUD);
    delay(50);
    create_link.write(STARTOP);
    #ifdef DEBUG
    Serial.println("Create link established");
    #endif
}

void oi_safe()
{
    //create_link.write(STARTOP);
    create_link.write(SAFEOP);
    #ifdef DEBUG
    Serial.println("Create put in Safe mode");
    #endif
}

void oi_full()
{
    //create_link.write(STARTOP);
    create_link.write(FULLOP);
    #ifdef DEBUG
    Serial.print("Create put in Full mode");
    #endif
}

void demo(char data)
{
    create_link.write(DEMOOP);
    
    if(data < 0 || data > 9)
    {
        #ifdef DEBUG
        Serial.println("Invalid demo. Aborting");
        #endif
        create_link.write(-1);
    }
    else
    {
        create_link.write(data);
    }
    #ifdef DEBUG
    Serial.println("Playing a Demo");
    #endif
}

void drive(char* data)
{
    #ifdef DEBUG
    short speed = data[0]*256;
    speed |= data[1];
    short radius = data[2]*256;
    radius |= data[3];

    Serial.print("Sending speed: ");
    Serial.print(speed);
    Serial.print(" Radius: ");
    Serial.println(radius);
    #endif
    create_link.write(data, DRIVE_DATA_SIZE);
}

void drive_direct(char* data)
{
    #ifdef DEBUG
    short rspeed = data[0]*256;
    rspeed |= data[1];
    short lspeed = data[2]*256;
    lspeed |= data[3];

    Serial.print("Sending right wheel speed: ");
    Serial.println(rspeed);
    Serial.print("Sending left wheel speed: ");
    Serial.println(lspeed);
    #endif
    create_link.write(data, DRIVE_DIRECT_DATA_SIZE);
}

