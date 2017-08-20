/* Opcodes for the various create commands */
#define     STARTOP         128
#define     SAFEOP          131
#define     FULLOP          132
#define     DEMOOP          136
#define     DRIVEOP         137
#define     DRIVEDOP        145
#define     LEDSOP          139
#define     SONGOP          140
#define     PLAYSONGOP      141
#define     QUERYOP         149
#define     WAITTIMEOP      155
#define     WAITDISTOP      156
#define     WAITANGLOP      157
#define     WAITEVENTOP     158

/* Demo selection values */
#define     DEMO_ABORT      255
#define     DEMO_COVER      0
#define     DEMO_DOCK       1
#define     DEMO_SPOT       2
#define     DEMO_MOUSE      3
#define     DEMO_FIG8       4
#define     DEMO_WIMP       5
#define     DEMO_HOME       6
#define     DEMO_TAG        7
#define     DEMO_PACH       8
#define     DEMO_BANJO      9

/* Event numbers for wait_event() */
#define     WHEEL_DROP      1
#define     FWHEEL_DROP     2
#define     LWHEEL_DROP     3
#define     RWHEEL_DROP     4
#define     BUMP            5
#define     LBUMP           6
#define     RBUMP           7
#define     VIRUAL_WALL     8
#define     WALL            9
#define     CLIFF           10
#define     LCLIFF          11
#define     FLCLIFF         12
#define     FRCLIFF         13
#define     RCLIFF          14
#define     HOME_BASE       15
#define     ADV_BUTTON      16
#define     PLAY_BUTTON     17
#define     PASSIVE         22

/* Sensor IDs */
#define     BUMPERID        7
#define     WALLID          8
#define     LCLIFFID        9
#define     FLCLIFFID       10
#define     FRCLIFFID       11
#define     RCLIFFID        12
#define     VWALLID         13
#define     OVERCURRENTID   14
#define     IRSENSID        17
#define     BUTTONSID       18
#define     DISTANCEID      19
#define     ANGLEID         20
#define     BATTEMPID       24
#define     BATVOLTSID      22
#define     BATCHARGEID     25
#define     BATCAPID        26
#define     BATCURRENTID    23
#define     WALLSIGID       27
#define     LCLIFFSIGID     28
#define     FLCLIFFISIGID   29
#define     FRCLIFFSIGID    30
#define     RCLIFFSIGID     31
#define     CHARGESRCID     34
#define     VELREQUESTID    39
#define     RADREQUESTID    40
#define     RVELREQUESTID   41
#define     LVELREQUESTID   42

/*  Arduino Commands */
const char     DRIVE           =    'D';
const char     DRIVE_DIRECT    =    'r';
const char     WHEELLEFT       =    'L';
const char     WHEELRIGHT      =    'R';
const char     MODESAFE        =    'S';
const char     MODEFULL        =    'F';
const char     WHEELSTOP       =    's';
const char     USEDEMO         =    'd';
const char     TERMINATOR      =    '\r';
