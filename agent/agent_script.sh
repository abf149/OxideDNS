while :
do
ip=$(ip route get 8.8.8.8 | awk '/8.8.8.8/ {print $NF}')

curl -s "http://abf149.scripts.mit.edu/server.py?s="$ip

if [ $? -eq 0 ]; then
    echo OK
    sleep 1m    
else
    echo FAIL
    sleep 10s    
fi


done
