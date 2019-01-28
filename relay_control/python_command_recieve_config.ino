void channel_select(String str){
  switch (str[0]){
    case 'a':
      operate_array = Channel_2_step1();
      pin_operate2(4);
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
      operate_array = Pause();
      pin_operate2(1);
      break;
    
    default:
      command="";
    }
    
}
