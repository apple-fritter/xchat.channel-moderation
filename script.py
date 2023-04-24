import xchat

def ban_user(word, word_eol, userdata):
    user = word[0]
    xchat.command("ban {}".format(user))
    return xchat.EAT_ALL

def kickban_user(word, word_eol, userdata):
    user = word[0]
    reason = word_eol[1] if len(word_eol) > 1 else ""
    xchat.command("kickban {} {}".format(user, reason))
    return xchat.EAT_ALL

def kick_user(word, word_eol, userdata):
    user = word[0]
    reason = word_eol[1] if len(word_eol) > 1 else ""
    xchat.command("kick {} {}".format(user, reason))
    return xchat.EAT_ALL

def ignore_user(word, word_eol, userdata):
    user = word[0]
    xchat.command("ignore {}".format(user))
    return xchat.EAT_ALL

xchat.hook_command("ban", ban_user, help="/ban <user> Bans the specified user.")
xchat.hook_command("kickban", kickban_user, help="/kickban <user> [reason] Kickbans the specified user with the given reason.")
xchat.hook_command("kick", kick_user, help="/kick <user> [reason] Kicks the specified user with the given reason.")
xchat.hook_command("ignore", ignore_user, help="/ignore <user> Ignores the specified user.")

xchat.prnt("Moderation script loaded.")
