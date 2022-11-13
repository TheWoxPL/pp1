from gettext import find
from operator import index


text = 'X-DSPAM-Confidence: 0.8475'
index=text.find(":")
float(text[index+2:])