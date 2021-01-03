import os
from tempfile import NamedTemporaryFile
from subprocess import call

from gtts import gTTS

from speech.logging import logger


def say(phrase):
    logger.debug("Saying '%s'", phrase)
    tts = gTTS(phrase)
    f = NamedTemporaryFile(mode="wb", delete=False)
    tts.write_to_fp(f)
    call(f"mpg123 {f.name}", shell=True)
    os.unlink(f.name)