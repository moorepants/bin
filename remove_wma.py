"""This script finds all wma files. Each should have an mp3 copy. It moves the
mp3s to a new folder. It removes the wma files from the beets database and
disk. This sets you up to import the mp3s in to the database and not have any
more wmas.

NOTE: If there were no mp3s of the wmas, I may have deleted a bunch of music..."""
import os
import subprocess

MP3_DIR = '/home/moorepants/music-src/wma_copies'

if not os.path.exists(MP3_DIR):
    os.makedirs(MP3_DIR)

# find all wma files
for root, dirs, files in os.walk("/home/moorepants/Music"):
    for filename in files:
        if filename.endswith(".wma"):
            name, ext = os.path.splitext(filename)
            mp3_filename = name + '.mp3'
            mp3_filepath = os.path.join(root, mp3_filename)
            _, album_rel_path = root.split('Music/')
            mp3_album_dir = os.path.join(MP3_DIR, album_rel_path)
            if not os.path.exists(mp3_album_dir):
                os.makedirs(mp3_album_dir)
            mp3_newfilepath = os.path.join(mp3_album_dir, mp3_filename)
            artist, album = album_rel_path.split('/')
            if os.path.exists(mp3_filepath):
                # move the mp3s into a new directory with same directory hierarchy
                print('Moving {} to {}'.format(mp3_filepath, mp3_newfilepath))
                os.rename(mp3_filepath, mp3_newfilepath)

                #cmd = 'beet remove -df path:"{}"'
                cmd = 'beet list path:"{}"'
                print(cmd.format(os.path.join(root, filename)))
                path_stm = 'path:{}'.format(os.path.join(root, filename))
                print(path_stm)
                cmd = ['beet', 'list', path_stm]
                cmd = ['beet', 'remove', '-df', path_stm]
                subprocess.check_call(cmd)
                print('\n')

"""
These are the files it dealt with.
(beets) moorepants@parvati:~$ python bin/remove_wma.py
Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/03 Man.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/03 Man.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/03 Man.wma"
path:""/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/03 Man.wma""


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/11 Modern Romance _ Poor Song.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/11 Modern Romance _ Poor Song.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/11 Modern Romance _ Poor Song.wma"
path:""/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/11 Modern Romance _ Poor Song.wma""


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/08 No No No.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/08 No No No.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/08 No No No.wma"
path:""/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/08 No No No.wma""


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/10 Y Control.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/10 Y Control.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/10 Y Control.wma"
path:""/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/10 Y Control.wma""


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/06 Pin.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/06 Pin.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/06 Pin.wma"
path:""/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/06 Pin.wma""


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/07 Cold Light.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/07 Cold Light.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/07 Cold Light.wma"
path:""/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/07 Cold Light.wma""


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/05 Black Tongue.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/05 Black Tongue.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/05 Black Tongue.wma"
path:""/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/05 Black Tongue.wma""


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/01 Rich.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/01 Rich.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/01 Rich.wma"
path:""/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/01 Rich.wma""


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/09 Maps.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/09 Maps.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/09 Maps.wma"
path:""/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/09 Maps.wma""
^CTraceback (most recent call last):
  File "/home/moorepants/miniconda/envs/beets/bin/beet", line 7, in <module>
    from beets.ui import main
  File "/home/moorepants/miniconda/envs/beets/lib/python2.7/site-packages/beets/__init__.py", line 20, in <module>
Traceback (most recent call last):
  File "bin/remove_wma.py", line 33, in <module>
    subprocess.check_call(cmd)
  File "/home/moorepants/miniconda/envs/beets/lib/python2.7/subprocess.py", line 181, in check_call
    from beets.util import confit
      File "/home/moorepants/miniconda/envs/beets/lib/python2.7/site-packages/beets/util/__init__.py", line 30, in <module>
retcode = call(*popenargs, **kwargs)
  File "/home/moorepants/miniconda/envs/beets/lib/python2.7/subprocess.py", line 168, in call
    return Popen(*popenargs, **kwargs).wait()
  File "/home/moorepants/miniconda/envs/beets/lib/python2.7/subprocess.py", line 1073, in wait
    import shlex
  File "/home/moorepants/miniconda/envs/beets/lib/python2.7/shlex.py", line 2, in <module>
    pid, sts = _eintr_retry_call(os.waitpid, self.pid, 0)
  File "/home/moorepants/miniconda/envs/beets/lib/python2.7/subprocess.py", line 121, in _eintr_retry_call
    return func(*args)
KeyboardInterrupt
    """A lexical analyzer class for simple shell-like syntaxes."""
KeyboardInterrupt
(beets) moorepants@parvati:~$ python bin/remove_wma.py
Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/03 Man.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/03 Man.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/03 Man.wma"
path:/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/03 Man.wma
Yeah Yeah Yeahs - Fever to Tell - Man


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/11 Modern Romance _ Poor Song.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/11 Modern Romance _ Poor Song.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/11 Modern Romance _ Poor Song.wma"
path:/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/11 Modern Romance _ Poor Song.wma
Yeah Yeah Yeahs - Fever to Tell - Modern Romance / Poor Song


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/08 No No No.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/08 No No No.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/08 No No No.wma"
path:/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/08 No No No.wma
Yeah Yeah Yeahs - Fever to Tell - No No No


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/10 Y Control.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/10 Y Control.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/10 Y Control.wma"
path:/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/10 Y Control.wma
Yeah Yeah Yeahs - Fever to Tell - Y Control


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/06 Pin.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/06 Pin.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/06 Pin.wma"
path:/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/06 Pin.wma
Yeah Yeah Yeahs - Fever to Tell - Pin


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/07 Cold Light.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/07 Cold Light.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/07 Cold Light.wma"
path:/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/07 Cold Light.wma
Yeah Yeah Yeahs - Fever to Tell - Cold Light


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/05 Black Tongue.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/05 Black Tongue.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/05 Black Tongue.wma"
path:/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/05 Black Tongue.wma
Yeah Yeah Yeahs - Fever to Tell - Black Tongue


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/01 Rich.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/01 Rich.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/01 Rich.wma"
path:/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/01 Rich.wma
Yeah Yeah Yeahs - Fever to Tell - Rich


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/09 Maps.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/09 Maps.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/09 Maps.wma"
path:/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/09 Maps.wma
Yeah Yeah Yeahs - Fever to Tell - Maps


Moving /home/moorepants/Music/Marry Mannor/_3Come Home_3/03 lover.mp3 to /home/moorepants/music-src/wma_copies/Marry Mannor/_3Come Home_3/03 lover.mp3
beet list path:"/home/moorepants/Music/Marry Mannor/_3Come Home_3/03 lover.wma"
path:/home/moorepants/Music/Marry Mannor/_3Come Home_3/03 lover.wma
Marry Mannor - <3Come Home<3 - lover


Moving /home/moorepants/Music/Marry Mannor/_3Come Home_3/04 sea of love.mp3 to /home/moorepants/music-src/wma_copies/Marry Mannor/_3Come Home_3/04 sea of love.mp3
beet list path:"/home/moorepants/Music/Marry Mannor/_3Come Home_3/04 sea of love.wma"
path:/home/moorepants/Music/Marry Mannor/_3Come Home_3/04 sea of love.wma
Marry Mannor - <3Come Home<3 - sea of love


Moving /home/moorepants/Music/Marry Mannor/_3Come Home_3/05 ms sanders.mp3 to /home/moorepants/music-src/wma_copies/Marry Mannor/_3Come Home_3/05 ms sanders.mp3
beet list path:"/home/moorepants/Music/Marry Mannor/_3Come Home_3/05 ms sanders.wma"
path:/home/moorepants/Music/Marry Mannor/_3Come Home_3/05 ms sanders.wma
Marry Mannor - <3Come Home<3 - ms sanders


Moving /home/moorepants/Music/Marry Mannor/_3Come Home_3/02 red shoes.mp3 to /home/moorepants/music-src/wma_copies/Marry Mannor/_3Come Home_3/02 red shoes.mp3
beet list path:"/home/moorepants/Music/Marry Mannor/_3Come Home_3/02 red shoes.wma"
path:/home/moorepants/Music/Marry Mannor/_3Come Home_3/02 red shoes.wma
Marry Mannor - <3Come Home<3 - red shoes


Moving /home/moorepants/Music/Marry Mannor/_3Come Home_3/01 heat wave.mp3 to /home/moorepants/music-src/wma_copies/Marry Mannor/_3Come Home_3/01 heat wave.mp3
beet list path:"/home/moorepants/Music/Marry Mannor/_3Come Home_3/01 heat wave.wma"
path:/home/moorepants/Music/Marry Mannor/_3Come Home_3/01 heat wave.wma
Marry Mannor - <3Come Home<3 - heat wave


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/06 Maddox Table.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/06 Maddox Table.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/06 Maddox Table.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/06 Maddox Table.wma
10,000 Maniacs - The Wishing Chair - Maddox Table


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/03 Just as the Tide Was a Flowing.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/03 Just as the Tide Was a Flowing.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/03 Just as the Tide Was a Flowing.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/03 Just as the Tide Was a Flowing.wma
10,000 Maniacs - The Wishing Chair - Just as the Tide Was a Flowing


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/09 Among the Americans.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/09 Among the Americans.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/09 Among the Americans.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/09 Among the Americans.wma
10,000 Maniacs - The Wishing Chair - Among the Americans


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/10 Everyone a Puzzle Lover.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/10 Everyone a Puzzle Lover.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/10 Everyone a Puzzle Lover.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/10 Everyone a Puzzle Lover.wma
10,000 Maniacs - The Wishing Chair - Everyone a Puzzle Lover


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/01 Can’t Ignore the Train.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/01 Can’t Ignore the Train.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/01 Can’t Ignore the Train.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/01 Can’t Ignore the Train.wma
10,000 Maniacs - The Wishing Chair - Can’t Ignore the Train


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/04 Lilydale.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/04 Lilydale.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/04 Lilydale.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/04 Lilydale.wma
^CTraceback (most recent call last):
  File "bin/remove_wma.py", line 33, in <module>
    subprocess.check_call(cmd)
  File "/home/moorepants/miniconda/envs/beets/lib/python2.7/subprocess.py", line 181, in check_call
    retcode = call(*popenargs, **kwargs)
  File "/home/moorepants/miniconda/envs/beets/lib/python2.7/subprocess.py", line 168, in call
    return Popen(*popenargs, **kwargs).wait()
  File "/home/moorepants/miniconda/envs/beets/lib/python2.7/subprocess.py", line 1073, in wait
    pid, sts = _eintr_retry_call(os.waitpid, self.pid, 0)
  File "/home/moorepants/miniconda/envs/beets/lib/python2.7/subprocess.py", line 121, in _eintr_retry_call
    return func(*args)
KeyboardInterrupt
(beets) moorepants@parvati:~$ python bin/remove_wma.py
Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/03 Man.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/03 Man.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/03 Man.wma"
path:/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/03 Man.wma


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/11 Modern Romance _ Poor Song.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/11 Modern Romance _ Poor Song.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/11 Modern Romance _ Poor Song.wma"
path:/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/11 Modern Romance _ Poor Song.wma


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/08 No No No.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/08 No No No.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/08 No No No.wma"
path:/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/08 No No No.wma


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/10 Y Control.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/10 Y Control.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/10 Y Control.wma"
path:/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/10 Y Control.wma


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/06 Pin.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/06 Pin.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/06 Pin.wma"
path:/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/06 Pin.wma


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/07 Cold Light.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/07 Cold Light.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/07 Cold Light.wma"
path:/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/07 Cold Light.wma


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/05 Black Tongue.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/05 Black Tongue.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/05 Black Tongue.wma"
path:/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/05 Black Tongue.wma


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/01 Rich.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/01 Rich.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/01 Rich.wma"
path:/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/01 Rich.wma


Moving /home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/09 Maps.mp3 to /home/moorepants/music-src/wma_copies/Yeah Yeah Yeahs/Fever to Tell/09 Maps.mp3
beet list path:"/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/09 Maps.wma"
path:/home/moorepants/Music/Yeah Yeah Yeahs/Fever to Tell/09 Maps.wma


Moving /home/moorepants/Music/Marry Mannor/_3Come Home_3/03 lover.mp3 to /home/moorepants/music-src/wma_copies/Marry Mannor/_3Come Home_3/03 lover.mp3
beet list path:"/home/moorepants/Music/Marry Mannor/_3Come Home_3/03 lover.wma"
path:/home/moorepants/Music/Marry Mannor/_3Come Home_3/03 lover.wma


Moving /home/moorepants/Music/Marry Mannor/_3Come Home_3/04 sea of love.mp3 to /home/moorepants/music-src/wma_copies/Marry Mannor/_3Come Home_3/04 sea of love.mp3
beet list path:"/home/moorepants/Music/Marry Mannor/_3Come Home_3/04 sea of love.wma"
path:/home/moorepants/Music/Marry Mannor/_3Come Home_3/04 sea of love.wma


Moving /home/moorepants/Music/Marry Mannor/_3Come Home_3/05 ms sanders.mp3 to /home/moorepants/music-src/wma_copies/Marry Mannor/_3Come Home_3/05 ms sanders.mp3
beet list path:"/home/moorepants/Music/Marry Mannor/_3Come Home_3/05 ms sanders.wma"
path:/home/moorepants/Music/Marry Mannor/_3Come Home_3/05 ms sanders.wma


Moving /home/moorepants/Music/Marry Mannor/_3Come Home_3/02 red shoes.mp3 to /home/moorepants/music-src/wma_copies/Marry Mannor/_3Come Home_3/02 red shoes.mp3
beet list path:"/home/moorepants/Music/Marry Mannor/_3Come Home_3/02 red shoes.wma"
path:/home/moorepants/Music/Marry Mannor/_3Come Home_3/02 red shoes.wma


Moving /home/moorepants/Music/Marry Mannor/_3Come Home_3/01 heat wave.mp3 to /home/moorepants/music-src/wma_copies/Marry Mannor/_3Come Home_3/01 heat wave.mp3
beet list path:"/home/moorepants/Music/Marry Mannor/_3Come Home_3/01 heat wave.wma"
path:/home/moorepants/Music/Marry Mannor/_3Come Home_3/01 heat wave.wma


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/06 Maddox Table.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/06 Maddox Table.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/06 Maddox Table.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/06 Maddox Table.wma


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/03 Just as the Tide Was a Flowing.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/03 Just as the Tide Was a Flowing.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/03 Just as the Tide Was a Flowing.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/03 Just as the Tide Was a Flowing.wma


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/09 Among the Americans.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/09 Among the Americans.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/09 Among the Americans.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/09 Among the Americans.wma


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/10 Everyone a Puzzle Lover.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/10 Everyone a Puzzle Lover.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/10 Everyone a Puzzle Lover.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/10 Everyone a Puzzle Lover.wma


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/01 Can’t Ignore the Train.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/01 Can’t Ignore the Train.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/01 Can’t Ignore the Train.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/01 Can’t Ignore the Train.wma


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/04 Lilydale.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/04 Lilydale.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/04 Lilydale.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/04 Lilydale.wma


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/05 Back o’ the Moon.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/05 Back o’ the Moon.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/05 Back o’ the Moon.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/05 Back o’ the Moon.wma


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/11 Cotton Alley.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/11 Cotton Alley.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/11 Cotton Alley.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/11 Cotton Alley.wma


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/07 The Colonial Wing.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/07 The Colonial Wing.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/07 The Colonial Wing.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/07 The Colonial Wing.wma


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/12 Daktari.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/12 Daktari.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/12 Daktari.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/12 Daktari.wma


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/15 Arbor Day.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/15 Arbor Day.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/15 Arbor Day.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/15 Arbor Day.wma


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/14 Tension Makes a Tangle.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/14 Tension Makes a Tangle.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/14 Tension Makes a Tangle.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/14 Tension Makes a Tangle.wma


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/13 My Mother the War.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/13 My Mother the War.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/13 My Mother the War.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/13 My Mother the War.wma


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/08 Grey Victory.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/08 Grey Victory.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/08 Grey Victory.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/08 Grey Victory.wma


Moving /home/moorepants/Music/10,000 Maniacs/The Wishing Chair/02 Scorpio Rising.mp3 to /home/moorepants/music-src/wma_copies/10,000 Maniacs/The Wishing Chair/02 Scorpio Rising.mp3
beet list path:"/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/02 Scorpio Rising.wma"
path:/home/moorepants/Music/10,000 Maniacs/The Wishing Chair/02 Scorpio Rising.wma


Moving /home/moorepants/Music/Marcy Playground/Marcy Playground/10 Dog and His Master.mp3 to /home/moorepants/music-src/wma_copies/Marcy Playground/Marcy Playground/10 Dog and His Master.mp3
beet list path:"/home/moorepants/Music/Marcy Playground/Marcy Playground/10 Dog and His Master.wma"
path:/home/moorepants/Music/Marcy Playground/Marcy Playground/10 Dog and His Master.wma


Moving /home/moorepants/Music/Marcy Playground/Marcy Playground/06 Sherry Fraser.mp3 to /home/moorepants/music-src/wma_copies/Marcy Playground/Marcy Playground/06 Sherry Fraser.mp3
beet list path:"/home/moorepants/Music/Marcy Playground/Marcy Playground/06 Sherry Fraser.wma"
path:/home/moorepants/Music/Marcy Playground/Marcy Playground/06 Sherry Fraser.wma


Moving /home/moorepants/Music/Marcy Playground/Marcy Playground/01 Poppies.mp3 to /home/moorepants/music-src/wma_copies/Marcy Playground/Marcy Playground/01 Poppies.mp3
beet list path:"/home/moorepants/Music/Marcy Playground/Marcy Playground/01 Poppies.wma"
path:/home/moorepants/Music/Marcy Playground/Marcy Playground/01 Poppies.wma


Moving /home/moorepants/Music/Marcy Playground/Marcy Playground/11 The Shadow of Seattle.mp3 to /home/moorepants/music-src/wma_copies/Marcy Playground/Marcy Playground/11 The Shadow of Seattle.mp3
beet list path:"/home/moorepants/Music/Marcy Playground/Marcy Playground/11 The Shadow of Seattle.wma"
path:/home/moorepants/Music/Marcy Playground/Marcy Playground/11 The Shadow of Seattle.wma


Moving /home/moorepants/Music/Marcy Playground/Marcy Playground/05 A Cloak of Elvenkind.mp3 to /home/moorepants/music-src/wma_copies/Marcy Playground/Marcy Playground/05 A Cloak of Elvenkind.mp3
beet list path:"/home/moorepants/Music/Marcy Playground/Marcy Playground/05 A Cloak of Elvenkind.wma"
path:/home/moorepants/Music/Marcy Playground/Marcy Playground/05 A Cloak of Elvenkind.wma


Moving /home/moorepants/Music/Marcy Playground/Marcy Playground/07 Gone Crazy.mp3 to /home/moorepants/music-src/wma_copies/Marcy Playground/Marcy Playground/07 Gone Crazy.mp3
beet list path:"/home/moorepants/Music/Marcy Playground/Marcy Playground/07 Gone Crazy.wma"
path:/home/moorepants/Music/Marcy Playground/Marcy Playground/07 Gone Crazy.wma


Moving /home/moorepants/Music/Marcy Playground/Marcy Playground/03 Ancient Walls of Flowers.mp3 to /home/moorepants/music-src/wma_copies/Marcy Playground/Marcy Playground/03 Ancient Walls of Flowers.mp3
beet list path:"/home/moorepants/Music/Marcy Playground/Marcy Playground/03 Ancient Walls of Flowers.wma"
path:/home/moorepants/Music/Marcy Playground/Marcy Playground/03 Ancient Walls of Flowers.wma


Moving /home/moorepants/Music/Marcy Playground/Marcy Playground/04 Saint Joe on the School Bus.mp3 to /home/moorepants/music-src/wma_copies/Marcy Playground/Marcy Playground/04 Saint Joe on the School Bus.mp3
beet list path:"/home/moorepants/Music/Marcy Playground/Marcy Playground/04 Saint Joe on the School Bus.wma"
path:/home/moorepants/Music/Marcy Playground/Marcy Playground/04 Saint Joe on the School Bus.wma


Moving /home/moorepants/Music/Marcy Playground/Marcy Playground/08 Opium.mp3 to /home/moorepants/music-src/wma_copies/Marcy Playground/Marcy Playground/08 Opium.mp3
beet list path:"/home/moorepants/Music/Marcy Playground/Marcy Playground/08 Opium.wma"
path:/home/moorepants/Music/Marcy Playground/Marcy Playground/08 Opium.wma


Moving /home/moorepants/Music/Marcy Playground/Marcy Playground/12 The Vampires of New York.mp3 to /home/moorepants/music-src/wma_copies/Marcy Playground/Marcy Playground/12 The Vampires of New York.mp3
beet list path:"/home/moorepants/Music/Marcy Playground/Marcy Playground/12 The Vampires of New York.wma"
path:/home/moorepants/Music/Marcy Playground/Marcy Playground/12 The Vampires of New York.wma


Moving /home/moorepants/Music/Marcy Playground/Marcy Playground/02 Sex and Candy.mp3 to /home/moorepants/music-src/wma_copies/Marcy Playground/Marcy Playground/02 Sex and Candy.mp3
beet list path:"/home/moorepants/Music/Marcy Playground/Marcy Playground/02 Sex and Candy.wma"
path:/home/moorepants/Music/Marcy Playground/Marcy Playground/02 Sex and Candy.wma


Moving /home/moorepants/Music/Marcy Playground/Marcy Playground/09 One More Suicide.mp3 to /home/moorepants/music-src/wma_copies/Marcy Playground/Marcy Playground/09 One More Suicide.mp3
beet list path:"/home/moorepants/Music/Marcy Playground/Marcy Playground/09 One More Suicide.wma"
path:/home/moorepants/Music/Marcy Playground/Marcy Playground/09 One More Suicide.wma


Moving /home/moorepants/Music/Pearl Jam/Vs_/04 Glorified G.mp3 to /home/moorepants/music-src/wma_copies/Pearl Jam/Vs_/04 Glorified G.mp3
beet list path:"/home/moorepants/Music/Pearl Jam/Vs_/04 Glorified G.wma"
path:/home/moorepants/Music/Pearl Jam/Vs_/04 Glorified G.wma


Moving /home/moorepants/Music/Pearl Jam/Vs_/05 Dissident.mp3 to /home/moorepants/music-src/wma_copies/Pearl Jam/Vs_/05 Dissident.mp3
beet list path:"/home/moorepants/Music/Pearl Jam/Vs_/05 Dissident.wma"
path:/home/moorepants/Music/Pearl Jam/Vs_/05 Dissident.wma


Moving /home/moorepants/Music/Pearl Jam/Vs_/07 Blood.mp3 to /home/moorepants/music-src/wma_copies/Pearl Jam/Vs_/07 Blood.mp3
beet list path:"/home/moorepants/Music/Pearl Jam/Vs_/07 Blood.wma"
path:/home/moorepants/Music/Pearl Jam/Vs_/07 Blood.wma


Moving /home/moorepants/Music/Pearl Jam/Vs_/11 Leash.mp3 to /home/moorepants/music-src/wma_copies/Pearl Jam/Vs_/11 Leash.mp3
beet list path:"/home/moorepants/Music/Pearl Jam/Vs_/11 Leash.wma"
path:/home/moorepants/Music/Pearl Jam/Vs_/11 Leash.wma


Moving /home/moorepants/Music/Pearl Jam/Vs_/01 Go.mp3 to /home/moorepants/music-src/wma_copies/Pearl Jam/Vs_/01 Go.mp3
beet list path:"/home/moorepants/Music/Pearl Jam/Vs_/01 Go.wma"
path:/home/moorepants/Music/Pearl Jam/Vs_/01 Go.wma


Moving /home/moorepants/Music/Pearl Jam/Vs_/08 Rearviewmirror.mp3 to /home/moorepants/music-src/wma_copies/Pearl Jam/Vs_/08 Rearviewmirror.mp3
beet list path:"/home/moorepants/Music/Pearl Jam/Vs_/08 Rearviewmirror.wma"
path:/home/moorepants/Music/Pearl Jam/Vs_/08 Rearviewmirror.wma


Moving /home/moorepants/Music/Pearl Jam/Vs_/10 Elderly Woman Behind the Counter in a Small Town.mp3 to /home/moorepants/music-src/wma_copies/Pearl Jam/Vs_/10 Elderly Woman Behind the Counter in a Small Town.mp3
beet list path:"/home/moorepants/Music/Pearl Jam/Vs_/10 Elderly Woman Behind the Counter in a Small Town.wma"
path:/home/moorepants/Music/Pearl Jam/Vs_/10 Elderly Woman Behind the Counter in a Small Town.wma


Moving /home/moorepants/Music/Pearl Jam/Vs_/06 W.M.A_.mp3 to /home/moorepants/music-src/wma_copies/Pearl Jam/Vs_/06 W.M.A_.mp3
beet list path:"/home/moorepants/Music/Pearl Jam/Vs_/06 W.M.A_.wma"
path:/home/moorepants/Music/Pearl Jam/Vs_/06 W.M.A_.wma


Moving /home/moorepants/Music/Pearl Jam/Vs_/09 Rats.mp3 to /home/moorepants/music-src/wma_copies/Pearl Jam/Vs_/09 Rats.mp3
beet list path:"/home/moorepants/Music/Pearl Jam/Vs_/09 Rats.wma"
path:/home/moorepants/Music/Pearl Jam/Vs_/09 Rats.wma


Moving /home/moorepants/Music/Pearl Jam/Vs_/03 Daughter.mp3 to /home/moorepants/music-src/wma_copies/Pearl Jam/Vs_/03 Daughter.mp3
beet list path:"/home/moorepants/Music/Pearl Jam/Vs_/03 Daughter.wma"
path:/home/moorepants/Music/Pearl Jam/Vs_/03 Daughter.wma


Moving /home/moorepants/Music/Pearl Jam/Vs_/02 Animal.mp3 to /home/moorepants/music-src/wma_copies/Pearl Jam/Vs_/02 Animal.mp3
beet list path:"/home/moorepants/Music/Pearl Jam/Vs_/02 Animal.wma"
path:/home/moorepants/Music/Pearl Jam/Vs_/02 Animal.wma


Moving /home/moorepants/Music/Pearl Jam/Vs_/12 Indifference.mp3 to /home/moorepants/music-src/wma_copies/Pearl Jam/Vs_/12 Indifference.mp3
beet list path:"/home/moorepants/Music/Pearl Jam/Vs_/12 Indifference.wma"
path:/home/moorepants/Music/Pearl Jam/Vs_/12 Indifference.wma


Moving /home/moorepants/Music/Oasis/Stop the Clocks 1946/13 Half the World Away.mp3 to /home/moorepants/music-src/wma_copies/Oasis/Stop the Clocks 1946/13 Half the World Away.mp3
beet list path:"/home/moorepants/Music/Oasis/Stop the Clocks 1946/13 Half the World Away.wma"
path:/home/moorepants/Music/Oasis/Stop the Clocks 1946/13 Half the World Away.wma


Moving /home/moorepants/Music/Oasis/Stop the Clocks 1946/08 Cigarettes & Alcohol.mp3 to /home/moorepants/music-src/wma_copies/Oasis/Stop the Clocks 1946/08 Cigarettes & Alcohol.mp3
beet list path:"/home/moorepants/Music/Oasis/Stop the Clocks 1946/08 Cigarettes & Alcohol.wma"
path:/home/moorepants/Music/Oasis/Stop the Clocks 1946/08 Cigarettes & Alcohol.wma


Moving /home/moorepants/Music/Oasis/Stop the Clocks 1946/11 Acquiesce.mp3 to /home/moorepants/music-src/wma_copies/Oasis/Stop the Clocks 1946/11 Acquiesce.mp3
beet list path:"/home/moorepants/Music/Oasis/Stop the Clocks 1946/11 Acquiesce.wma"
path:/home/moorepants/Music/Oasis/Stop the Clocks 1946/11 Acquiesce.wma


Moving /home/moorepants/Music/Oasis/Stop the Clocks 1946/10 Live Forever.mp3 to /home/moorepants/music-src/wma_copies/Oasis/Stop the Clocks 1946/10 Live Forever.mp3
beet list path:"/home/moorepants/Music/Oasis/Stop the Clocks 1946/10 Live Forever.wma"
path:/home/moorepants/Music/Oasis/Stop the Clocks 1946/10 Live Forever.wma


Moving /home/moorepants/Music/Oasis/Stop the Clocks 1946/17 Champagne Supernova.mp3 to /home/moorepants/music-src/wma_copies/Oasis/Stop the Clocks 1946/17 Champagne Supernova.mp3
beet list path:"/home/moorepants/Music/Oasis/Stop the Clocks 1946/17 Champagne Supernova.wma"
path:/home/moorepants/Music/Oasis/Stop the Clocks 1946/17 Champagne Supernova.wma


Moving /home/moorepants/Music/Oasis/Stop the Clocks 1946/12 Supersonic.mp3 to /home/moorepants/music-src/wma_copies/Oasis/Stop the Clocks 1946/12 Supersonic.mp3
beet list path:"/home/moorepants/Music/Oasis/Stop the Clocks 1946/12 Supersonic.wma"
path:/home/moorepants/Music/Oasis/Stop the Clocks 1946/12 Supersonic.wma


Moving /home/moorepants/Music/Oasis/Stop the Clocks 1946/03 Talk Tonight.mp3 to /home/moorepants/music-src/wma_copies/Oasis/Stop the Clocks 1946/03 Talk Tonight.mp3
beet list path:"/home/moorepants/Music/Oasis/Stop the Clocks 1946/03 Talk Tonight.wma"
path:/home/moorepants/Music/Oasis/Stop the Clocks 1946/03 Talk Tonight.wma


Moving /home/moorepants/Music/Oasis/Stop the Clocks 1946/16 Morning Glory.mp3 to /home/moorepants/music-src/wma_copies/Oasis/Stop the Clocks 1946/16 Morning Glory.mp3
beet list path:"/home/moorepants/Music/Oasis/Stop the Clocks 1946/16 Morning Glory.wma"
path:/home/moorepants/Music/Oasis/Stop the Clocks 1946/16 Morning Glory.wma


Moving /home/moorepants/Music/Oasis/Stop the Clocks 1946/14 Go Let It Out.mp3 to /home/moorepants/music-src/wma_copies/Oasis/Stop the Clocks 1946/14 Go Let It Out.mp3
beet list path:"/home/moorepants/Music/Oasis/Stop the Clocks 1946/14 Go Let It Out.wma"
path:/home/moorepants/Music/Oasis/Stop the Clocks 1946/14 Go Let It Out.wma


Moving /home/moorepants/Music/Oasis/Stop the Clocks 1946/07 Slide Away.mp3 to /home/moorepants/music-src/wma_copies/Oasis/Stop the Clocks 1946/07 Slide Away.mp3
beet list path:"/home/moorepants/Music/Oasis/Stop the Clocks 1946/07 Slide Away.wma"
path:/home/moorepants/Music/Oasis/Stop the Clocks 1946/07 Slide Away.wma


Moving /home/moorepants/Music/Oasis/Stop the Clocks 1946/09 The Masterplan.mp3 to /home/moorepants/music-src/wma_copies/Oasis/Stop the Clocks 1946/09 The Masterplan.mp3
beet list path:"/home/moorepants/Music/Oasis/Stop the Clocks 1946/09 The Masterplan.wma"
path:/home/moorepants/Music/Oasis/Stop the Clocks 1946/09 The Masterplan.wma


Moving /home/moorepants/Music/Oasis/Stop the Clocks 1946/06 Wonderwall.mp3 to /home/moorepants/music-src/wma_copies/Oasis/Stop the Clocks 1946/06 Wonderwall.mp3
beet list path:"/home/moorepants/Music/Oasis/Stop the Clocks 1946/06 Wonderwall.wma"
path:/home/moorepants/Music/Oasis/Stop the Clocks 1946/06 Wonderwall.wma


Moving /home/moorepants/Music/Oasis/Stop the Clocks 1946/15 Songbird.mp3 to /home/moorepants/music-src/wma_copies/Oasis/Stop the Clocks 1946/15 Songbird.mp3
beet list path:"/home/moorepants/Music/Oasis/Stop the Clocks 1946/15 Songbird.wma"
path:/home/moorepants/Music/Oasis/Stop the Clocks 1946/15 Songbird.wma


Moving /home/moorepants/Music/Oasis/Stop the Clocks 1946/02 Some Might Say.mp3 to /home/moorepants/music-src/wma_copies/Oasis/Stop the Clocks 1946/02 Some Might Say.mp3
beet list path:"/home/moorepants/Music/Oasis/Stop the Clocks 1946/02 Some Might Say.wma"
path:/home/moorepants/Music/Oasis/Stop the Clocks 1946/02 Some Might Say.wma


Moving /home/moorepants/Music/Oasis/Stop the Clocks 1946/01 Rock 'n' Roll Star.mp3 to /home/moorepants/music-src/wma_copies/Oasis/Stop the Clocks 1946/01 Rock 'n' Roll Star.mp3
beet list path:"/home/moorepants/Music/Oasis/Stop the Clocks 1946/01 Rock 'n' Roll Star.wma"
path:/home/moorepants/Music/Oasis/Stop the Clocks 1946/01 Rock 'n' Roll Star.wma


Moving /home/moorepants/Music/Oasis/Stop the Clocks 1946/18 Don't Look Back in Anger.mp3 to /home/moorepants/music-src/wma_copies/Oasis/Stop the Clocks 1946/18 Don't Look Back in Anger.mp3
beet list path:"/home/moorepants/Music/Oasis/Stop the Clocks 1946/18 Don't Look Back in Anger.wma"
path:/home/moorepants/Music/Oasis/Stop the Clocks 1946/18 Don't Look Back in Anger.wma


Moving /home/moorepants/Music/Oasis/Stop the Clocks 1946/05 The Importance of Being Idle.mp3 to /home/moorepants/music-src/wma_copies/Oasis/Stop the Clocks 1946/05 The Importance of Being Idle.mp3
beet list path:"/home/moorepants/Music/Oasis/Stop the Clocks 1946/05 The Importance of Being Idle.wma"
path:/home/moorepants/Music/Oasis/Stop the Clocks 1946/05 The Importance of Being Idle.wma


Moving /home/moorepants/Music/Oasis/Stop the Clocks 1946/04 Lyla.mp3 to /home/moorepants/music-src/wma_copies/Oasis/Stop the Clocks 1946/04 Lyla.mp3
beet list path:"/home/moorepants/Music/Oasis/Stop the Clocks 1946/04 Lyla.wma"
path:/home/moorepants/Music/Oasis/Stop the Clocks 1946/04 Lyla.wma


Moving /home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/08 Memories Can't Wait.mp3 to /home/moorepants/music-src/wma_copies/Talking Heads/The Best of Talking Heads [Sire Records]/08 Memories Can't Wait.mp3
beet list path:"/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/08 Memories Can't Wait.wma"
path:/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/08 Memories Can't Wait.wma


Moving /home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/09 Once in a Lifetime.mp3 to /home/moorepants/music-src/wma_copies/Talking Heads/The Best of Talking Heads [Sire Records]/09 Once in a Lifetime.mp3
beet list path:"/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/09 Once in a Lifetime.wma"
path:/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/09 Once in a Lifetime.wma


Moving /home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/18 (Nothing but) Flowers.mp3 to /home/moorepants/music-src/wma_copies/Talking Heads/The Best of Talking Heads [Sire Records]/18 (Nothing but) Flowers.mp3
beet list path:"/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/18 (Nothing but) Flowers.wma"
path:/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/18 (Nothing but) Flowers.wma


Moving /home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/06 Life During Wartime.mp3 to /home/moorepants/music-src/wma_copies/Talking Heads/The Best of Talking Heads [Sire Records]/06 Life During Wartime.mp3
beet list path:"/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/06 Life During Wartime.wma"
path:/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/06 Life During Wartime.wma


Moving /home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/17 Blind.mp3 to /home/moorepants/music-src/wma_copies/Talking Heads/The Best of Talking Heads [Sire Records]/17 Blind.mp3
beet list path:"/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/17 Blind.wma"
path:/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/17 Blind.wma


Moving /home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/05 Found a Job.mp3 to /home/moorepants/music-src/wma_copies/Talking Heads/The Best of Talking Heads [Sire Records]/05 Found a Job.mp3
beet list path:"/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/05 Found a Job.wma"
path:/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/05 Found a Job.wma


Moving /home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/03 Uh-Oh, Love Comes to Town.mp3 to /home/moorepants/music-src/wma_copies/Talking Heads/The Best of Talking Heads [Sire Records]/03 Uh-Oh, Love Comes to Town.mp3
beet list path:"/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/03 Uh-Oh, Love Comes to Town.wma"
path:/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/03 Uh-Oh, Love Comes to Town.wma


Moving /home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/10 Houses in Motion.mp3 to /home/moorepants/music-src/wma_copies/Talking Heads/The Best of Talking Heads [Sire Records]/10 Houses in Motion.mp3
beet list path:"/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/10 Houses in Motion.wma"
path:/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/10 Houses in Motion.wma


Moving /home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/11 This Must Be the Place (Naive Melody).mp3 to /home/moorepants/music-src/wma_copies/Talking Heads/The Best of Talking Heads [Sire Records]/11 This Must Be the Place (Naive Melody).mp3
beet list path:"/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/11 This Must Be the Place (Naive Melody).wma"
path:/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/11 This Must Be the Place (Naive Melody).wma


Moving /home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/12 Girlfriend Is Better.mp3 to /home/moorepants/music-src/wma_copies/Talking Heads/The Best of Talking Heads [Sire Records]/12 Girlfriend Is Better.mp3
beet list path:"/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/12 Girlfriend Is Better.wma"
path:/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/12 Girlfriend Is Better.wma


Moving /home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/13 Burning Down the House.mp3 to /home/moorepants/music-src/wma_copies/Talking Heads/The Best of Talking Heads [Sire Records]/13 Burning Down the House.mp3
beet list path:"/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/13 Burning Down the House.wma"
path:/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/13 Burning Down the House.wma


Moving /home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/01 Love → Building on Fire.mp3 to /home/moorepants/music-src/wma_copies/Talking Heads/The Best of Talking Heads [Sire Records]/01 Love → Building on Fire.mp3
beet list path:"/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/01 Love → Building on Fire.wma"
path:/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/01 Love → Building on Fire.wma


Moving /home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/15 And She Was.mp3 to /home/moorepants/music-src/wma_copies/Talking Heads/The Best of Talking Heads [Sire Records]/15 And She Was.mp3
beet list path:"/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/15 And She Was.wma"
path:/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/15 And She Was.wma


Moving /home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/14 Road to Nowhere.mp3 to /home/moorepants/music-src/wma_copies/Talking Heads/The Best of Talking Heads [Sire Records]/14 Road to Nowhere.mp3
beet list path:"/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/14 Road to Nowhere.wma"
path:/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/14 Road to Nowhere.wma


Moving /home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/02 Psycho Killer.mp3 to /home/moorepants/music-src/wma_copies/Talking Heads/The Best of Talking Heads [Sire Records]/02 Psycho Killer.mp3
beet list path:"/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/02 Psycho Killer.wma"
path:/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/02 Psycho Killer.wma


Moving /home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/07 Heaven.mp3 to /home/moorepants/music-src/wma_copies/Talking Heads/The Best of Talking Heads [Sire Records]/07 Heaven.mp3
beet list path:"/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/07 Heaven.wma"
path:/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/07 Heaven.wma


Moving /home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/16 Wild Wild Life.mp3 to /home/moorepants/music-src/wma_copies/Talking Heads/The Best of Talking Heads [Sire Records]/16 Wild Wild Life.mp3
beet list path:"/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/16 Wild Wild Life.wma"
path:/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/16 Wild Wild Life.wma


Moving /home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/04 Take Me to the River.mp3 to /home/moorepants/music-src/wma_copies/Talking Heads/The Best of Talking Heads [Sire Records]/04 Take Me to the River.mp3
beet list path:"/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/04 Take Me to the River.wma"
path:/home/moorepants/Music/Talking Heads/The Best of Talking Heads [Sire Records]/04 Take Me to the River.wma


Moving /home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/10 Track 10.mp3 to /home/moorepants/music-src/wma_copies/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/10 Track 10.mp3
beet list path:"/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/10 Track 10.wma"
path:/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/10 Track 10.wma


Moving /home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/04 Track 4.mp3 to /home/moorepants/music-src/wma_copies/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/04 Track 4.mp3
beet list path:"/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/04 Track 4.wma"
path:/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/04 Track 4.wma


Moving /home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/12 Track 12.mp3 to /home/moorepants/music-src/wma_copies/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/12 Track 12.mp3
beet list path:"/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/12 Track 12.wma"
path:/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/12 Track 12.wma


Moving /home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/08 Track 8.mp3 to /home/moorepants/music-src/wma_copies/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/08 Track 8.mp3
beet list path:"/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/08 Track 8.wma"
path:/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/08 Track 8.wma


Moving /home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/06 Track 6.mp3 to /home/moorepants/music-src/wma_copies/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/06 Track 6.mp3
beet list path:"/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/06 Track 6.wma"
path:/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/06 Track 6.wma


Moving /home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/11 Track 11.mp3 to /home/moorepants/music-src/wma_copies/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/11 Track 11.mp3
beet list path:"/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/11 Track 11.wma"
path:/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/11 Track 11.wma


Moving /home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/05 Track 5.mp3 to /home/moorepants/music-src/wma_copies/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/05 Track 5.mp3
beet list path:"/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/05 Track 5.wma"
path:/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/05 Track 5.wma


Moving /home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/03 Track 3.mp3 to /home/moorepants/music-src/wma_copies/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/03 Track 3.mp3
beet list path:"/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/03 Track 3.wma"
path:/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/03 Track 3.wma


Moving /home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/01 Track 1.mp3 to /home/moorepants/music-src/wma_copies/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/01 Track 1.mp3
beet list path:"/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/01 Track 1.wma"
path:/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/01 Track 1.wma


Moving /home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/07 Track 7.mp3 to /home/moorepants/music-src/wma_copies/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/07 Track 7.mp3
beet list path:"/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/07 Track 7.wma"
path:/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/07 Track 7.wma


Moving /home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/09 Track 9.mp3 to /home/moorepants/music-src/wma_copies/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/09 Track 9.mp3
beet list path:"/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/09 Track 9.wma"
path:/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/09 Track 9.wma


Moving /home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/13 Track 13.mp3 to /home/moorepants/music-src/wma_copies/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/13 Track 13.mp3
beet list path:"/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/13 Track 13.wma"
path:/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/13 Track 13.wma


Moving /home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/02 Track 2.mp3 to /home/moorepants/music-src/wma_copies/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/02 Track 2.mp3
beet list path:"/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/02 Track 2.wma"
path:/home/moorepants/Music/Axlerod Carrey and Foss/SF Jug Band festival and rehersals/02 Track 2.wma


Moving /home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/09 Come Back Jonee.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/09 Come Back Jonee.mp3
beet list path:"/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/09 Come Back Jonee.wma"
path:/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/09 Come Back Jonee.wma


Moving /home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/10 Sloppy (I Saw My Baby Gettin’).mp3 to /home/moorepants/music-src/wma_copies/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/10 Sloppy (I Saw My Baby Gettin’).mp3
beet list path:"/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/10 Sloppy (I Saw My Baby Gettin’).wma"
path:/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/10 Sloppy (I Saw My Baby Gettin’).wma


Moving /home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/03 Praying Hands.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/03 Praying Hands.mp3
beet list path:"/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/03 Praying Hands.wma"
path:/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/03 Praying Hands.wma


Moving /home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/02 (I Can’t Get No) Satisfaction.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/02 (I Can’t Get No) Satisfaction.mp3
beet list path:"/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/02 (I Can’t Get No) Satisfaction.wma"
path:/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/02 (I Can’t Get No) Satisfaction.wma


Moving /home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/05 Mongoloid.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/05 Mongoloid.mp3
beet list path:"/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/05 Mongoloid.wma"
path:/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/05 Mongoloid.wma


Moving /home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/06 Jocko Homo.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/06 Jocko Homo.mp3
beet list path:"/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/06 Jocko Homo.wma"
path:/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/06 Jocko Homo.wma


Moving /home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/07 Too Much Paranoias.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/07 Too Much Paranoias.mp3
beet list path:"/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/07 Too Much Paranoias.wma"
path:/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/07 Too Much Paranoias.wma


Moving /home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/04 Space Junk.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/04 Space Junk.mp3
beet list path:"/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/04 Space Junk.wma"
path:/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/04 Space Junk.wma


Moving /home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/08 Gut Feeling _ (Slap Your Mammy).mp3 to /home/moorepants/music-src/wma_copies/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/08 Gut Feeling _ (Slap Your Mammy).mp3
beet list path:"/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/08 Gut Feeling _ (Slap Your Mammy).wma"
path:/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/08 Gut Feeling _ (Slap Your Mammy).wma


Moving /home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/11 Shrivel‐Up.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/11 Shrivel‐Up.mp3
beet list path:"/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/11 Shrivel‐Up.wma"
path:/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/11 Shrivel‐Up.wma


Moving /home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/01 Uncontrollable Urge.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/01 Uncontrollable Urge.mp3
beet list path:"/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/01 Uncontrollable Urge.wma"
path:/home/moorepants/Music/DEVO/Q_ Are We Not Men_ A_ We Are Devo! [M5 3239]/01 Uncontrollable Urge.wma


Moving /home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/05 Jerkin' Back 'n' Forth.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Greatest Hits [9 26449-2]/05 Jerkin' Back 'n' Forth.mp3
beet list path:"/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/05 Jerkin' Back 'n' Forth.wma"
path:/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/05 Jerkin' Back 'n' Forth.wma


Moving /home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/02 Through Being Cool.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Greatest Hits [9 26449-2]/02 Through Being Cool.mp3
beet list path:"/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/02 Through Being Cool.wma"
path:/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/02 Through Being Cool.wma


Moving /home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/08 (I Can't Get No) Satisfaction.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Greatest Hits [9 26449-2]/08 (I Can't Get No) Satisfaction.mp3
beet list path:"/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/08 (I Can't Get No) Satisfaction.wma"
path:/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/08 (I Can't Get No) Satisfaction.wma


Moving /home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/12 Smart Patrol _ Mr. DNA.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Greatest Hits [9 26449-2]/12 Smart Patrol _ Mr. DNA.mp3
beet list path:"/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/12 Smart Patrol _ Mr. DNA.wma"
path:/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/12 Smart Patrol _ Mr. DNA.wma


Moving /home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/06 Peek-a-Boo!.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Greatest Hits [9 26449-2]/06 Peek-a-Boo!.mp3
beet list path:"/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/06 Peek-a-Boo!.wma"
path:/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/06 Peek-a-Boo!.wma


Moving /home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/13 Gut Feeling.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Greatest Hits [9 26449-2]/13 Gut Feeling.mp3
beet list path:"/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/13 Gut Feeling.wma"
path:/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/13 Gut Feeling.wma


Moving /home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/04 That's Good.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Greatest Hits [9 26449-2]/04 That's Good.mp3
beet list path:"/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/04 That's Good.wma"
path:/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/04 That's Good.wma


Moving /home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/09 Whip It.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Greatest Hits [9 26449-2]/09 Whip It.mp3
beet list path:"/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/09 Whip It.wma"
path:/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/09 Whip It.wma


Moving /home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/14 Gates of Steel.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Greatest Hits [9 26449-2]/14 Gates of Steel.mp3
beet list path:"/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/14 Gates of Steel.wma"
path:/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/14 Gates of Steel.wma


Moving /home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/10 Girl U Want.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Greatest Hits [9 26449-2]/10 Girl U Want.mp3
beet list path:"/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/10 Girl U Want.wma"
path:/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/10 Girl U Want.wma


Moving /home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/01 Here to Go (Go mix version).mp3 to /home/moorepants/music-src/wma_copies/DEVO/Greatest Hits [9 26449-2]/01 Here to Go (Go mix version).mp3
beet list path:"/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/01 Here to Go (Go mix version).wma"
path:/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/01 Here to Go (Go mix version).wma


Moving /home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/16 Jocko Homo.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Greatest Hits [9 26449-2]/16 Jocko Homo.mp3
beet list path:"/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/16 Jocko Homo.wma"
path:/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/16 Jocko Homo.wma


Moving /home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/15 Working in the Coalmine.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Greatest Hits [9 26449-2]/15 Working in the Coalmine.mp3
beet list path:"/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/15 Working in the Coalmine.wma"
path:/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/15 Working in the Coalmine.wma


Moving /home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/11 Freedom of Choice.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Greatest Hits [9 26449-2]/11 Freedom of Choice.mp3
beet list path:"/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/11 Freedom of Choice.wma"
path:/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/11 Freedom of Choice.wma


Moving /home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/03 Big Mess.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Greatest Hits [9 26449-2]/03 Big Mess.mp3
beet list path:"/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/03 Big Mess.wma"
path:/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/03 Big Mess.wma


Moving /home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/07 Beautiful World.mp3 to /home/moorepants/music-src/wma_copies/DEVO/Greatest Hits [9 26449-2]/07 Beautiful World.mp3
beet list path:"/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/07 Beautiful World.wma"
path:/home/moorepants/Music/DEVO/Greatest Hits [9 26449-2]/07 Beautiful World.wma


Moving /home/moorepants/Music/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/02 One Dime Blues.mp3 to /home/moorepants/music-src/wma_copies/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/02 One Dime Blues.mp3
beet list path:"/home/moorepants/Music/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/02 One Dime Blues.wma"
path:/home/moorepants/Music/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/02 One Dime Blues.wma


Moving /home/moorepants/Music/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/06 Dryland Blues.mp3 to /home/moorepants/music-src/wma_copies/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/06 Dryland Blues.mp3
beet list path:"/home/moorepants/Music/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/06 Dryland Blues.wma"
path:/home/moorepants/Music/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/06 Dryland Blues.wma


Moving /home/moorepants/Music/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/05 Black is the Color of My True Love's Hair.mp3 to /home/moorepants/music-src/wma_copies/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/05 Black is the Color of My True Love's Hair.mp3
beet list path:"/home/moorepants/Music/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/05 Black is the Color of My True Love's Hair.wma"
path:/home/moorepants/Music/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/05 Black is the Color of My True Love's Hair.wma


Moving /home/moorepants/Music/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/03 Freight Train.mp3 to /home/moorepants/music-src/wma_copies/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/03 Freight Train.mp3
beet list path:"/home/moorepants/Music/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/03 Freight Train.wma"
path:/home/moorepants/Music/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/03 Freight Train.wma


Moving /home/moorepants/Music/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/04 One Thin Dime.mp3 to /home/moorepants/music-src/wma_copies/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/04 One Thin Dime.mp3
beet list path:"/home/moorepants/Music/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/04 One Thin Dime.wma"
path:/home/moorepants/Music/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/04 One Thin Dime.wma


Moving /home/moorepants/Music/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/01 All the Pretty Horses.mp3 to /home/moorepants/music-src/wma_copies/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/01 All the Pretty Horses.mp3
beet list path:"/home/moorepants/Music/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/01 All the Pretty Horses.wma"
path:/home/moorepants/Music/Laura Gibson/Six White Horses_ Blues & Traditionals, Volume 1/01 All the Pretty Horses.wma


Moving /home/moorepants/Music/Laura Gibson/If You Come to Greet Me/03 Nightwatch.mp3 to /home/moorepants/music-src/wma_copies/Laura Gibson/If You Come to Greet Me/03 Nightwatch.mp3
beet list path:"/home/moorepants/Music/Laura Gibson/If You Come to Greet Me/03 Nightwatch.wma"
path:/home/moorepants/Music/Laura Gibson/If You Come to Greet Me/03 Nightwatch.wma


Moving /home/moorepants/Music/Laura Gibson/If You Come to Greet Me/09 The Longest Day.mp3 to /home/moorepants/music-src/wma_copies/Laura Gibson/If You Come to Greet Me/09 The Longest Day.mp3
beet list path:"/home/moorepants/Music/Laura Gibson/If You Come to Greet Me/09 The Longest Day.wma"
path:/home/moorepants/Music/Laura Gibson/If You Come to Greet Me/09 The Longest Day.wma


Moving /home/moorepants/Music/Laura Gibson/If You Come to Greet Me/06 Small Town Parade.mp3 to /home/moorepants/music-src/wma_copies/Laura Gibson/If You Come to Greet Me/06 Small Town Parade.mp3
beet list path:"/home/moorepants/Music/Laura Gibson/If You Come to Greet Me/0
"""
