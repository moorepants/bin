"""
1. Remove files older than 30 days from filesystem and record the filenames.
2. Search for those file names in the xml.
3. Remove location tag and change mountpoint tag to location.
4. Change status tag to 103
"""
import os
import time
from xml.etree import ElementTree
from shutil import copyfile
import io
import contextlib
import codecs


def lower_first(s):
    return s[:1].lower() + s[1:] if s else ''


def html_replace(exc):
    if isinstance(exc, (UnicodeEncodeError, UnicodeTranslateError)):
        s = []
        for c in exc.object[exc.start:exc.end]:
            s.append('&#%s;' % lower_first(hex(ord(c))[1:].upper()))
        return ''.join(s), exc.end
    else:
        raise TypeError("can't handle %s" % exc.__name__)
codecs.register_error('html_replace', html_replace)


# monkey patch this python function to prevent it from using xmlcharrefreplace
@contextlib.contextmanager
def _get_writer(file_or_filename, encoding):
    # returns text write method and release all resources after using
    try:
        write = file_or_filename.write
    except AttributeError:
        # file_or_filename is a file name
        if encoding == "unicode":
            file = open(file_or_filename, "w")
        else:
            file = open(file_or_filename, "w", encoding=encoding,
                        errors="xmlcharrefreplace")
        with file:
            yield file.write
    else:
        # file_or_filename is a file-like object
        # encoding determines if it is a text or binary writer
        if encoding == "unicode":
            # use a text writer as is
            yield write
        else:
            # wrap a binary writer with TextIOWrapper
            with contextlib.ExitStack() as stack:
                if isinstance(file_or_filename, io.BufferedIOBase):
                    file = file_or_filename
                elif isinstance(file_or_filename, io.RawIOBase):
                    file = io.BufferedWriter(file_or_filename)
                    # Keep the original file open when the BufferedWriter is
                    # destroyed
                    stack.callback(file.detach)
                else:
                    # This is to handle passed objects that aren't in the
                    # IOBase hierarchy, but just have a write method
                    file = io.BufferedIOBase()
                    file.writable = lambda: True
                    file.write = write
                    try:
                        # TextIOWrapper uses this methods to determine
                        # if BOM (for UTF-16, etc) should be added
                        file.seekable = file_or_filename.seekable
                        file.tell = file_or_filename.tell
                    except AttributeError:
                        pass
                file = io.TextIOWrapper(file,
                                        encoding=encoding,
                                        errors='html_replace',
                                        #errors='backslashreplace',
                                        #errors="surrogateescape",
                                        #errors="xmlcharrefreplace",
                                        newline="\n")
                # Keep the original file open when the TextIOWrapper is
                # destroyed
                stack.callback(file.detach)
                yield file.write

ElementTree._get_writer = _get_writer


copyfile('/home/moorepants/.local/share/rhythmbox/rhythmdb.xml',
         '/home/moorepants/Desktop/rhythmdb.xml')

PODCASTS_PATH = "/home/moorepants/Podcasts"

now = time.time()

filenames = []

for dirpath, dirnames, filepaths in os.walk(PODCASTS_PATH):
    for f in filepaths:
        path_to_file = os.path.join(dirpath, f)
        # 30 days old
        if os.stat(path_to_file).st_mtime < now - 30 * 86400:
            if os.path.isfile(path_to_file):
                filenames.append(f)
                print(path_to_file)
                #os.remove(path_to_file)

et = ElementTree.parse('/home/moorepants/Desktop/rhythmdb.xml')

podcast_entries = [n for n in et.findall('entry')
                   if n.attrib['type'] == 'podcast-post']

deleted_entries = []
for f in filenames:
    for n in podcast_entries:
        status_tag = n.find('status')
        location_tag = n.find('location')
        if (status_tag.text == '100' and f in location_tag.text):
            deleted_entries.append(n)

for entry in deleted_entries:
    location_tag = entry.find('location')
    entry.remove(location_tag)
    mountpoint_tag = entry.find('mountpoint')
    mountpoint_tag.tag = 'location'
    status_tag = entry.find('status')
    status_tag.text = '103'

# TODO : Figure out how to deal with the fact that hex code points are changed
# to decimal code points.
with open('/home/moorepants/Desktop/rhythmdb-modified.xml', 'wb') as f:
    et.write(f, short_empty_elements=False, xml_declaration=False,
             encoding='ascii', method='html')

#with open('/home/moorepants/Desktop/rhythmdb-modified.xml', 'r') as f:
    #text = f.read()
#
#text = text.replace(r'\r', r'&#13;')
#
#with open('/home/moorepants/Desktop/rhythmdb-modified.xml', 'w') as f:
    #f.write(text)
