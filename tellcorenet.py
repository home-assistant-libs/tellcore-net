"""This is a Python module that provides an interface to the Yahoo! Weather

more details from https://github.com/pvizeli/tellcore-net
"""
import shlex
import subprocess

SOCAT_SERVER = \
    "socat TCP-LISTEN:{port},reuseaddr,fork UNIX-CONNECT:/tmp/TelldusClient"
SOCAT_CLIENT = \
    "socat TCP:{host}:{port} UNIX-LISTEN:/tmp/TelldusClient"


class TellCoreClient(object):
    """Client for tellcore."""

    def __init__(self, host, port):
        """Initialize TellCore client."""
        self.proc = None
        self.host = host
        self.port = port

    def start(self):
        """Start client."""
        args = shlex.split(SOCAT_CLIENT.format(host=self.host, port=self.port))
        self.proc = subprocess.Popen(
            args,
            stdin=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL
        )

    def stop(self):
        """Stop client."""
        if self.proc:
            self.proc.kill()
        self.proc = None


class TellCoreServer(object):
    """Server for tellcore."""

    def __init__(self, port):
        """Initialize TellCore server."""
        self.proc = None
        self.port = port

    def start(self):
        """Start server."""
        args = shlex.split(SOCAT_SERVER.format(port=self.port))
        self.proc = subprocess.Popen(
            args,
            stdin=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL
        )

    def stop(self):
        """Stop server."""
        if self.proc:
            self.proc.kill()
        self.proc = None
