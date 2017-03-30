#/bin/sh
echo "--Henglv adb keytool--"
echo "m:Menu,h:Home,b:Back,e:Enter, c:Call,"
echo "w:Up, l:Left, d:Right, s:Down,"
echo "x:Exit" 
#echo "->"
while true
do
echo -e ">\c"
read -n 1 key
echo ""
case $key in
[Hh]) 
adb shell input keyevent 3;;
[Bb]) 
adb shell input keyevent 4;;
[Mm]) 
adb shell input keyevent 82;;
[Ee]) 
adb shell input keyevent 23;;

[Cc]) 
adb shell input keyevent 5;;

[Ww]) 
adb shell input keyevent 19;;
[Dd]) 
adb shell input keyevent 22;;
[Ss]) 
adb shell input keyevent 20;;
[Aa]) 
adb shell input keyevent 21;;

[Cc]) 
adb shell input keyevent 5;;

[Xx])
exit;;
esac

done





