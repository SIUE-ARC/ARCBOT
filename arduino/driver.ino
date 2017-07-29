#include <SoftwareSerial.h>
#include <string.h>

#define     CREATE_TX   2
#define     CREATE_RX   3

char found = 0;

SoftwareSerial create_link(CREATE_RX, CREATE_TX);

void setup()
{
    Serial.begin(9600);
    create_link.begin(57600);
    while(!Serial);
}

void loop()
{
    while(discover() == -1)
    {
        discover();
    }
    if(found)
        Serial.print("kthxbai");
}

char discover()
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
        return 0;
    }
    else
        return -1;
}
