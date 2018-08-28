# Automate Screen Shot Clean-Up
## Objective
Write a python script to move screenshots to trash every once they are older than 24 hours.

## Steps:
	1. Identify screenshots among other files 
	2. Identify timestamp on screenshot
	3. Send files that are > 24 hours old to `.Trash` folder in the home folder
	4. Repeat program every 60 seconds

## Tools Used:
* Python:
	* Built-in Str class methods to analyze filename and concatenate file paths
	* Import datetime module for timestamps and datetime objects
	* Import os module for a portable way of using operating system dependent functionality :
	
	`os.listdir(path=‘.’)`
		* Return a list containing the names of the entries in the directory given by path. 

	`os.path.expanduser(path)`
		* Expand ~ and ~user constructions.  If user or `$HOME` is unknown, do nothing.

	`os.stat(path, *, dir_fd=None, follow_symlinks=True )`
		* Get the status of a file or a file descriptor.

```python
# example:

>>> import os
>>> statinfo = os.stat('somefile.txt')
>>> statinfo.st_ctime
# returns when file was created in utc (seconds)
```

	`shutil.move(src, dst, copy_function=copy2)`
		* Recursively move a file or directory (src) to another location (dst) and return the destination.

	`os.path.join(a, *p)`
		* Join two or more pathname components, inserting '/' as needed.
		
* Shebang: Specify location of Python 3 interpreter using to run this script
```
#!/usr/bin/env python3
```

* Use [launchd agents](https://davidhamann.de/2018/03/13/setting-up-a-launchagent-macos-cron/) to schedule script on macOS


#Projects
