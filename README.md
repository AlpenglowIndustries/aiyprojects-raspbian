# Alpenglow FUnicorn Google AIY Voice Repo

This repo is for an [Alpenglow Industries FUnicorn board][alpenglow-funicorn] hooked up to a Google AIY Voice Hat version 1 on a Raspberry Pi 3B+.  It basically makes the FUnicorn voice-activated, so you can say "Hey Google, Fuck You!" and beautiful LEDs written in cursive script light up with "Fuck You!", next to a majestic rearing gold unicorn.  What's not to love?

This was forked from the Google AIY Projects repo, original info on that below.

Changes and Additions:
* cloudspeech.py was updated according to description in [issue 716][issue-716].
* demo python scripts for the FUnicorn added to src/examples/voice

Examples:
* funicorn_demo_wassistant.py has full Google Assistant functionality and is commanded via the wake word (OK Google or Hey Google), and outputs a "button press" to the FUnicorn when "fuck you" is uttered.  It also says "No, Fuck You" in a most excellent obviously computer-generated voice.
* funicorn_demo_alwayslistening.py is solely a cloud speech to text demo that is always listening and interpreting.  There is no Google Assistant functionality.

Hardware Setup:
* Google AIY Voice Hat Servo 0 left pin (GPIO26) to Alpenglow FUnicorn button connector pin 3
* Google AIY Voice Hat Servo 0 right pin (GND) to Alpenglow FUnicorn button connector pin 4

Also see [The FUnicorn on Hackaday.io][funicorn-hackaday] for more info and photos.
For more irreverent electronics and frivolous circuits, follow us!
* [frivolous_circs][twitter] on twitter
* [frivolous.circuits][instagram] on instagram
* [Alpenglow Industries][hackaday] on Hackaday
* [Alpenglow Industries][youtube] on YouTube

Web and Storefronts:
* Alpenglow Industries [website][alpenglowindustries.com]
* Our products [on Tindie][tindie]
* Our products [on Digi-Key][digikey]

--------

## AIY Projects

This repository contains an easy-to-use Python API for the [AIY Vision Kit][aiy-vision]
and [AIY Voice Kit][aiy-voice]. The code for all AIY kits is in the `aiyprojects` branch,
and is included in images starting with `aiyprojects-2017-12-18.img`.
The previous `voicekit` branch contains code just for the Voice Kit, and the
`master` branch contains the original deprecated `Voice Recognizer` demo.

## Documentation

If you're just getting started with the Vision or Voice kit, see the
assembly guide and other maker guides at [aiyprojects.withgoogle.com].

If you just need the Python API reference, see [aiyprojects.readthedocs.io].
Also have a look at the [example code][aiy-github-examples].

If you want to flash the latest AIY system image or install AIY packages on an existing
Raspbian system, read the [system updates guide][HACKING.md].

## Releases

* [Image downloads][downloads]
* [Change log][changelog]

## Bugs & Support

If you've found a bug, please [review the known issues and report a new one][aiy-github-issues].

If you've fixed a bug yourself, please send us a pull request!
For details, read [CONTRIBUTING.md].

If you're having trouble assembling your kit or running the demos, try the following links:

* [AIY Help docs][help-docs]
* [AIY Forums][aiy-forums]
* [AIY Stack Overflow][aiy-stack-overflow]
* [AIY GitHub Issues][aiy-github-issues]
* support-aiyprojects@google.com

If you've found a problem with the Assistant API (for example, it crashes
or provides incorrect responses), try the following:

* [Assistant Stack Overflow][assistant-stack-overflow]
* [Assistant GitHub Issues][assistant-github-issues]

##

<p align="center">
  <img width="15%" src="https://aiyprojects.withgoogle.com/static/images/icons/aiy-circular-logo.svg">
</p>

[newsletter]: https://www.alpenglowindustries.com/newsletter.html
[twitter]: https://twitter.com/frivolous_circs
[instagram]: https://www.instagram.com/frivolous.circuits/
[hackaday]: https://hackaday.io/alpenglow
[youtube]: https://www.youtube.com/alpenglowindustries
[alpenglowindustries.com]: https://www.alpenglowindustries.com/
[tindie]: https://www.tindie.com/stores/alpenglow/
[digikey]: https://www.digikey.com/en/products/result?s=N4IgTCBcDaIIYBsAOBTAdgcwQewO4gF0BfIA
[alpenglow-funicorn]: https://www.tindie.com/products/alpenglow/the-funicorn/
[issue-716]: https://github.com/google/aiyprojects-raspbian/issues/716
[funicorn-hackaday]: https://hackaday.io/project/173726-the-funicorn

[HACKING.md]: HACKING.md
[CONTRIBUTING.md]: CONTRIBUTING.md
[downloads]: https://github.com/google/aiyprojects-raspbian/releases
[changelog]: CHANGES.md

[aiyprojects.withgoogle.com]: https://aiyprojects.withgoogle.com
[aiyprojects.readthedocs.io]: https://aiyprojects.readthedocs.io
[aiy-vision]: https://aiyprojects.withgoogle.com/vision/
[aiy-voice]: https://aiyprojects.withgoogle.com/voice/

[help-docs]: https://aiyprojects.withgoogle.com/help
[aiy-forums]: https://www.raspberrypi.org/forums/viewforum.php?f=114
[aiy-stack-overflow]: https://stackoverflow.com/questions/tagged/google-aiy
[aiy-github-issues]: https://github.com/google/aiyprojects-raspbian/issues
[aiy-github-examples]: https://github.com/google/aiyprojects-raspbian/tree/aiyprojects/src/examples

[assistant-stack-overflow]: https://stackoverflow.com/questions/tagged/google-assistant-sdk
[assistant-github-issues]: https://github.com/googlesamples/assistant-sdk-python/issues
