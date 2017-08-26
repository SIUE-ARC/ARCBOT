#include "create.h"
#include <arduino.h>

SoftwareSerial create_link(RX, TX);

void create_init()
{
    create_link.begin(BAUD);
    create_link.write(STARTOP);
    #ifdef DEBUG
    Serial.println("Create link established");
    #endif
}

/*
    This command puts the OI into Safe mode, enabling user
    control of Create. It turns off all LEDs. The OI can be in
    Passive, Safe, or Full mode to accept this command.
*/
void oi_safe()
{
    //create_link.write(STARTOP);
    create_link.write(SAFEOP);
    #ifdef DEBUG
    Serial.println("Create put in Safe mode");
    #endif
}

/*
    This command gives you complete control over Create
    by putting the OI into Full mode, and turning off the cliff,
    wheel-drop and internal charger safety features. That is, in
    Full mode, Create executes any command that you send
    it, even if the internal charger is plugged in, or the robot
    senses a cliff or wheel drop.
*/
void oi_full()
{
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
        #ifdef DEBUG
        Serial.println("Playing a Demo");
        #endif
    }
}

/*
    Allows create to move in an arc or straight line.
    Documentiation on this command (page 9): https://www.irobot.com/filelibrary/pdfs/hrd/create/Create%20Open%20Interface_v2.pdf
*/
void drive(char* data)
{
    #ifdef DEBUG
    short speed = (short)data[0]*256;
    Serial.print("Sending speed: ");
    Serial.print(speed);
    speed += (short)data[1];
    short radius = (short)data[2]*256;
    Serial.print(" Radius: ");
    Serial.println(radius);
    radius += (short)data[3];

    Serial.print("Sending speed: ");
    Serial.print(speed);
    Serial.print(" Radius: ");
    Serial.println(radius);
    #endif
    create_link.write(DRIVEOP);
    create_link.write(data, DRIVE_DATA_SIZE);
}

/*
    Allows independent control of each create wheel.
    Documentiation on this command (page 9): https://www.irobot.com/filelibrary/pdfs/hrd/create/Create%20Open%20Interface_v2.pdf
*/
void drive_direct(char* data)
{
    #ifdef DEBUG
    short rspeed = data[0]*256;
    rspeed += data[1];
    short lspeed = data[2]*256;
    lspeed += data[3];

    Serial.print("Sending right wheel speed: ");
    Serial.println(rspeed);
    Serial.print("Sending left wheel speed: ");
    Serial.println(lspeed);
    #endif
    create_link.write(DRIVEDOP);
    create_link.write(data, DRIVE_DIRECT_DATA_SIZE);
}

/*
    This command changes the state of one of the lEDs on 
    the create. The Advance and Play LEDs can be on or off
    and the Power LED can change color and intensity.
 */
void leds(char* data)
{
    #ifdef DEBUG
    if(data[0] == 0)
        Serial.println("Turning off Advance and Play LEDs");
    else if(data[0] == 2)
        Serial.println("Turning on only the Play LED");
    else if(data[0] == 8)
        Serial.println("Turning on only the Advance LED");
    else if(data[0] == 10)
        Serial.println("Turning on Adance and Play LEDs");
    else
        Serial.println("Invalid LED configuration specified");

    Serial.print("Color: ");
    Serial.print(data[1]);
    Serial.print(" Intensity: ");
    Serial.println(data[2]);
    #endif
    
    create_link.write(LEDSOP);
    create_link.write(&data[0], LEDS_DATA_SIZE);
}

/*
    This command stores a user made song in the create's memory
    so that it can be recalled and played at a later time. 
 */
void song(char* data)
{
    #ifdef DEBUG
    char index;
    Serial.print("Song will be stored as song number: ");
    Serial.println(data[0]);
    Serial.print("Number of notes: ");
    Serial.println(data[1]);
    Serial.print("List of notes: ");

    for(index = 0; index < data[1]; index++)
    {
        Serial.print(data[2+index], HEX);
        Serial.print(" ");
    }
    Serial.println();
    #endif 

    create_link.write(SONGOP);
    create_link.write(&data[0], SONG_DATA_SIZE);
}

/*
    Plays the requested song from the create's stored
    bank of songs.
 */
void play_song(char number)
{
    #ifdef DEBUG
    if(number <= 15 && number >= 0)
    {
        Serial.print("Selected song number: ");
        Serial.println(number);
    }
    else
        Serial.println("Invalid song number. Choose 0-15");
    #endif

    create_link.write(PLAYSONGOP);
    create_link.write(number);
}

void query_sensor(char* data)
{
    char index;
    char sesnor_data[50];
    char rcv_bytes = 0;
    
    #ifdef DEBUG
    Serial.print("Number of packets: ");
    Serial.println(data[0]);
    Serial.print("Packet IDs: ");
    #endif
    
    for(index = 0; index < data[0]; index++)
    {
        #ifdef DEBUG
        Serial.print(data[1 + index]);
        Serial.print(" ");
        #endif
        switch(data[1 + index])
        {
            case BUMPERID:
                rcv_bytes += 1;
                break;
            case WALLID:
                rcv_bytes += 1;
                break;
            case LCLIFFID:
                rcv_bytes += 1;
                break;
            case FLCLIFFID:
                rcv_bytes += 1;
                break;
            case FRCLIFFID:
                rcv_bytes += 1;
                break;
            case RCLIFFID:
                rcv_bytes += 1;
                break;
            case VWALLID:
                rcv_bytes += 1;
                break;
            case OVERCURRENTID:
                rcv_bytes += 1;
                break;
            case IRSENSID:
                rcv_bytes += 1;
                break;
            case BUTTONSID:
                rcv_bytes += 1;
                break;
            case DISTANCEID:
                rcv_bytes += 2;
                break;
            case ANGLEID:
                rcv_bytes += 2;
                break;
            case BATTEMPID:
                rcv_bytes += 1;
                break;
            case BATVOLTSID:
                rcv_bytes += 2;
                break;
            case BATCHARGEID:
                rcv_bytes += 2;
                break;
            case BATCAPID:
                rcv_bytes += 2;
                break;
            case BATCURRENTID:
                rcv_bytes += 2;
                break;
            case WALLSIGID:
                rcv_bytes += 2;
                break;
            case LCLIFFSIGID:
                rcv_bytes += 2;
                break;
            case FLCLIFFISIGID:
                rcv_bytes += 2;
                break;
            case FRCLIFFSIGID:
                rcv_bytes += 2;
                break;
            case RCLIFFSIGID:
                rcv_bytes += 2;
                break;
            case CHARGESRCID:
                rcv_bytes += 1;
                break;
            case VELREQUESTID:
                rcv_bytes += 2;
                break;
            case RADREQUESTID:
                rcv_bytes += 2;
                break;
            case RVELREQUESTID:
                rcv_bytes += 2;
                break;
            case LVELREQUESTID:
                rcv_bytes += 2;
                break;
            #ifdef DEBUG
            default:
                Serial.print("Encountered unknown sensor ID: ");
                Serial.println(data[1 + index);
            #endif
        }
    }
    
    #ifdef DEBUG
    Serial.println();
    Serial.println("Data received: ")
    #endif
    
    create_link.write(QUERYOP);
    create_link.write(data[0]);
    
    for(index = 0; index < data[0]; index++)
    {
        create_link.write(data[1 + index]);
    }
    
    #ifdef DEGBUG
    create_link.readBytes(sensor_data, data[0]);
    else
    
    #endif
}

/*
  This command causes Create to wait for the specified time.
  During this time, Create’s state does not change, nor does
  it react to any inputs, serial or otherwise.
*/
void wait_time(char data)
{
  #ifdef DEBUG
  Serial.print("ARCBOT will wait for: ");
  Serial.println(data);
  #endif
  create_link.write(WAITTIMEOP);
  create_link.write(data);
}


/*
    This command causes iRobot Create to wait until it has
    traveled the specified distance in mm. When Create travels
    forward, the distance is incremented. When Create travels
    backward, the distance is decremented. If the wheels
    are passively rotated in either direction, the distance is
    incremented. Until Create travels the specified distance,
    its state does not change, nor does it react to any inputs,
    serial or otherwise.
*/
void wait_distance(char* data)
{
  #ifdef DEBUG
  Serial.println("ARCBOT is waiting to travel a certain distance");
  #endif

  create_link.write(WAITDISTOP);
  create_link.write(data,WAIT_DISTANCE_DATA_SIZE);
}

/*
    This command causes Create to wait until it has rotated
    through specified angle in degrees. When Create turns
    counterclockwise, the angle is incremented. When Create
    turns clockwise, the angle is decremented. Until Create
    turns through the specified angle, its state does not change,
    nor does it react to any inputs, serial or otherwise.
*/
void wait_angle(char* data)
{
  #ifdef DEBUG
  Serial.println("ARCBOT is waiting to rotate a certain angle");
  #endif

  create_link.write(WAITANGLOP);
  create_link.write(data, WAIT_ANGLE_DATA_SIZE);
}

/*
    This command causes Create to wait until it detects the
    specified event. Until the specified event is detected,
    Create’s state does not change, nor does it react to any
    inputs, serial or otherwise.
*/
void wait_event(char data)
{
  #ifdef DEBUG
  Serial.println("ARCBOT is waiting for a specific event to happen");
  #endif

  create_link.write(WAITEVENTOP);
  create_link.write(data);
}
