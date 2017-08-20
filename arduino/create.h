#include <SoftwareSerial.h>
#include "encodings.h"

#define     DRIVE_DATA_SIZE             4
#define     DRIVE_DIRECT_DATA_SIZE      4
#define     LEDS_DATA_SIZE              3
#define     SONG_DATA_SIZE              63
#define     QUERY_DATA_SIZE             63
#define     WAIT_DISTANCE_DATA_SIZE     2
#define     WAIT_ANGLE_DATA_SIZE        2
#define     TX                          2
#define     RX                          3
#define     BAUD                        57600
#define     DEBUG

void create_init();
void oi_safe();
void oi_full();
void demo(char data);
void drive(char* data);
void drive_direct(char* data);
void leds(char* data);
void song(char length, char number, char* notes);
void play_song(char number);
void query_sensor(char length, char* ids);
void wait_time(char data);
void wait_distance(char* data);
void wait_angle(char* data);
void wait_event(char data);
int angle();
char battery_temp();
unsigned int battery_volts();
