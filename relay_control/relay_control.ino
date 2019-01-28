#define CH595 48
//#define ELECTRODE 12

String command = "";
const int latch = 2;
const int clock_pin = 3;
const int data_pin = 4;
const int output[] = {latch,clock_pin,data_pin};
int len = sizeof(output)/sizeof(output[0]);
bool *operate_array = NULL;
bool *p =NULL;

void setup() {
  Serial.begin(9600);
  Serial.println("Ready");
  pinmode_init(output);
}

void pinmode_init(const int pinList[]){
  for(int i=0;i<len;i++){
    pinMode(pinList[i],OUTPUT);
    digitalWrite(pinList[i],LOW);
  }
}
  

void loop() {
  python_command();
  channel_select(command);
  command = '@';
}

void python_command() {
  if (Serial.available()){
  command="";
  delay(1);

  while(Serial.available()){
    command+=(char)Serial.read();
    }
  Serial.println(command);
  }

}

void pin_operate2(int control_Num){
  for(int i=0;i<control_Num;i++){
    digitalWrite(latch,LOW);
    for (int j=CH595;j>0;j--){
        p = operate_array +i*CH595 +j-1;
        input_data(*p);
      }
      digitalWrite(latch,HIGH);
      delay(500);
    }
}

void input_data(bool High_or_Low){
  digitalWrite(clock_pin,LOW);
  digitalWrite(data_pin,High_or_Low);
  digitalWrite(clock_pin,HIGH);
  }


