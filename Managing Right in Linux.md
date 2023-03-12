Linux is a multi-user system so it is necessary to provide a permissions system to control the set of authorized operations on files and directories, which includes all the system resources and devices (on a Unix system, any device is represented by a file or directory). This principle is common to all Unix-like systems.

Each file or directory has specific permissions for three categories of users:
- The owner (represented with u as in user)
- The group (represented with g as in group)
- The others (represented with o as in others)

Three types of rights can be combined:
- **Read** (symbolized with r)
- **Write** (symbolized with w) and
- **Execute** (symbolized by x)

The commonest way to allow rights and permissions on files and folders is to use chmod, chown and chgrp.
- Eg. To allow a read right on a folder or file for a user/owner, **chmod u+r path/to/file_or_folder**
- To allow all rights i.e **read, write and execute** for a user/owner, **chmod u+rwx path/to/file_or_folder**

------------------------------------------------------------

Do you also know that we can use figures as in numbers to represent those rights and user categories?
Let's dive into it.
I'm pretty sure most of us have seen some of these commands before:
- chmod 700 hello.py, chmod 754 hello_world.sh, or chmod 777 /etc/kubernetes however, we do not understand the figures.
- This is what they mean.
Remember the three rights stated earlier, this is what they are reffered to in numerical terms. **4 - read, 2 - write and 1 - execute** and each of the commands above (chmod '700') also represent **7-user, 0-group and 0-others** in that order.

Now, that is not the end of it. Each figure (700) = chmod 7=4+2+1 0=0+0+0 0=0+0+0 which all represent the read, write and execute permissions for each user on a file or directory.

Eg. **chmod 754 hello.py** means *a user/owner can 4-read, 2-write and 1-execute the hello.py file, and the group users can 4-read and 1-execute the hello.py file*, but the other users can only 4-read that file.

So just do the math whenever you want to use **chmod 777** on any important file.
