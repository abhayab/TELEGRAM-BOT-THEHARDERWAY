import telegram.ext

def start(update, context):
    update.message.reply_text("Hello! Welcome to TheHarderWay.\nYour ultimate destination for top-notch football skill tutorials! Our channel is dedicated to helping football enthusiasts like you master the art of the game, one skill at a time.In our tutorials, we break down complex football maneuvers into easy-to-follow steps, ensuring that players of all levels can improve their game. Whether you're a beginner looking to develop a solid foundation or an experienced player striving for mastery, we've got you covered.\nJoin our passionate community of football lovers who are committed to taking the harder way, knowing that it's the path to true excellence.\nTYPE /help to get the available commands")
    
def help(update,context):
    update.message.reply_text("""
    The following commands are available:
    /FREESTYLE  -> Freestyle Playlist
    /FUN ->  Fun Playlist
    /FLICKUPS-> Flick-ups Playlist
    /BALLMASTERY -> Ball Mastery Playlist
    /contact -> contact information 
     """)
    
#def content(update, context):
    #update.message.reply_text("We have various playlists available!")

def FREESTYLE(update, context):
    update.message.reply_text("tutorial link : https://www.youtube.com/watch?v=ExZF4AnuF_w&list=PLnk2_GJXZYAufIeCdApyglPIX4Kw_CQ0x&pp=iAQB")

def FUN(update, context):
    update.message.reply_text("tutorial link :https://www.youtube.com/watch?v=P4ACZf2tIjw&list=PLnk2_GJXZYAtRFvruEFTOKDf8t4qXZ1iE&pp=iAQB")
    
def FLICKUPS(update, context):
    update.message.reply_text("tutorial link :https://www.youtube.com/watch?v=kYdrl__-IlY&list=PLnk2_GJXZYAuBOJSeekJkCxNztOH3Bqeg&pp=iAQB")
    
def BALLMASTERY(update, context):
    update.message.reply_text("tutorial link : https://www.youtube.com/watch?v=eZdYDFcBH8o&list=PLnk2_GJXZYAvjJ6dQXdWCGVuOmcsp-T_Q&pp=iAQB")
    
def contact(update, context):
    update.message.reply_text("You can contact on the official mail id")

def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}, use the commands using /")


Token = ("TELEGRAM_BOT_APIKEY")
#print(bot.get_me())
updater = telegram.ext.Updater("TELEGRAM_BOT_APIKEY", use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start',start))
disp.add_handler(telegram.ext.CommandHandler('help',help))
#disp.add_handler(telegram.ext.CommandHandler('content',content))
disp.add_handler(telegram.ext.CommandHandler('FREESTYLE',FREESTYLE))
disp.add_handler(telegram.ext.CommandHandler('FUN',FUN))
disp.add_handler(telegram.ext.CommandHandler('FLICKUPS',FLICKUPS))
disp.add_handler(telegram.ext.CommandHandler('BALLMASTERY',BALLMASTERY))
disp.add_handler(telegram.ext.CommandHandler('contact',contact))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()
