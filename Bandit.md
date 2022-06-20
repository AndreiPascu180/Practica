to connect to level0: ssh bandit0@bandit.labs.overthewire.org -p 2220 cu parola bandit0
level0: cat readme -> pass for lvl 2 : boJ9jbbUNNfktd78OOpsqOltutMc3MY1
level1: cat ./- -> pass: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
level2: cat "spaces in this filename" -> pass: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
level3: cd inhere -> ls -al -> cat .hidden -> pass: pIwrPrtPN36QITSp3EQaw936yaFoFgAB
level4: cd inhere -> ls -al -> file ./-* -> -file07 ascii text -> cat ./-file07 -> pass koReBOKuIDDepwhWk7jZC0RTdopnAYKh
level5: cd inhere -> find -size 1033c -type f -> ./maybehere07/.file2 -> cat ./maybehere07/.file2 -> pass: DXjZPULLxYr17uwoI01bNLQbtFemEgo7
level6: find / -user bandit7 -group bandit6 -size 33c 2>/dev/null -> cat /var/lib/dpkg/info/bandit7.password -> pass: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
level7: cat data.txt | grep "millionth" -> millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV
level8: cat data.txt | sort | uniq -u -> pass: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
level9: strings data.txt | grep "=" -> ========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
level10: cat data.txt | base64 --decode -> The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
level11: cat data.txt |  tr '[A-Za-z]' '[N-ZA-Mn-za-m]' -> The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
level12: zcat data | bzcat | zcat | tar -x | tar -x | bzcat | tar -x | zcat  -> The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
level13: ssh -i sshkey.private  bandit14@localhost -p 2220 -> cat /etc/bandit_pass/bandit14 -> pass: 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
level14: nc localhost 30000 -> entered: 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e -> output: Correct! BfMYroe26WYalil77FoDi9qh59eK5xNr
level15:
level16:
level17:
level18:

