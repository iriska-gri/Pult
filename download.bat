ping -n 5 127.0.0.1 > NUL
erase %1
copy %2 %1
start "" /wait %1