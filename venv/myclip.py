#python 3
#mclip.py
#! python3
# mclip.py - A multi-clipboard program.
import pyperclip

TEXT = dict(agree="""Yes, I agree. That sounds fine to me.""",
            busy="""Sorry, can we do this later this week or next week?""",
            upsell="""Would you consider making this a monthly donation?""")
import sys
if len(sys.argv)   < 2:
    print('Usage: python myclip.py [keyphrase] - copy phares text')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(' Text for ' + keyphrase + 'copied to clipboard')
else:
    print('there is no text for' + keyphrase)

