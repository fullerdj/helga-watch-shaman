from twisted.internet import reactor
from helga.plugins import command, ResponseNotReady
from helga import log, settings
import urllib2
import json
#from urllib2 import *

logger = log.getLogger(__name__)

def check_ref(client, channel, nick, ref, sha1, last):
    logger.debug("foo")
    client.msg(channel, "looking")
    url = 'https://shaman.ceph.com/api/builds/ceph/' + ref + '/' + sha1
    f = urllib2.urlopen(url)
    repos = json.loads(f.read())
    
    status = [r['status'] for r in repos]
    
    if status == []:
        client.msg(channel, nick + ": couldn't find a build with " +
                   ref + "/" + sha1)
        
    for s in status:
        if (s != 'completed'):
            reactor.callLater(30, check_ref, client, channel,
                              nick, ref, sha1, status)
            break
            
    if status != last:
        client.msg(channel, nick + ": " + str(status))
    else:
        client.msg(channel, nick + ": no change")
    
@command('watch-build', aliases=['wb'], help='foo', priority=0, shlex=True)
def helga_watch_shaman(client, channel, nick, message, cmd, args):
    ref = args[0]
    sha1 = args[1]
    
    logger.debug("blah")
    check_ref(client, channel, nick, ref, sha1, [])
    raise ResponseNotReady
