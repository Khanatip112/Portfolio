#include "MPU6050_6Axis_MotionApps20.h"
#include "Wire.h"
#include <ESP8266WiFi.h>
#include <TridentTD_LineNotify.h>
MPU6050 mpu;
int16_t ax, ay, az;
int16_t gx, gy, gz;
int valx , valy , valz;
int val1 , val2 ;
int valgy1 = 0 , valgy2 = 0;
int buzzer = D3;
int isNotify = 0;
int timer = 0;

int Switch1 = D5;

char ssid[] = "S21plus";
char pass[] = "Khanatip";
#define LINE_TOKEN "GO8hRTHn1zej5NjaNcnutEKbTXqNMe1z03g2AiD9CDq"

void setup()
{
  Wire.begin();
  Serial.begin(115200);
  Serial.println("Initialize MPU");
  mpu.initialize();
  Serial.println(mpu.testConnection() ? "Connected" : "Connection failed");
  pinMode(buzzer, OUTPUT);
  pinMode(Switch1,INPUT_PULLUP);
  WiFi.begin (ssid, pass);
  LINE.setToken(LINE_TOKEN);
  }

void loop()
{
  int Switch1State = digitalRead(Switch1);
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
  valx = map(ax, -17000, 17000, 0, 179);
  valy = map(ay, -17000, 17000, 0, 179);
  valz = map(az, -17000, 17000, 0, 179);
  Serial.print("axis x = ") ;
  Serial.print(valx) ;
  Serial.print(" axis y = ") ;
  Serial.print(valy) ;
  Serial.print(" axis z = ") ;
  Serial.println(valz) ;

  if(Switch1State == LOW){
   Serial.println("I need help!!!!") ;
   LINE.notify("I need help!!!!");
   LINE.notifyPicture("https://png.pngtree.com/png-vector/20220518/ourmid/pngtree-woman-needs-help-stress-psychologist-png-image_4673847.png");
   tone (buzzer,300);
   delay(500);
   tone (buzzer,700);
   delay(500);
   tone (buzzer,300);
   delay(500);
   tone (buzzer,700);
   delay(500);
   tone (buzzer,300);
   delay(500);
   tone (buzzer,700);
   delay(500);
   tone (buzzer,300);
   delay(500);
   tone (buzzer,700);
   delay(500);
   tone (buzzer,300);
   delay(500);
   tone (buzzer,700);
   delay(500);
   tone (buzzer,300);
   delay(500);
   tone (buzzer,700);
   delay(500);
  } 
  else
  noTone (buzzer);
  {
  }

  if ((( valx >=87)&&(valx <=98))&&(( valy >=1)&&(valy <=25))) {
    Serial.println("ล้มหลังงงงง") ;
    
    tone (buzzer,300);
    delay(500);
    tone (buzzer,700);
    delay(500);
    if (timer%20==0){LINE.notify("Smart Crutch have fallen, please check!!!"),LINE.notifyPicture("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRct22fCaEnBSLKu2oLKuF1gFB2VYFKJjQZZk_DF0cd_rFTA__W3jx3OK301nZhKnv3Ac4&usqp=CAU"); isNotify=1;timer++;}
    else{timer++;}
       
  }
  if ((( valx >=95)&&(valx <=107))&&(( valy >=150)&&(valy <=180))) {
    Serial.println("ล้มหน้าาาา") ;
     
    tone (buzzer,300);
    delay(500);
    tone (buzzer,700);
    delay(500);
    if (timer%20==0){LINE.notify("Smart Crutch have fallen, please check!!!"),LINE.notifyPicture("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRct22fCaEnBSLKu2oLKuF1gFB2VYFKJjQZZk_DF0cd_rFTA__W3jx3OK301nZhKnv3Ac4&usqp=CAU"); isNotify=1;timer++;}
    else{timer++;}
      
  }
  
  if ((( valx >=25)&&(valx <=40))&&(( valy >=120)&&(valy <=145))) {
    Serial.println("ล้มซ้าย") ;
    
    tone (buzzer,300);
    delay(500);
    tone (buzzer,700);
    delay(500);
    if (timer%20==0){LINE.notify("Smart Crutch have fallen, please check!!!"),LINE.notifyPicture("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRct22fCaEnBSLKu2oLKuF1gFB2VYFKJjQZZk_DF0cd_rFTA__W3jx3OK301nZhKnv3Ac4&usqp=CAU"); isNotify=1;timer++;}
    else{timer++;}
       
  }

 if ((( valx >=140)&&(valx <=168))&&(( valy >=120)&&(valy <=145))) {
    Serial.println("ล้มขวา") ;
    
    tone (buzzer,300);
    delay(500);
    tone (buzzer,700);
    delay(500);
    if (timer%20==0){LINE.notify("Smart Crutch have fallen, please check!!!"),LINE.notifyPicture("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRct22fCaEnBSLKu2oLKuF1gFB2VYFKJjQZZk_DF0cd_rFTA__W3jx3OK301nZhKnv3Ac4&usqp=CAU"); isNotify=1;timer++;}
    else{timer++;}
       
  }

 else if ((( valx >=70)&&(valx <=120))&&(( valy >=70)&&(valy <=120)))  {
    noTone (buzzer);
    if (isNotify ==1)
    {LINE.notify("Smart Crutch is in normal state."),LINE.notifyPicture("https://png.pngtree.com/png-clipart/20220130/original/pngtree-hand-drawn-cartoon-to-help-the-old-man-cross-the-road-png-image_7243520.png"),Serial.println("ไม้เท้าอยู่ในสถานะปกติ") ; isNotify=0;timer=0;}
  } 

  delay(500);
}
