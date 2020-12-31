import os
from tempfile import NamedTemporaryFile
from time import sleep

from gtts import gTTS
from pyglet.media import load, Player

from speech.logging import logger


def say(phrase):
    logger.debug("Saying '%s'", phrase)
    tts = gTTS(phrase)
    f = NamedTemporaryFile(mode="wb", delete=False)
    tts.write_to_fp(f)
    player = Player()
    f = open(f.name, mode="rb")
    music = load("blah", file=f, streaming=False)
    player.queue(music)
    player.play()
    sleep(music.duration)
    player.delete()
    f.close()
    os.unlink(f.name)