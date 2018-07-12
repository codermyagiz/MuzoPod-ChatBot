@echo off
del sound.mp3
rmdir /Q /S __pycache__
git pull origin master
git add .
git commit -m "."
git push origin master