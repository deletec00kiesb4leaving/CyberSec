for i in $(seq 254);
 do
   ping 192.168.1.${i} -c1 -W1 &
done | grep from

