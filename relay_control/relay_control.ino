#define CH595 16
#define ELECTRODE 12

String command = "";
const int latch = 2;
const int clock_pin = 3;
const int data_pin = 4;
const int output[] = {latch,clock_pin,data_pin};
int len = sizeof(output)/sizeof(output[0]);
int *operate_array = NULL;
int *p =NULL;

int * Channel_1_step2(){
  static int channel[] = {
  1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
  0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,
  0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,
  0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,
  0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,
  0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,
  0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,
  0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,
  0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,
  0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,
};
  return channel;
}

int * Channel_1_step1(){
  static int channel1[] = {
  1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
  0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,
  0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,
  0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,
  0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,
  0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,
  0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,
  0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,
  0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,
  0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,
  0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,
  0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,
};
  return channel1;
}

int * Pause(){
  static int p[]={
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    };
    return p;
  }

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

void channel_select(String str){
  switch (str[0]){
    case 'a':
      operate_array = Channel_1_step1();
      pin_operate2(ELECTRODE);
      operate_array = Channel_1_step2();
      pin_operate2(ELECTRODE);
      break;
    
    case 'b':
      operate_array = NULL;
      pin_operate2(0);
      break;
      
    case '@':
      operate_array = Pause();
      pin_operate2(1);
      break;
    
    default:
      command="";
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

void input_data(int High_or_Low){
  digitalWrite(clock_pin,LOW);
  digitalWrite(data_pin,High_or_Low);
  digitalWrite(clock_pin,HIGH);
  }


