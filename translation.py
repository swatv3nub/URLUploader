class Translation(object):

    START_TEXT = """Hello,

Welcome to Cloud Download Bot!

<b>Please send me any Direct download URL link, I can upload to telegram as File/Video</b>

/help for more details..

Dev : @ProjectHackfreaks
"""

    HELP_USER = """Hey I'am a Cloud Downloader..
    
1. Send url (Link | New Name with Extension).
2. Send Custom Thumbnail (Optional).
3. Select the button.
   video  - Give File as video without Screenshots
   file  - Give File without Screenshots


"""

    FORMAT_SELECTION = """Select the desired format: <a href='{}'>file size might be approximate</a>
    
Send your custum thumbnail if required.
You can use /deletethumbnail to delete the auto-generated thumbnail."""
    
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""


    UPGRADE_TEXT = "<b>It's Free!! You Don'r need to Updrage.</a>"
    
    DOWNLOAD_START = "Trying to download your file..."
    
    UPLOAD_START = "Uploading now.."

    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \n\nUploaded in {} seconds. Join @ProjectHackfreaks"

    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."

    SAVED_CUSTOM_THUMB_NAIL = "Custom thumbnail saved. This will be permanent.\n\nUse /deletethumbnail to clear it."

    DEL_ETED_CUSTOM_THUMB_NAIL = "Custom thumbnail cleared succesfully."

    CUSTOM_CAPTION_UL_FILE = " "

    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    
    SHOW_THUMB = "Use /deletethumbnail to clear this thumbnail."
    
    NO_THUMB = "No saved thumbnails Found!!\n\nSend an image to save it as your thumbnail permanently."
  
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /rename with custom thumbnail support"

    RENAME_403_ERR = "403: File Couldn't be Renamed."
