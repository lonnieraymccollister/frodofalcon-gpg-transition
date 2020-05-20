@ECHO OFF
REM.-- Prepare the Command Processor
SETLOCAL ENABLEEXTENSIONS
SETLOCAL ENABLEDELAYEDEXPANSION
echo.%1
set one=%1
echo.%2
set two=%2
echo.%3
set three=%3
:menuLOOP
echo.
echo.= Menu =================================================
echo.
for /f "tokens=1,2,* delims=_ " %%A in ('"findstr /b /c:":menu_" "%~f0""') do echo.  %%B  %%C
set choice=
echo.&set /p choice=Make a choice or hit ENTER to quit: ||GOTO:EOF
echo.&call:menu_%choice%
GOTO:menuLOOP

::-----------------------------------------------------------
:: menu for gpg drop in Frodo keysfrodo(**directory is here**)
::-----------------------------------------------------------

:menu_1   encrypt *** cmd syntax --- pyemail.bat key_name_receiver filename key_name_sender
echo *** copy and enter key from cmd prompt
del "pk.txt"
del "sk.txt"
copy "keysfrodo\pk%one%.txt" "pk.txt"
copy "keysfrodo\pk%one%.txt" "sk.txt"
python enc.py
gpg --symmetric --cipher-algo AES256 "%two%"
pause
del "pk.txt"
del "sk.txt"
copy "keysfalcon\pk%three%.txt" "pk.txt"
copy "keysfalcon\sk%three%.txt" "sk.txt"
python SignFile.py "%two%" "%two%.sig"
pause
copy "ct.txt" "Message\ct.txt"  
copy "%two%.gpg" "Message\%two%.gpg" 
copy "%two%.sig" "Message\%two%.sig"
del "ct.txt"
del "%two%"
del "%two%.gpg"
del "%two%.sig"
cls
GOTO:EOF

:menu_2   decrypt *** cmd syntax --- pyemail.bat key_name_receiver filename key_name_sender
echo *** copy and enter key from cmd prompt
del "pk.txt"
del "sk.txt"
copy "keysfrodo\pk%one%.txt" "pk.txt"
copy "keysfrodo\sk%one%.txt" "sk.txt"
python dec.py
gpg -o "%two%" -d "%two%.gpg"
pause
del "pk.txt"
del "sk.txt"
copy "keysfalcon\pk%three%.txt" "pk.txt"
copy "keysfalcon\pk%three%.txt" "sk.txt"
python VerifyFile.py "%two%" "%two%.sig" 
pause
copy "ct.txt" "Message\ct.txt" 
copy "%two%" "Message\%two%" 
copy "%two%.gpg" "Message\%two%.gpg"
copy "%two%.sig" "Message\%two%.sig"
del "ct.txt"
del "%two%"
del "%two%.gpg"
del "%two%.sig"
cls
GOTO:EOF

:menu_3   Delete all files in message directory
del "MESSAGE\*.*"
cls
GOTO:EOF

:menu_4   Generate keysfrodo *** cmd syntax --- pyemail.bat keyname
echo *** keysfrodo will be stored in the keysfrodo directory
python keygen.py
pause
copy "pk.txt" "keysfrodo\pk%one%.txt" 
copy "sk.txt" "keysfrodo\sk%one%.txt" 
pause
cls
GOTO:EOF

:menu_5   Generate keysfalcon *** cmd syntax --- pyemail.bat keyname
echo *** keysfalcon will be stored in the keysfalcon directory
python Generatekeys.py
pause
copy "pk.txt" "keysfalcon\pk%one%.txt" 
copy "sk.txt" "keysfalcon\sk%one%.txt" 
pause
cls
GOTO:EOF


:menu_

:menu_T   Tip
echo.It's easy to add a line separator using one or more fake labels
GOTO:EOF

:menu_C   Clear Screen
cls
GOTO:EOF