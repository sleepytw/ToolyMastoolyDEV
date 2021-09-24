@echo off
title ToolyMastooly

set cpath=%~dp0
set webserver=%cpath:~0,-24%\ToolyMastooly.py REM or whatever
set telnetserver=%cpath:~0,-24%\telnetServer.py REM or whatever

python %webserver%
python %telnetserver%