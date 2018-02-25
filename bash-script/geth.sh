
#!/usr/bin/expect
exec solcjs --abi test.sol
exec solcjs --bin test.sol
set abi [exec more test_sol_startup.abi]
set bin [exec more test_sol_startup.bin]
spawn /usr/bin/geth attach
expect ">"
send "eth.accounts\r"
expect ">"
send "personal.unlockAccount(eth.coinbase)\r"
send "gLhT2018gLhT\r"
expect ">"
send "var getstartup = eth.contract($abi)\r"
expect ">"
send "var bytecode = '0x$bin'\r"
expect ">"
send "var deploy = {from:eth.coinbase, data:bytecode, gas: 2000000}\r"
expect ">"
send "var getstartupPartialInstance = getstartup.new(deploy)\r"
expect ">"
interact
send "getstartupPartialInstance.address\r"
send "exit\r"
expect eof
