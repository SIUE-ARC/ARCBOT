#include "encodings.h"
#include <arduino.h>
#include <Servo.h>

#define     ULTRASOUND0_PIN     4
#define     ULTRASOUND0_PIN     7
#define     ULTRASOUND0_PIN     8
#define     ULTRASOUND0_PIN     12
#define     IR0_PIN             A0
#define     IR1_PIN             A1
#define     IR2_PIN             A2
#define     SERV0_PIN           9
#define     SERV1_PIN           10

#define     SERVO_DATA_SIZE     3
#define     USONIC_DATA_SIZE    1
#define     IR_DATA_SIZE        1

void init_hardware();
void servo(char* data);
void ir_sensor(char data);
void ultrasonic(char data);
