#include "create.h"
#include <string.h>

char found = 0;
unsigned int i; //loop var
char* data;

void setup()
{
    Serial.begin(9600);
    delay(2000);
    create_init();
    while(!Serial);

    pinMode(TX, OUTPUT);
    pinMode(RX, INPUT);
    data = (char*)malloc(SONG_DATA_SIZE); //buffer large enough to hold any data for any command.
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
    char buff[5];
    unsigned char index = 0;

    while(index < 5)
    {
        if(Serial.available() > 0)
        {
            buff[index] = Serial.read();
            index++;
        }
    }

    if(strncmp(buff, "ohai\r", 5) == 0)
    {
        found = 1;
        Serial.print("kthxbai");
    }
}

void command_lookup()
{
    char command = 0;

    if(Serial.available() > 0)
    {
        command = Serial.read();
        i = Serial.readBytesUntil(TERMINATOR, data, SONG_DATA_SIZE);
       /* while(Serial.available() > 0)
        {
            data[i] = Serial.read();
        }*/
        
        switch(command)
        {
            case MODESAFE:
                oi_safe();
                break;
            case MODEFULL:
                oi_full();
                break;
            case USEDEMO:
                if(i > 0)
                    data[0] = Serial.read();
                #ifdef DEBUG
                else 
                {
                    Serial.println("No demo selected!");
                    break;
                }
                #endif
                demo(data[0]); 
                break;
            case DRIVE_DIRECT:
                if( i == 4) 
                    drive_direct(data);
                
                #ifdef DEBUG
                else Serial.println("Not enough data sent");
                #endif
                break;
            case DRIVE:                 
                if( i == 4) 
                    drive(data);
                
                #ifdef DEBUG
                else Serial.println("Not enough data sent");
                #endif
                break;
            case WHEELSTOP:
                for(i = 0; i < DRIVE_DATA_SIZE; i++) data[i] = 0;
                drive(data);
                #ifdef DEBUG
                Serial.println("Stopping all wheel motion");
                #endif
                break;
            default:
                #ifdef DEBUG
                Serial.println("Invalid command");
                #endif
        }
    }
}

