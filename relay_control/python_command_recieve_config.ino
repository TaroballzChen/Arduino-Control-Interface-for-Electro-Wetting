void channel_select(String str){
  switch (str[0]){
    case 'a':
      pin_operate(a,arrayLength(a));
      break;
    
    case 'b':
      pin_operate(b,arrayLength(b));
      break;

    case 'c':
      break;
          
    case '@':
      pin_operate(Pause,arrayLength(Pause));
      break;
    
    default:
      command="";
    }
    
}
