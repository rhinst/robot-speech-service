from unittest.mock import patch, Mock

from speech.talker import say


def test_say():
    m_file = Mock()
    m_file.name = "/tmp/testfile"
    m_gtts = Mock()
    m_tempfile = Mock(return_value=m_file)
    m_os = Mock()
    m_call = Mock()
    test_text = "oh hello there"
    with patch("speech.talker.logger"), patch("speech.talker.gTTS", m_gtts), patch(
        "speech.talker.NamedTemporaryFile", m_tempfile
    ), patch("speech.talker.call", m_call), patch("speech.talker.os", m_os):
        say(test_text)
        m_gtts.assert_called_once_with(test_text)
        m_call.assert_called_once_with(f"mpg123 {m_file.name}", shell=True)
        m_os.unlink.assert_called_once_with(m_file.name)
