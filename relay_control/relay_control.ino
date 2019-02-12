#define CH595 48
#define arrayLength(arr) (sizeof((arr))/sizeof((arr)[0]))

String command = "";
const int latch = 2;
const int clock_pin = 3;
const int data_pin = 4;
const int output[] = {latch,clock_pin,data_pin};
int len = arrayLength(output);

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

void pin_operate(const byte control_array[][CH595],int len){
  for(int i=0;i<len;i++){
    digitalWrite(latch,LOW);
    for (int j=CH595-1;j>=0;j--){
      byte data = pgm_read_word_near(control_array[i]+j);
      input_data(data);
      }
      digitalWrite(latch,HIGH);
      delay(500);
    }
    
}

void input_data(byte High_or_Low){
  digitalWrite(clock_pin,LOW);
  digitalWrite(data_pin,High_or_Low);
  digitalWrite(clock_pin,HIGH);
  }


