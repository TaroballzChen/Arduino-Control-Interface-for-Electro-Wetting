for (i = 15; i < 87; i++) {
	open("/Volumes/MacStorage/FJUgoogledrive/pythonwork/Arduino-Control-Interface-for-Electro-Wetting/tools/data2/water_mix/water_mix10/image"+i+".jpg");
	makeLine(115, 235, 149, 303);
//	makeOval(51, 199, 150, 150);ww
	waitForUser("123");
	run("Color Profiler");
	selectWindow("Plot of image"+i);
//	run("Color Histogram");
//	waitForUser("123");
	run("AutoClickerJ GUI 1.0.7", "order=LeftClick x_point=602 y_point=691 delay=100 clickandkeywrite=[]");
	wait(500);
	saveAs("Text", "/Users/chenyuanyu/Desktop/water_mix_new/"+i+".csv");
//	saveAs("Text", "/Users/chenyuanyu/Desktop//mixing_str/"+i+".csv");
	selectWindow("Plot of image"+i);
	close();
	selectWindow("image"+i+".jpg");
	close();
}