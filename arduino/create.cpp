#include "create.h"
#include <arduino.h>

SoftwareSerial create_link(CREATE_RX, CREATE_TX);

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

