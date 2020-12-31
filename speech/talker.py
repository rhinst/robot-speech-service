import os
from tempfile import NamedTemporaryFile
from time import sleep

from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

from speech.logging import logger


def say(phrase):
    logger.debug("Saying '%s'", phrase)
    tts = gTTS(phrase)
    f = NamedTemporaryFile(mode="wb", delete=False)
    tts.write_to_fp(f)
    music = AudioSegment.from_mp3(f.name)
    play(music)
    sleep(5)
    os.unlink(f.name)