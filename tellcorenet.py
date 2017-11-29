"""This is a Python module that provides an interface to the Yahoo! Weather

more details from https://github.com/pvizeli/tellcore-net
"""
import shlex
import subprocess

SOCAT_SERVER = \
    "socat TCP-LISTEN:{port},reuseaddr,fork UNIX-CONNECT:/tmp/{type}"
SOCAT_CLIENT = \
    "socat TCP:{host}:{port} UNIX-LISTEN:/tmp/{type}"

TELLDUS_CLIENT = 'TelldusClient'
TELLDUS_EVENTS = 'TelldusEvents'


class TellCoreClient(object):
    """Client for tellcore."""

    def __init__(self, host, port_client, port_events):
        """Initialize TellCore client."""
        self.proc = None
        self.host = host
        self.port_client = port_client
        self.port_events = port_events

    def start(self):
        """Start client."""
        self.proc = []
        for telldus, port in (
                (TELLDUS_CLIENT, self.port_client),
                (TELLDUS_EVENTS, self.port_events)):
            args = shlex.split(SOCAT_CLIENT.format(
                type=telldus, host=self.host, port=port))
            self.proc.append(subprocess.Popen(
                args,
                stdin=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL
            ))

    def stop(self):
        """Stop client."""
        if self.proc:
            for proc in self.proc:
                proc.kill()
        self.proc = None


class TellCoreServer(object):
    """Server for tellcore."""

    def __init__(self, port_client, port_events):
        """Initialize TellCore server."""
        self.proc = None
        self.port_client = port_client
        self.port_events = port_events

    def start(self):
        """Start server."""
        self.proc = []
        for telldus, port in (
                (TELLDUS_CLIENT, self.port_client),
                (TELLDUS_EVENTS, self.port_events)):
            args = shlex.split(SOCAT_CLIENT.format(
                type=telldus, port=port))
            self.proc.append(subprocess.Popen(
                args,
                stdin=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL
            ))

    def stop(self):
        """Stop server."""
        if self.proc:
            for proc in self.proc:
                proc.kill()
        self.proc = None
