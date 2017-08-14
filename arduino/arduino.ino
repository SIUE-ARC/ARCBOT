#include "create.h"
#include <string.h>

char found = 0;

void setup()
{
    Serial.begin(9600);
    delay(2000);
    create_init();
    while(!Serial);

    pinMode(CREATE_TX, OUTPUT);
    pinMode(CREATE_RX, INPUT);
}

void loop()
{
    while(!found)
    {
        discover();
    }

    command_lookup();
}

void discover()
{
    char buff[4];
    char index = 0;

    while(index < 4)
    {
        if(Serial.available() > 0)
        {
            buff[index] = Serial.read();
            index++;
        }
    }

    if(strncmp(buff, "ohai", 4) == 0)
    {
        found = 1;
        Serial.print("kthxbai");
    }
}

void command_lookup()
{
    char command = 0;
    char* data;

    if(Serial.available() > 0)
    {
        command = Serial.read();

        switch(command)
        {
            case 's':
                oi_safe();
                break;
            case 'f':
                oi_full();
                break;
            case 'd':
                demo(DEMO_BANJO);
                break;
            default:
                #ifdef DEBUG
                Serial.print("Invalid command");
                #endif
        }
    }
}

