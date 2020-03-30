@echo on
git add . 
set msg=Update: %date%-%time%
git commit -m "%msg%"
git push origin master