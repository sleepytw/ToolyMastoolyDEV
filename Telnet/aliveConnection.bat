@echo off

:pingAlive
ping 186.71.208.28 -n 1

if ERRORLEVEL == 0 echo Alive
if ERRORLEVEL == 1 echo Dead