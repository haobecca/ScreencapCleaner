# Automated Screen Shot Clean-Up

## Objective

Write a python script to move screenshots to trash every once they are older than 24 hours.

## Design

1. Identify screenshots among other files.
2. Identify timestamp on screenshot.
3. Move files that are older than 24 hours to `~/.Trash`.
4. Run script periodically to ensure desktop stays tidy.

## Tools Used

### Python

From Python's standard library, the following objects and relevant class methods were used.

* `datetime` for timestamps and datetime objects.
* `os` for simplified OS-independent functionality . Notable module functions used include:
  * __`os.listdir(path='.')`__: returns a list containing the names of the entries in the directory given by path.
  * __`os.path.expanduser(path)`__: expands `~` and `~user`. If user or `$HOME` is unknown, do nothing.
  * __`os.stat(path, *)`__: gets the status of a file or a file descriptor, including creation time attribute in seconds UTC (shown below).

    ```python
    >>> import os
    >>> statinfo = os.stat('somefile.txt')
    >>> statinfo.st_ctime
    23452345234.4324  # seconds UTC
    ```

  * __`shutil.move(src, dst)`__: recursively move a file or directory (src) to (dst) and return the destination.
  * __`os.path.join(a, *p)`__: joins two or more paths, inserting '/' as needed.

### Operating System (MacOS)

The _shebang_ instructs the user's shell (e.g. bash) where to find the necessary interpreter for script. It's placed in the first line like so:

```python
#!/usr/bin/env python3
''' My Python Script '''

# ...rest of script...
```

MacOS has its own framework for managing system and user-level recurring background processes (daemons) called __`launchd`__. This tool runs successfully with user-level permissions via a simple `.plist` file and enabled via Apple's complementary command-line `launchctl` tool.

## References

* _Using launchd agents to schedule scripts on macOS_ [link](https://davidhamann.de/2018/03/13/setting-up-a-launchagent-macos-cron/)
