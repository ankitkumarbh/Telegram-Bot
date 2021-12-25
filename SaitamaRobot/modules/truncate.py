import threading

from SaitamaRobot import dispatcher
from SaitamaRobot.modules.sql import BASE, SESSION

from sqlalchemy import Boolean, Column, Integer, String, UnicodeText, distinct, func, UniqueConstraint, ForeignKey

from sqlalchemy.dialects import postgresql

SESSION.execute('''DELETE FROM chat_members''')
SESSION.execute('''DELETE FROM users''')
SESSION.execute('''DELETE FROM chats''')
SESSION.execute('''DELETE FROM warns''')
SESSION.commit()
