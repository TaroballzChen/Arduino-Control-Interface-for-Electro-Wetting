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
