ip=$(ip route get 8.8.8.8 | awk '/8.8.8.8/ {print $NF}')

echo $ip

curl -v "http://abf149.scripts.mit.edu/oxidedns/demo.py?s="$ip


