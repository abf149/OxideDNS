while :
do
ip=$(ip route get 8.8.8.8 | awk '/8.8.8.8/ {print $NF}')

curl -v "http://abf149.scripts.mit.edu/oxidedns/demo.py?s="$ip

sleep 1m
done
