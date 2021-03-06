/* Sweep
2019/8/5 from seeep example
pwm  3,5,6,9,10,11

2019/8/5: servo use 3,5,6,9
by CNHsu
*/

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
Servo myservo3,myservo5,myservo6;
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
int dt =50; // default dt
void setup() {
  //myservo.attach(9);  // attaches the servo on pin 9 to the servo object
 myservo.attach(9,544,2400); // calibrate
 myservo.write(90); // default degree
 myservo3.attach(3,544,2400); // calibrate
 myservo3.write(90); // default degree
 myservo5.attach(5,544,2400); // calibrate
 myservo5.write(90); // default degree
 myservo6.attach(6,544,2400); // calibrate
 myservo6.write(150); // default degree
  Serial.begin(38400);
  Serial.println("Hello Servo (m1,m2,m3,m4):");
  Serial.println("example m175: servo1 75degree");
  Serial.println("m1=0-180, m2=40-180, m3=140-180, m4=150-45");
  dt=50;
}

void loop() {
  int i,k;
  int state;
  char ch,mode;
  String instr="";
  String binstr="";

instr="";  
while(!Serial.available()) {}  
 instr=Serial.readString();
 binstr="";
 mode=' ';
if (instr[0]=='m') { // m1=servo3,,m2=servo5,m3=servo=6,m4=servo9
  binstr=instr.substring(2);
  ch=instr[1];
}
else if (instr[0]=='r') {
  mode='r';
  binstr=instr.substring(2);
  ch=instr[1]; 
}
else if (instr[0]=='d') {
  mode='r';
  binstr=instr.substring(1);
  ch='d';
  dt=binstr.toInt();
}
else
{
  binstr=instr;
  ch='1'; // default servo3
}
 state=binstr.toInt();
 if (instr[0]=='d' || (state >=0 && state <=180))
  {
    if(mode !='r'){
    Serial.write("servo option:");
    Serial.write(ch);
    Serial.write("=");
    Serial.println(state);
    }
    switch(ch)
    {
      case 'a':
               Serial.write("auto demo run");
               servoto ('1',90);
               servoto('2',150);
               servoto('4',150);
               delay(100);
               servoto('3',140);
               servoto('3',170);
               servoto('4',45);
               servoto('1',170);
               servoto('2',150);
               servoto('4',150);
               delay(100);
               servoto('3',140);
               delay(100);
               servoto('2',150);
               servoto('4',45);
               servoto('1',90);
               break;  
      case 'c':
               Serial.write("auto demo run");
               servoto ('1',90);
               servoto('2',150);
               servoto('4',150); // down
               delay(100);
               servoto('3',140); // open
               servoto('3',170); // close
               servoto('4',45);
               servoto('1',170); // move to 
               servoto('2',150);
               servoto('4',150); // down
               //
               servoto('4',45); // back
               servoto('1',20);
               servoto('2',150);
               servoto('4',150);
               servoto('3',140); // open
               delay(100);
               servoto('2',150);
               servoto('4',45); // back
               servoto('1',90); // move to 
               delay(100);
               servoto('1',20); // move to
               servoto('2',150);
               servoto('4',150);
               servoto('3',170); // close
               servoto('4',45);
               servoto('1',90); 
               servoto('4',150);
               delay(100);
               servoto('3',140);
               delay(100);
               servoto('2',150);
               servoto('4',45);
               servoto('1',90);
               break;              
      case'd' :
               Serial.write("delay time:");
               Serial.println(dt);
               break;
      case'5' : //base
                  servoto('1',170);
                  servoto('1',10);
                  servoto('1',90);
 
               break;   
       case'6' : //arm
                  servoto('4',90);
                  servoto('2',170);
                  servoto('2',150);                 

               break; 
       case'7' : //arm
                  servoto('3',175);
                  servoto('3',140);
                  servoto('3',160);

               break;    
       case'8' : //arm
                  servoto('2',150); // set 2 to 150
                  servoto('4',150);
                  servoto('4',45);
                  /*
                  state=150;
                  i=myservo.read();
                  for (i=i+1; i<=state; i++){
                    myservo.write(i);
                    delay(dt);
                   }
                   state=45;
                   i=150;
                    for (i=i-1; i>=state; i--){
                     myservo.write(i);
                     delay(dt);
                    }
*/
               break;
                                                                
      case'1' : //base
                
                if(mode =='r'){
                i=myservo3.read();
                Serial.write("servo read1-3=:");
                Serial.println(i);
                delay(dt);
                }
                else {
                i=myservo3.read();
                if (state == i) {}
                else if(state >i)
                  {
                  for (i=i+1; i<=state; i++){
                    myservo3.write(i);
                    delay(dt);
                   }
                  }
                  else {
                    for (i=i-1; i>=state; i--){
                     myservo3.write(i);
                     delay(dt);
                    }
                //myservo3.write(0); // back to default 90degree                
                  }
                }
               break;
      case'2' : //left1
                if (state <60) state=60;
                if(mode =='r'){
                i=myservo5.read();
                Serial.write("servo read2-5=:");
                Serial.println(i);
                delay(dt);
                }
                else {           
                i=myservo5.read();
                if (state == i) {}
                else if(state >i)
                  {
                  for (i=i+1; i<=state; i++){
                    myservo5.write(i);
                    delay(dt);
                   }
                  }
                  else {
                    for (i=i-1; i>=state; i--){
                     myservo5.write(i);
                     delay(dt);
                    }
                //myservo3.write(0); // back to default 90degree                
                  }
                }
               // myservo5.write(0); // back to default 90degree                
               break;
      case'3' : //arm
                if (state < 140) state=140;
                
                if(mode =='r'){
                i=myservo6.read();
                Serial.write("servo read3-6=:");
                Serial.println(i);
                delay(dt);
                } 
                else {               
                i=myservo6.read();
                if (state == i) {}
                else if(state >i)
                  {
                  for (i=i+1; i<=state; i++){
                    myservo6.write(i);
                    delay(dt);
                   }
                  }
                  else {
                    for (i=i-1; i>=state; i--){
                     myservo6.write(i);
                     delay(dt);
                    }
                //myservo3.write(0); // back to default 90degree                
                  }            
                }
               break;
      case'4' : //right
                if(state > 150) state =150;
                else if(state < 45) state=45;
                
                if(mode =='r'){
                i=myservo.read();
                Serial.write("servo read4-9=:");
                Serial.println(i);
                delay(dt);
                }
                else{                
                i=myservo.read();
                if (state == i) {}
                else if(state >i)
                  {
                  for (i=i+1; i<=state; i++){
                    myservo.write(i);
                    delay(dt);
                   }
                  }
                  else {
                    for (i=i-1; i>=state; i--){
                     myservo.write(i);
                     delay(dt);
                    }
                //myservo3.write(0); // back to default 90degree                
                  }
                }
               break;      
    }
    
  } 
/* test code  
    Serial.write("servo option:");
    Serial.println(binstr);
    myservo.write(state);
    delay(200);
     myservo.write(90); // return to original

     myservo3.write(state);
     delay(200);
     myservo3.write(90); // return to original

     myservo5.write(state);
     delay(200);
     myservo5.write(90); // return to original

     myservo6.write(state);
     delay(200);
     myservo6.write(90); // return to original
 */ 

/*
  
  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  */
}

int servoto(char ch,int deg)
{
  int i;
  int state;
  state=deg;
  Serial.write("servo to:");
  Serial.println(state);
  Serial.println(ch);
  Serial.write("delay : ");
  Serial.println(dt);
  switch(ch){
        case'1' : //base
                Serial.write("servo 1");
                i=myservo3.read();
                if (state == i) {}
                else if(state >i)
                  {
                  for (i=i+1; i<=state; i++){
                    myservo3.write(i);
                    delay(dt);
                   }
                  }
                  else {
                    for (i=i-1; i>=state; i--){
                     myservo3.write(i);
                     delay(dt);
                    }
                //myservo3.write(0); // back to default 90degree                
                  }
                
               break;
      case'2' : //left1
                if (state <60) state=60;
                Serial.write("servo 2");    
                i=myservo5.read();
                if (state == i) {}
                else if(state >i)
                  {
                  for (i=i+1; i<=state; i++){
                    myservo5.write(i);
                    delay(dt);
                   }
                  }
                  else {
                    for (i=i-1; i>=state; i--){
                     myservo5.write(i);
                     delay(dt);
                    }
                //myservo3.write(0); // back to default 90degree                
                  }
                
               // myservo5.write(0); // back to default 90degree                
               break;
      case'3' : //arm
                if (state < 140) state=140;
                Serial.write("servo 3");                           
                i=myservo6.read();
                if (state == i) {}
                else if(state >i)
                  {
                  for (i=i+1; i<=state; i++){
                    myservo6.write(i);
                    delay(dt);
                   }
                  }
                  else {
                    for (i=i-1; i>=state; i--){
                     myservo6.write(i);
                     delay(dt);
                    }
                //myservo3.write(0); // back to default 90degree                
                  }            
                
               break;
      case'4' : //right
                if(state > 150) state =150;
                else if(state < 45) state=45;
                Serial.write("servo 4");                                
                i=myservo.read();
                if (state == i) {}
                else if(state >i)
                  {
                  for (i=i+1; i<=state; i++){
                    myservo.write(i);
                    delay(dt);
                   }
                  }
                  else {
                    for (i=i-1; i>=state; i--){
                     myservo.write(i);
                     delay(dt);
                    }
                //myservo3.write(0); // back to default 90degree                
                  }
                
               break;
  }
}
