String command = "";
#define LEN 3
const int output[] = {8,11,12};
const int output2[] = {7,8,9};
int len = sizeof(output)/sizeof(output[0]);
const int operate[LEN][LEN] = {
  {1,0,0},
  {0,1,0},
  {0,0,1}
  };

const int collect[LEN][LEN] = {
  {0,1,0},
  {1,0,1},
  {1,1,1}
};

const int pause[LEN][LEN] = {{0,0,0},{0,0,0},{0,0,0}};


void setup() {
  Serial.begin(9600);
  Serial.println("Ready");
  pinmode_init(output);
}

void pinmode_init(const int pinList[]){
  for(int i=0;i<len;i++){
    pinMode(i,OUTPUT);
    digitalWrite(i,LOW);
  }
}
  

void loop() {
  python_command();
  
  channel_select(command);

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
      pin_operate(operate,output);
      break;
    
    case 'b':
      pin_operate(collect,output);
      break;
      
    case '@':
      pin_operate(pause,output);
      break;
    
    default:
      command="";
    }
    
}

void pin_operate(const int operation[LEN][LEN],const int pin[LEN]){
  for (int i=0;i<len;i++) {
    for(int j=0;j<len;j++){
      digitalWrite(pin[j],operation[i][j]);
      }
      delay(500);
    }
}




