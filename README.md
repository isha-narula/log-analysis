# log-analysis

>ISHA NARULA

OBJECTIVE:
1. Sort the articles according to number of views.
2. List name of authors according to the number of views.
3. Find the error percentage on each day.

How to run the program ?

Requirements:
- Python3
- Vagrant
- VirtualBox

Next,
- Open terminal(linux)/gitbash(windows) in your system and change the  directory  to vagrant.
- Run command "vagrant up" to setup Virtual Machine.
- Now, run "vagrant ssh" to login and join.
- cd into the the vagrant directory
- Run psql -d news -f newsdata.sql for loading the data of the database into local database.

To Execute, 
- Run the command "python log_analysis.py" in terminal(linux)/  gitbash(windows).

