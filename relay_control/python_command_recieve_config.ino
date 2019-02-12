void channel_select(String str){
  switch (str[0]){
    case 'a':
      pin_operate(a,arrayLength(a));
      break;
    
    case 'b':
      operate_array = Channel_2_step2();
      pin_operate2(1);
      break;

    case 'c':
      operate_array = Channel_2_step3();
      pin_operate2(2);
      break;
          
    case '@':
      pin_operate(Pause,arrayLength(Pause));
      break;
    
    default:
      command="";
    }
    
}
