"""Wrapper for wgfmu.h

Generated with:
/home/ganeshgore/.local/bin/ctypesgen wgfmu.h -o wgfmupylib.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python v(3, 2)

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64, )
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types


class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1:]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1:]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, Union):

    _fields_ = [("raw", POINTER(c_char)), ("data", c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from c_char array
        elif isinstance(obj, c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_,
                                              bytes) and type._type_ != "P":
        return type
    else:
        return c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util


def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []


class LibraryLoader(object):
    def __init__(self):
        self.other_dirs = []

    def load_library(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self, path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == "darwin":
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError as e:
            raise ImportError(e)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # FIXME / TODO return '.' and os.path.dirname(__file__)
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path:
                yield path

    def getplatformpaths(self, libname):
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir, name)

    def getdirs(self, libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path(
            "DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"), "/usr/local/lib", "/usr/lib"
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")
        dirs.append(os.path.dirname(__file__))

        if hasattr(sys, "frozen") and sys.frozen == "macosx_app":
            dirs.append(
                os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in (
                "LD_LIBRARY_PATH",
                "SHLIB_PATH",  # HPUX
                "LIBPATH",  # OS/2, AIX
                "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")
        directories.append(os.path.dirname(__file__))

        try:
            with open("/etc/ld.so.conf") as f:
                directories.extend([dir.strip() for dir in f])
        except IOError:
            pass

        unix_lib_dirs_list = ["/lib", "/usr/lib", "/lib64", "/usr/lib64"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            bitage = platform.architecture()[0]
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += [
                    "/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"
                ]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu", "/usr/lib/x86_64-linux-gnu"
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        ext_re = re.compile(r"\.s[ol]$")
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result:
            yield result

        path = ctypes.util.find_library(libname)
        if path:
            yield os.path.join("/lib", path)


# Windows


class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try:
            return getattr(self.cdll, name)
        except AttributeError:
            try:
                return getattr(self.windll, name)
            except AttributeError:
                raise


class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for F in other_dirs:
        if not os.path.isabs(F):
            F = os.path.abspath(F)
        loader.other_dirs.append(F)


load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# No libraries

_lib = "WGFMU"
# _libs["WGFMU"] = load_library("C:\\Windows\\SysWOW64\\wgfmu")
_libs["WGFMU"] = WinDLL("C:\\Windows\\SysWOW64\\wgfmu")

# No modules

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 128
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_openSession'):
        continue
    WGFMU_openSession = _lib.WGFMU_openSession
    WGFMU_openSession.argtypes = [c_char_p]
    WGFMU_openSession.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 129
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_closeSession'):
        continue
    WGFMU_closeSession = _lib.WGFMU_closeSession
    WGFMU_closeSession.argtypes = []
    WGFMU_closeSession.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 130
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_initialize'):
        continue
    WGFMU_initialize = _lib.WGFMU_initialize
    WGFMU_initialize.argtypes = []
    WGFMU_initialize.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 131
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_setTimeout'):
        continue
    WGFMU_setTimeout = _lib.WGFMU_setTimeout
    WGFMU_setTimeout.argtypes = [c_double]
    WGFMU_setTimeout.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 132
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_doSelfCalibration'):
        continue
    WGFMU_doSelfCalibration = _lib.WGFMU_doSelfCalibration
    WGFMU_doSelfCalibration.argtypes = [POINTER(c_int), String, POINTER(c_int)]
    WGFMU_doSelfCalibration.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 133
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_doSelfTest'):
        continue
    WGFMU_doSelfTest = _lib.WGFMU_doSelfTest
    WGFMU_doSelfTest.argtypes = [POINTER(c_int), String, POINTER(c_int)]
    WGFMU_doSelfTest.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 134
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getChannelIdSize'):
        continue
    WGFMU_getChannelIdSize = _lib.WGFMU_getChannelIdSize
    WGFMU_getChannelIdSize.argtypes = [POINTER(c_int)]
    WGFMU_getChannelIdSize.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 135
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getChannelIds'):
        continue
    WGFMU_getChannelIds = _lib.WGFMU_getChannelIds
    WGFMU_getChannelIds.argtypes = [POINTER(c_int), POINTER(c_int)]
    WGFMU_getChannelIds.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 139
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getErrorSize'):
        continue
    WGFMU_getErrorSize = _lib.WGFMU_getErrorSize
    WGFMU_getErrorSize.argtypes = [POINTER(c_int)]
    WGFMU_getErrorSize.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 140
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getError'):
        continue
    WGFMU_getError = _lib.WGFMU_getError
    WGFMU_getError.argtypes = [String, POINTER(c_int)]
    WGFMU_getError.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 141
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getErrorSummarySize'):
        continue
    WGFMU_getErrorSummarySize = _lib.WGFMU_getErrorSummarySize
    WGFMU_getErrorSummarySize.argtypes = [POINTER(c_int)]
    WGFMU_getErrorSummarySize.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 142
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getErrorSummary'):
        continue
    WGFMU_getErrorSummary = _lib.WGFMU_getErrorSummary
    WGFMU_getErrorSummary.argtypes = [String, POINTER(c_int)]
    WGFMU_getErrorSummary.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 143
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_treatWarningsAsErrors'):
        continue
    WGFMU_treatWarningsAsErrors = _lib.WGFMU_treatWarningsAsErrors
    WGFMU_treatWarningsAsErrors.argtypes = [c_int]
    WGFMU_treatWarningsAsErrors.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 144
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_setWarningLevel'):
        continue
    WGFMU_setWarningLevel = _lib.WGFMU_setWarningLevel
    WGFMU_setWarningLevel.argtypes = [c_int]
    WGFMU_setWarningLevel.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 145
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getWarningLevel'):
        continue
    WGFMU_getWarningLevel = _lib.WGFMU_getWarningLevel
    WGFMU_getWarningLevel.argtypes = [POINTER(c_int)]
    WGFMU_getWarningLevel.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 146
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getWarningSummarySize'):
        continue
    WGFMU_getWarningSummarySize = _lib.WGFMU_getWarningSummarySize
    WGFMU_getWarningSummarySize.argtypes = [POINTER(c_int)]
    WGFMU_getWarningSummarySize.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 147
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getWarningSummary'):
        continue
    WGFMU_getWarningSummary = _lib.WGFMU_getWarningSummary
    WGFMU_getWarningSummary.argtypes = [String, POINTER(c_int)]
    WGFMU_getWarningSummary.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 148
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_openLogFile'):
        continue
    WGFMU_openLogFile = _lib.WGFMU_openLogFile
    WGFMU_openLogFile.argtypes = [String]
    WGFMU_openLogFile.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 149
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_closeLogFile'):
        continue
    WGFMU_closeLogFile = _lib.WGFMU_closeLogFile
    WGFMU_closeLogFile.argtypes = []
    WGFMU_closeLogFile.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 153
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_setOperationMode'):
        continue
    WGFMU_setOperationMode = _lib.WGFMU_setOperationMode
    WGFMU_setOperationMode.argtypes = [c_int, c_int]
    WGFMU_setOperationMode.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 154
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getOperationMode'):
        continue
    WGFMU_getOperationMode = _lib.WGFMU_getOperationMode
    WGFMU_getOperationMode.argtypes = [c_int, POINTER(c_int)]
    WGFMU_getOperationMode.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 155
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_setForceVoltageRange'):
        continue
    WGFMU_setForceVoltageRange = _lib.WGFMU_setForceVoltageRange
    WGFMU_setForceVoltageRange.argtypes = [c_int, c_int]
    WGFMU_setForceVoltageRange.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 156
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getForceVoltageRange'):
        continue
    WGFMU_getForceVoltageRange = _lib.WGFMU_getForceVoltageRange
    WGFMU_getForceVoltageRange.argtypes = [c_int, POINTER(c_int)]
    WGFMU_getForceVoltageRange.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 157
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_setMeasureMode'):
        continue
    WGFMU_setMeasureMode = _lib.WGFMU_setMeasureMode
    WGFMU_setMeasureMode.argtypes = [c_int, c_int]
    WGFMU_setMeasureMode.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 158
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getMeasureMode'):
        continue
    WGFMU_getMeasureMode = _lib.WGFMU_getMeasureMode
    WGFMU_getMeasureMode.argtypes = [c_int, POINTER(c_int)]
    WGFMU_getMeasureMode.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 159
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_setMeasureVoltageRange'):
        continue
    WGFMU_setMeasureVoltageRange = _lib.WGFMU_setMeasureVoltageRange
    WGFMU_setMeasureVoltageRange.argtypes = [c_int, c_int]
    WGFMU_setMeasureVoltageRange.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 160
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getMeasureVoltageRange'):
        continue
    WGFMU_getMeasureVoltageRange = _lib.WGFMU_getMeasureVoltageRange
    WGFMU_getMeasureVoltageRange.argtypes = [c_int, POINTER(c_int)]
    WGFMU_getMeasureVoltageRange.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 161
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_setMeasureCurrentRange'):
        continue
    WGFMU_setMeasureCurrentRange = _lib.WGFMU_setMeasureCurrentRange
    WGFMU_setMeasureCurrentRange.argtypes = [c_int, c_int]
    WGFMU_setMeasureCurrentRange.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 162
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getMeasureCurrentRange'):
        continue
    WGFMU_getMeasureCurrentRange = _lib.WGFMU_getMeasureCurrentRange
    WGFMU_getMeasureCurrentRange.argtypes = [c_int, POINTER(c_int)]
    WGFMU_getMeasureCurrentRange.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 163
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_setForceDelay'):
        continue
    WGFMU_setForceDelay = _lib.WGFMU_setForceDelay
    WGFMU_setForceDelay.argtypes = [c_int, c_double]
    WGFMU_setForceDelay.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 164
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getForceDelay'):
        continue
    WGFMU_getForceDelay = _lib.WGFMU_getForceDelay
    WGFMU_getForceDelay.argtypes = [c_int, POINTER(c_double)]
    WGFMU_getForceDelay.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 165
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_setMeasureDelay'):
        continue
    WGFMU_setMeasureDelay = _lib.WGFMU_setMeasureDelay
    WGFMU_setMeasureDelay.argtypes = [c_int, c_double]
    WGFMU_setMeasureDelay.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 166
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getMeasureDelay'):
        continue
    WGFMU_getMeasureDelay = _lib.WGFMU_getMeasureDelay
    WGFMU_getMeasureDelay.argtypes = [c_int, POINTER(c_double)]
    WGFMU_getMeasureDelay.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 167
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_setMeasureEnabled'):
        continue
    WGFMU_setMeasureEnabled = _lib.WGFMU_setMeasureEnabled
    WGFMU_setMeasureEnabled.argtypes = [c_int, c_int]
    WGFMU_setMeasureEnabled.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 168
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_isMeasureEnabled'):
        continue
    WGFMU_isMeasureEnabled = _lib.WGFMU_isMeasureEnabled
    WGFMU_isMeasureEnabled.argtypes = [c_int, POINTER(c_int)]
    WGFMU_isMeasureEnabled.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 169
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_setTriggerOutMode'):
        continue
    WGFMU_setTriggerOutMode = _lib.WGFMU_setTriggerOutMode
    WGFMU_setTriggerOutMode.argtypes = [c_int, c_int, c_int]
    WGFMU_setTriggerOutMode.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 170
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getTriggerOutMode'):
        continue
    WGFMU_getTriggerOutMode = _lib.WGFMU_getTriggerOutMode
    WGFMU_getTriggerOutMode.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]
    WGFMU_getTriggerOutMode.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 174
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_connect'):
        continue
    WGFMU_connect = _lib.WGFMU_connect
    WGFMU_connect.argtypes = [c_int]
    WGFMU_connect.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 175
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_disconnect'):
        continue
    WGFMU_disconnect = _lib.WGFMU_disconnect
    WGFMU_disconnect.argtypes = [c_int]
    WGFMU_disconnect.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 179
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_clear'):
        continue
    WGFMU_clear = _lib.WGFMU_clear
    WGFMU_clear.argtypes = []
    WGFMU_clear.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 183
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_createPattern'):
        continue
    WGFMU_createPattern = _lib.WGFMU_createPattern
    WGFMU_createPattern.argtypes = [String, c_double]
    WGFMU_createPattern.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 184
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_addVector'):
        continue
    WGFMU_addVector = _lib.WGFMU_addVector
    WGFMU_addVector.argtypes = [String, c_double, c_double]
    WGFMU_addVector.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 185
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_addVectors'):
        continue
    WGFMU_addVectors = _lib.WGFMU_addVectors
    WGFMU_addVectors.argtypes = [
        String, POINTER(c_double),
        POINTER(c_double), c_int
    ]
    WGFMU_addVectors.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 186
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_setVector'):
        continue
    WGFMU_setVector = _lib.WGFMU_setVector
    WGFMU_setVector.argtypes = [String, c_double, c_double]
    WGFMU_setVector.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 187
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_setVectors'):
        continue
    WGFMU_setVectors = _lib.WGFMU_setVectors
    WGFMU_setVectors.argtypes = [
        String, POINTER(c_double),
        POINTER(c_double), c_int
    ]
    WGFMU_setVectors.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 191
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_createMergedPattern'):
        continue
    WGFMU_createMergedPattern = _lib.WGFMU_createMergedPattern
    WGFMU_createMergedPattern.argtypes = [String, String, String, c_int]
    WGFMU_createMergedPattern.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 192
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_createMultipliedPattern'):
        continue
    WGFMU_createMultipliedPattern = _lib.WGFMU_createMultipliedPattern
    WGFMU_createMultipliedPattern.argtypes = [
        String, String, c_double, c_double
    ]
    WGFMU_createMultipliedPattern.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 193
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_createOffsetPattern'):
        continue
    WGFMU_createOffsetPattern = _lib.WGFMU_createOffsetPattern
    WGFMU_createOffsetPattern.argtypes = [String, String, c_double, c_double]
    WGFMU_createOffsetPattern.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 197
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_setMeasureEvent'):
        continue
    WGFMU_setMeasureEvent = _lib.WGFMU_setMeasureEvent
    WGFMU_setMeasureEvent.argtypes = [
        String, String, c_double, c_int, c_double, c_double, c_int
    ]
    WGFMU_setMeasureEvent.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 198
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_setRangeEvent'):
        continue
    WGFMU_setRangeEvent = _lib.WGFMU_setRangeEvent
    WGFMU_setRangeEvent.argtypes = [String, String, c_double, c_int]
    WGFMU_setRangeEvent.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 199
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_setTriggerOutEvent'):
        continue
    WGFMU_setTriggerOutEvent = _lib.WGFMU_setTriggerOutEvent
    WGFMU_setTriggerOutEvent.argtypes = [String, String, c_double, c_double]
    WGFMU_setTriggerOutEvent.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 203
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_addSequence'):
        continue
    WGFMU_addSequence = _lib.WGFMU_addSequence
    WGFMU_addSequence.argtypes = [c_int, String, c_double]
    WGFMU_addSequence.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 204
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_addSequences'):
        continue
    WGFMU_addSequences = _lib.WGFMU_addSequences
    WGFMU_addSequences.argtypes = [
        c_int, POINTER(POINTER(c_char)),
        POINTER(c_double), c_int
    ]
    WGFMU_addSequences.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 208
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getPatternForceValueSize'):
        continue
    WGFMU_getPatternForceValueSize = _lib.WGFMU_getPatternForceValueSize
    WGFMU_getPatternForceValueSize.argtypes = [String, POINTER(c_int)]
    WGFMU_getPatternForceValueSize.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 209
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getPatternForceValues'):
        continue
    WGFMU_getPatternForceValues = _lib.WGFMU_getPatternForceValues
    WGFMU_getPatternForceValues.argtypes = [
        String, c_int,
        POINTER(c_int),
        POINTER(c_double),
        POINTER(c_double)
    ]
    WGFMU_getPatternForceValues.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 210
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getPatternForceValue'):
        continue
    WGFMU_getPatternForceValue = _lib.WGFMU_getPatternForceValue
    WGFMU_getPatternForceValue.argtypes = [
        String, c_int, POINTER(c_double),
        POINTER(c_double)
    ]
    WGFMU_getPatternForceValue.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 211
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getPatternInterpolatedForceValue'):
        continue
    WGFMU_getPatternInterpolatedForceValue = _lib.WGFMU_getPatternInterpolatedForceValue
    WGFMU_getPatternInterpolatedForceValue.argtypes = [
        String, c_double, POINTER(c_double)
    ]
    WGFMU_getPatternInterpolatedForceValue.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 212
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getPatternMeasureTimeSize'):
        continue
    WGFMU_getPatternMeasureTimeSize = _lib.WGFMU_getPatternMeasureTimeSize
    WGFMU_getPatternMeasureTimeSize.argtypes = [String, POINTER(c_int)]
    WGFMU_getPatternMeasureTimeSize.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 213
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getPatternMeasureTimes'):
        continue
    WGFMU_getPatternMeasureTimes = _lib.WGFMU_getPatternMeasureTimes
    WGFMU_getPatternMeasureTimes.argtypes = [
        String, c_int, POINTER(c_int),
        POINTER(c_double)
    ]
    WGFMU_getPatternMeasureTimes.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 214
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getPatternMeasureTime'):
        continue
    WGFMU_getPatternMeasureTime = _lib.WGFMU_getPatternMeasureTime
    WGFMU_getPatternMeasureTime.argtypes = [String, c_int, POINTER(c_double)]
    WGFMU_getPatternMeasureTime.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 218
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getForceValueSize'):
        continue
    WGFMU_getForceValueSize = _lib.WGFMU_getForceValueSize
    WGFMU_getForceValueSize.argtypes = [c_int, POINTER(c_double)]
    WGFMU_getForceValueSize.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 219
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getForceValues'):
        continue
    WGFMU_getForceValues = _lib.WGFMU_getForceValues
    WGFMU_getForceValues.argtypes = [
        c_int, c_double,
        POINTER(c_int),
        POINTER(c_double),
        POINTER(c_double)
    ]
    WGFMU_getForceValues.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 220
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getForceValue'):
        continue
    WGFMU_getForceValue = _lib.WGFMU_getForceValue
    WGFMU_getForceValue.argtypes = [
        c_int, c_double, POINTER(c_double),
        POINTER(c_double)
    ]
    WGFMU_getForceValue.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 221
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getInterpolatedForceValue'):
        continue
    WGFMU_getInterpolatedForceValue = _lib.WGFMU_getInterpolatedForceValue
    WGFMU_getInterpolatedForceValue.argtypes = [
        c_int, c_double, POINTER(c_double)
    ]
    WGFMU_getInterpolatedForceValue.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 222
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getMeasureTimeSize'):
        continue
    WGFMU_getMeasureTimeSize = _lib.WGFMU_getMeasureTimeSize
    WGFMU_getMeasureTimeSize.argtypes = [c_int, POINTER(c_int)]
    WGFMU_getMeasureTimeSize.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 223
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getMeasureTimes'):
        continue
    WGFMU_getMeasureTimes = _lib.WGFMU_getMeasureTimes
    WGFMU_getMeasureTimes.argtypes = [
        c_int, c_int, POINTER(c_int),
        POINTER(c_double)
    ]
    WGFMU_getMeasureTimes.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 224
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getMeasureTime'):
        continue
    WGFMU_getMeasureTime = _lib.WGFMU_getMeasureTime
    WGFMU_getMeasureTime.argtypes = [c_int, c_int, POINTER(c_double)]
    WGFMU_getMeasureTime.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 228
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getMeasureEventSize'):
        continue
    WGFMU_getMeasureEventSize = _lib.WGFMU_getMeasureEventSize
    WGFMU_getMeasureEventSize.argtypes = [c_int, POINTER(c_int)]
    WGFMU_getMeasureEventSize.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 229
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getMeasureEvents'):
        continue
    WGFMU_getMeasureEvents = _lib.WGFMU_getMeasureEvents
    WGFMU_getMeasureEvents.argtypes = [
        c_int, c_int,
        POINTER(c_int),
        POINTER(POINTER(c_char)),
        POINTER(POINTER(c_char)),
        POINTER(c_int),
        POINTER(c_double),
        POINTER(c_int),
        POINTER(c_int),
        POINTER(c_int)
    ]
    WGFMU_getMeasureEvents.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 230
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getMeasureEvent'):
        continue
    WGFMU_getMeasureEvent = _lib.WGFMU_getMeasureEvent
    WGFMU_getMeasureEvent.argtypes = [
        c_int, c_int, String, String,
        POINTER(c_int),
        POINTER(c_double),
        POINTER(c_int),
        POINTER(c_int),
        POINTER(c_int)
    ]
    WGFMU_getMeasureEvent.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 231
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getMeasureEventAttribute'):
        continue
    WGFMU_getMeasureEventAttribute = _lib.WGFMU_getMeasureEventAttribute
    WGFMU_getMeasureEventAttribute.argtypes = [
        c_int, c_int,
        POINTER(c_double),
        POINTER(c_int),
        POINTER(c_double),
        POINTER(c_double),
        POINTER(c_int)
    ]
    WGFMU_getMeasureEventAttribute.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 235
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_exportAscii'):
        continue
    WGFMU_exportAscii = _lib.WGFMU_exportAscii
    WGFMU_exportAscii.argtypes = [String]
    WGFMU_exportAscii.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 239
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_update'):
        continue
    WGFMU_update = _lib.WGFMU_update
    WGFMU_update.argtypes = []
    WGFMU_update.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 240
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_updateChannel'):
        continue
    WGFMU_updateChannel = _lib.WGFMU_updateChannel
    WGFMU_updateChannel.argtypes = [c_int]
    WGFMU_updateChannel.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 241
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_execute'):
        continue
    WGFMU_execute = _lib.WGFMU_execute
    WGFMU_execute.argtypes = []
    WGFMU_execute.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 242
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_abort'):
        continue
    WGFMU_abort = _lib.WGFMU_abort
    WGFMU_abort.argtypes = []
    WGFMU_abort.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 243
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_abortChannel'):
        continue
    WGFMU_abortChannel = _lib.WGFMU_abortChannel
    WGFMU_abortChannel.argtypes = [c_int]
    WGFMU_abortChannel.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 244
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getStatus'):
        continue
    WGFMU_getStatus = _lib.WGFMU_getStatus
    WGFMU_getStatus.argtypes = [
        POINTER(c_int), POINTER(c_double),
        POINTER(c_double)
    ]
    WGFMU_getStatus.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 245
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getChannelStatus'):
        continue
    WGFMU_getChannelStatus = _lib.WGFMU_getChannelStatus
    WGFMU_getChannelStatus.argtypes = [
        c_int, POINTER(c_int),
        POINTER(c_double),
        POINTER(c_double)
    ]
    WGFMU_getChannelStatus.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 246
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_waitUntilCompleted'):
        continue
    WGFMU_waitUntilCompleted = _lib.WGFMU_waitUntilCompleted
    WGFMU_waitUntilCompleted.argtypes = []
    WGFMU_waitUntilCompleted.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 250
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getMeasureValueSize'):
        continue
    WGFMU_getMeasureValueSize = _lib.WGFMU_getMeasureValueSize
    WGFMU_getMeasureValueSize.argtypes = [
        c_int, POINTER(c_int), POINTER(c_int)
    ]
    WGFMU_getMeasureValueSize.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 251
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getMeasureValues'):
        continue
    WGFMU_getMeasureValues = _lib.WGFMU_getMeasureValues
    WGFMU_getMeasureValues.argtypes = [
        c_int, c_int,
        POINTER(c_int),
        POINTER(c_double),
        POINTER(c_double)
    ]
    WGFMU_getMeasureValues.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 252
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getMeasureValue'):
        continue
    WGFMU_getMeasureValue = _lib.WGFMU_getMeasureValue
    WGFMU_getMeasureValue.argtypes = [
        c_int, c_int, POINTER(c_double),
        POINTER(c_double)
    ]
    WGFMU_getMeasureValue.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 256
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_getCompletedMeasureEventSize'):
        continue
    WGFMU_getCompletedMeasureEventSize = _lib.WGFMU_getCompletedMeasureEventSize
    WGFMU_getCompletedMeasureEventSize.argtypes = [
        c_int, POINTER(c_int), POINTER(c_int)
    ]
    WGFMU_getCompletedMeasureEventSize.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 257
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_isMeasureEventCompleted'):
        continue
    WGFMU_isMeasureEventCompleted = _lib.WGFMU_isMeasureEventCompleted
    WGFMU_isMeasureEventCompleted.argtypes = [
        c_int, String, String, c_int, c_double, c_int,
        POINTER(c_int),
        POINTER(c_int),
        POINTER(c_int),
        POINTER(c_int)
    ]
    WGFMU_isMeasureEventCompleted.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 261
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_dcforceVoltage'):
        continue
    WGFMU_dcforceVoltage = _lib.WGFMU_dcforceVoltage
    WGFMU_dcforceVoltage.argtypes = [c_int, c_double]
    WGFMU_dcforceVoltage.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 262
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_dcmeasureValue'):
        continue
    WGFMU_dcmeasureValue = _lib.WGFMU_dcmeasureValue
    WGFMU_dcmeasureValue.argtypes = [c_int, POINTER(c_double)]
    WGFMU_dcmeasureValue.restype = c_int
    break

# /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 263
for _lib in _libs.values():
    if not hasattr(_lib, 'WGFMU_dcmeasureAveragedValue'):
        continue
    WGFMU_dcmeasureAveragedValue = _lib.WGFMU_dcmeasureAveragedValue
    WGFMU_dcmeasureAveragedValue.argtypes = [
        c_int, c_int, c_int, POINTER(c_double)
    ]
    WGFMU_dcmeasureAveragedValue.restype = c_int
    break

WGFMUAPI = c_int  # /d/OneDrive - University of Utah/PhD-Related/TesterCodes/demo/wgfmu.h: 18

# No inserted files
