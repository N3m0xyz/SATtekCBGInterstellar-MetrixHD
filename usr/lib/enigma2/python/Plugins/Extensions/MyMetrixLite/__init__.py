# -*- coding: UTF-8 -*-
#######################################################################
#
#    MyMetrixLite by arn354 & svox
#    based on
#    MyMetrix
#    Coded by iMaxxx (c) 2013
#
#
#  This plugin is licensed under the Creative Commons
#  Attribution-NonCommercial-ShareAlike 3.0 Unported License.
#  To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/
#  or send a letter to Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305, USA.
#
#  This plugin is NOT free software. It is open source, you are allowed to
#  modify it (if you keep the license), but it may not be commercially
#  distributed other than under the conditions noted above.
#
#
#######################################################################

from gettext import bindtextdomain, dgettext, gettext
from os.path import exists
# from shutil import move

from Components.SystemInfo import BoxInfo
from Components.config import config, ConfigSubsection, ConfigSelection, ConfigSelectionNumber, ConfigYesNo, ConfigText, ConfigInteger
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
#############################################################

PLUGIN_PATH = resolveFilename(SCOPE_PLUGINS, "Extensions/MyMetrixLite")

#############################################################

# Gettext

PluginLanguageDomain = "MyMetrixLite"


def localeInit():
	bindtextdomain(PluginLanguageDomain, PLUGIN_PATH + "/locale")


def _(txt):
	ret = dgettext(PluginLanguageDomain, txt)
	return ret if ret else gettext(txt)


localeInit()
language.addCallback(localeInit)

#############################################################


#############################################################

Greyscale = [(f"{x}{x}{x}", _("Greyscale %d") % (i + 1)) for i, x in enumerate(("15", "1C", "2E", "42", "58", "6E", "84", "A4", "BD", "D8", "E6", "F2", "FA"))]

ColorList = [
		("F0A30A", _("Amber")),
		("825A2C", _("Brown")),
		("5E0901", _("Burgund")),
		("0050EF", _("Cobalt")),
		("911D10", _("Crimson")),
		("1BA1E2", _("Cyan")),
		("00008B", _("Darkblue")),
		("2F1A09", _("Darkbrown")),
		("0F0F0F", _("Darkgrey")),
		("A61D4D", _("Magenta %d") % 1),
		("660066", _("Magenta %d") % 2),
		("A4C400", _("Lime")),
		("6A00FF", _("Indigo")),
		("5FA816", _("Brightgreen")),
		("70AD11", _("Green")),
		("009A93", _("Turquoise")),
		("008A00", _("Emerald")),
		("76608A", _("Mauve")),
		("FF5A00", _("Mandarin")),
		("0000CD", _("Mediumblue")),
		("0A173A", _("Midnight")),
		("000080", _("Navy")),
		("6D8764", _("Olive")),
		("C3461B", _("Orange")),
		("F472D0", _("Pink")),
		("E51400", _("Red")),
		("27408B", _("Royal Blue")),
		("7A3B3F", _("Sienna")),
		("647687", _("Steel")),
		("149BAF", _("Teal")),
		("6C0AAB", _("Violet")),
		("D8C100", _("Brightyellow")),
		("BF9217", _("Yellow")),
		("000000", _("Black"))
	] + Greyscale + [("FFFFFF", _("White"))]


# new transparency values
# TransparencyList = [("%0.2X" % int(x * 2.555), "%d%%" % x) for x in list(range(0, 105, 5))]

# old transparency values
TransparencyList = [
	("00", "0%"),
	("0D", "5%"),
	("1A", "10%"),
	("27", "15%"),
	("34", "20%"),
	("40", "25%"),
	("4D", "30%"),
	("5A", "35%"),
	("67", "40%"),
	("74", "45%"),
	("80", "50%"),
	("8D", "55%"),
	("9A", "60%"),
	("A7", "65%"),
	("B4", "70%"),
	("C0", "75%"),
	("CD", "80%"),
	("DA", "85%"),
	("E7", "90%"),
	("F4", "95%"),
	("FF", "100%")
]

SysFontTypeList = [
	("/usr/share/fonts/ae_AlMateen.ttf", ("ae_AlMateen (ae_AlMateen.ttf)")),
	("/usr/share/fonts/andale.ttf", ("Andale Mono (andale.ttf)")),
	("/usr/share/fonts/DejaVuSans.ttf", ("DejaVu Sans (DejaVuSans.ttf)")),
	("/usr/share/fonts/lcd.ttf", ("LCD (lcd.ttf)")),
	# ("/usr/share/fonts/md_khmurabi_10.ttf", ("MD King KhammuRabi (md_khmurabi_10.ttf)")),
	("/usr/share/fonts/nmsbd.ttf", ("Nemisis Flatline (nmsbd.ttf)")),
	# ("/usr/share/fonts/Roboto-Black.ttf", ("Roboto Bk (Roboto-Black.ttf)")),
	# ("/usr/share/fonts/Roboto-BlackItalic.ttf", ("Roboto Bk (Roboto-BlackItalic.ttf)")),
	# ("/usr/share/fonts/Roboto-Bold.ttf", ("Roboto (Roboto-Bold.ttf)")),
	# ("/usr/share/fonts/Roboto-BoldItalic.ttf", ("Roboto (Roboto-BoldItalic.ttf)")),
	("/usr/share/fonts/tuxtxt.ttf", ("Bitstream Vera Sans Mono (tuxtxt.ttf)"))
	# ("/usr/share/fonts/valis_enigma.ttf", ("valis_enigma (valis_enigma.ttf)"))
]
SkinFontTypeList = [
	("/usr/share/enigma2/MetrixHD/fonts/analog.ttf", ("Analog (analog.ttf)")),
	("/usr/share/enigma2/MetrixHD/fonts/DejaVuSans.ttf", ("DejaVu Sans (DejaVuSans.ttf)")),
	("/usr/share/enigma2/MetrixHD/fonts/digi.ttf", ("LCD (digi.ttf)")),
	("/usr/share/enigma2/MetrixHD/fonts/DroidSans.ttf", ("Droid Sans (DroidSans.ttf)")),
	("/usr/share/enigma2/MetrixHD/fonts/DroidSans-Bold.ttf", ("Droid Sans Bold (DroidSans-Bold.ttf)")),
	("/usr/share/enigma2/MetrixHD/fonts/HandelGotD.ttf", ("HandelGotD (HandelGotD.ttf)")),
	("/usr/share/enigma2/MetrixHD/fonts/HandelGotDBol.ttf", ("HandelGotD Bold (HandelGotDBol.ttf)")),
	("/usr/share/enigma2/MetrixHD/fonts/OpenSans-Regular.ttf", ("OpenSans Regular (OpenSans-Regular.ttf)")),
	("/usr/share/enigma2/MetrixHD/fonts/Raleway-Channel.ttf", ("Raleway Channel (Raleway-Channel.ttf)")),
	("/usr/share/enigma2/MetrixHD/fonts/Raleway-Light.ttf", ("Raleway Light(Raleway-Light.ttf)")),
	("/usr/share/enigma2/MetrixHD/fonts/Raleway-Regular.ttf", ("Raleway Regular (Raleway-Regular.ttf)")),
	("/usr/share/enigma2/MetrixHD/fonts/setrixHD.ttf", ("Segoe UI Light 8 (setrixHD.ttf)"))
]

SkinFontPresetList = [
	("preset_0", _("Standard Fonts")),
	("preset_1", _("Standard Fonts greater")),
	("preset_2", _("Bold and greater Fonts")),
	("preset_3", _("Raleway Fonts")),
	("preset_4", _("Digital Fonts")),
	("preset_5", _("Analog Fonts")),
	("preset_6", _("HandelGotD Fonts"))
	]

FontTypeList = []

for lines in SysFontTypeList:
	if exists(lines[0]):
		FontTypeList.append(lines)

for lines in SkinFontTypeList:
	if exists(lines[0]):
		FontTypeList.append(lines)


def initColorsConfig():

	BorderList = [
		("F0A30A", _("Amber")),
		("825A2C", _("Brown")),
		("0050EF", _("Cobalt")),
		("911D10", _("Crimson")),
		("1BA1E2", _("Cyan")),
		("00008B", _("Darkblue")),
		("0F0F0F", _("Darkgrey")),
		("A61D4D", _("Magenta")),
		("A4C400", _("Lime")),
		("6A00FF", _("Indigo")),
		("5FA816", _("Brightgreen")),
		("70AD11", _("Green")),
		("008A00", _("Emerald")),
		("76608A", _("Mauve")),
		("0000CD", _("Mediumblue")),
		("000080", _("Navy")),
		("6D8764", _("Olive")),
		("C3461B", _("Orange")),
		("F472D0", _("Pink")),
		("E51400", _("Red")),
		("27408B", _("Royal Blue")),
		("7A3B3F", _("Sienna")),
		("647687", _("Steel")),
		("149BAF", _("Teal")),
		("6C0AAB", _("Violet")),
		("D8C100", _("Brightyellow")),
		("BF9217", _("Yellow")),
		("000000", _("Black"))
	] + Greyscale + [("FFFFFF", _("White")), ("trans", _("Transparent"))]

	BorderWidth = [
		("no", _("No"))
	] + [("%dpx" % x, _("%d px") % x) for x in range(1, 11)]

	SkinColorPresetList = [
		("preset_0", _("Standard Colors")),
		("preset_1", _("Bright Colors")),
		("preset_2", _("Dark Colors")),
		("preset_3", _("Red Colors")),
		("preset_4", _("Yellow Colors")),
		("preset_5", _("Green Colors"))
		]

	config.plugins.MyMetrixLiteColors = ConfigSubsection()

	# preset
	config.plugins.MyMetrixLiteColors.SkinColorExamples = ConfigSelection(default="preset_0", choices=SkinColorPresetList)
	# MetrixColors

	config.plugins.MyMetrixLiteColors.listboxborder_top = ConfigSelection(default="FFFFFF", choices=BorderList)
	config.plugins.MyMetrixLiteColors.listboxborder_topwidth = ConfigSelection(default="no", choices=BorderWidth)
	config.plugins.MyMetrixLiteColors.listboxborder_bottom = ConfigSelection(default="FFFFFF", choices=BorderList)
	config.plugins.MyMetrixLiteColors.listboxborder_bottomwidth = ConfigSelection(default="no", choices=BorderWidth)
	config.plugins.MyMetrixLiteColors.listboxborder_right = ConfigSelection(default="FFFFFF", choices=BorderList)
	config.plugins.MyMetrixLiteColors.listboxborder_rightwidth = ConfigSelection(default="no", choices=BorderWidth)
	config.plugins.MyMetrixLiteColors.listboxborder_left = ConfigSelection(default="FFFFFF", choices=BorderList)
	config.plugins.MyMetrixLiteColors.listboxborder_leftwidth = ConfigSelection(default="no", choices=BorderWidth)

	config.plugins.MyMetrixLiteColors.windowborder_top = ConfigSelection(default="0F0F0F", choices=BorderList)
	config.plugins.MyMetrixLiteColors.windowborder_bottom = ConfigSelection(default="0F0F0F", choices=BorderList)
	config.plugins.MyMetrixLiteColors.windowborder_right = ConfigSelection(default="0F0F0F", choices=BorderList)
	config.plugins.MyMetrixLiteColors.windowborder_left = ConfigSelection(default="0F0F0F", choices=BorderList)

	config.plugins.MyMetrixLiteColors.menufont = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.menufontselected = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.menubackground = ConfigSelection(default="0F0F0F", choices=ColorList)
	config.plugins.MyMetrixLiteColors.menubackgroundtransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.menusymbolbackground = ConfigSelection(default="27408B", choices=ColorList)
	config.plugins.MyMetrixLiteColors.menusymbolbackgroundtransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.infobarbackground = ConfigSelection(default="0F0F0F", choices=ColorList)
	config.plugins.MyMetrixLiteColors.infobarbackgroundtransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.infobarprogress = ConfigSelection(default="27408B", choices=ColorList)
	config.plugins.MyMetrixLiteColors.infobarprogresstransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.infobarfont1 = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.infobarfont2 = ConfigSelection(default="BDBDBD", choices=ColorList)
	config.plugins.MyMetrixLiteColors.infobaraccent1 = ConfigSelection(default="BDBDBD", choices=ColorList)
	config.plugins.MyMetrixLiteColors.infobaraccent2 = ConfigSelection(default="6E6E6E", choices=ColorList)

	config.plugins.MyMetrixLiteColors.channelselectionservice = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.channelselectionserviceselected = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.channelselectionservicedescription = ConfigSelection(default="BDBDBD", choices=ColorList)
	config.plugins.MyMetrixLiteColors.channelselectionprogress = ConfigSelection(default="BDBDBD", choices=ColorList)
	config.plugins.MyMetrixLiteColors.channelselectionprogressborder = ConfigSelection(default="BDBDBD", choices=ColorList)
	config.plugins.MyMetrixLiteColors.channelselectionservicedescriptionselected = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.channelselectioncolorServiceRecorded = ConfigSelection(default="E51400", choices=ColorList)
	config.plugins.MyMetrixLiteColors.channelselectioncolorServicePseudoRecorded = ConfigSelection(default="0000CD", choices=ColorList)
	config.plugins.MyMetrixLiteColors.channelselectioncolorServiceStreamed = ConfigSelection(default="C3461B", choices=ColorList)

	config.plugins.MyMetrixLiteColors.emcWatchingColor = ConfigSelection(default="D8C100", choices=ColorList)
	config.plugins.MyMetrixLiteColors.emcFinishedColor = ConfigSelection(default="5FA816", choices=ColorList)
	config.plugins.MyMetrixLiteColors.emcRecordingColor = ConfigSelection(default="E51400", choices=ColorList)
	config.plugins.MyMetrixLiteColors.emcCoolHighlightColor = ConfigYesNo(default=True)

	config.plugins.MyMetrixLiteColors.windowtitletext = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.windowtitletexttransparency = ConfigSelection(default="00", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.windowtitletextback = ConfigSelection(default="0F0F0F", choices=ColorList)
	config.plugins.MyMetrixLiteColors.windowtitletextbacktransparency = ConfigSelection(default="00", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.backgroundtext = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.backgroundtexttransparency = ConfigSelection(default="34", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.backgroundtextback = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.backgroundtextbacktransparency = ConfigSelection(default="67", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.backgroundtextborderwidth = ConfigSelectionNumber(0, 10, 1, default=0)
	config.plugins.MyMetrixLiteColors.backgroundtextbordercolor = ConfigSelection(default="0F0F0F", choices=ColorList)
	config.plugins.MyMetrixLiteColors.backgroundtextbordertransparency = ConfigSelection(default="1A", choices=TransparencyList)

	config.plugins.MyMetrixLiteColors.layerabackground = ConfigSelection(default="0F0F0F", choices=ColorList)
	config.plugins.MyMetrixLiteColors.layerabackgroundtransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.layeraforeground = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.layeraselectionbackground = ConfigSelection(default="27408B", choices=ColorList)
	config.plugins.MyMetrixLiteColors.layeraselectionbackgroundtransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.layeraselectionforeground = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.layeraaccent1 = ConfigSelection(default="BDBDBD", choices=ColorList)
	config.plugins.MyMetrixLiteColors.layeraaccent2 = ConfigSelection(default="6E6E6E", choices=ColorList)
	config.plugins.MyMetrixLiteColors.layeraprogress = ConfigSelection(default="27408B", choices=ColorList)
	config.plugins.MyMetrixLiteColors.layeraprogresstransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.layeraunderline = ConfigSelection(default="BDBDBD", choices=ColorList)
	config.plugins.MyMetrixLiteColors.layeraunderlinetransparency = ConfigSelection(default="00", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.layeraextendedinfo1 = ConfigSelection(default="BDBDBD", choices=ColorList)
	config.plugins.MyMetrixLiteColors.layeraextendedinfo2 = ConfigSelection(default="6E6E6E", choices=ColorList)

	config.plugins.MyMetrixLiteColors.layerbbackground = ConfigSelection(default="27408B", choices=ColorList)
	config.plugins.MyMetrixLiteColors.layerbbackgroundtransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.layerbforeground = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.layerbselectionbackground = ConfigSelection(default="0F0F0F", choices=ColorList)
	config.plugins.MyMetrixLiteColors.layerbselectionbackgroundtransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.layerbselectionforeground = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.layerbaccent1 = ConfigSelection(default="BDBDBD", choices=ColorList)
	config.plugins.MyMetrixLiteColors.layerbaccent2 = ConfigSelection(default="6E6E6E", choices=ColorList)
	config.plugins.MyMetrixLiteColors.layerbprogress = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.layerbprogresstransparency = ConfigSelection(default="1A", choices=TransparencyList)

	config.plugins.MyMetrixLiteColors.epgbackground = ConfigSelection(default="0F0F0F", choices=ColorList)
	config.plugins.MyMetrixLiteColors.epgbackgroundtransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.epgborderlines = ConfigSelection(default="BDBDBD", choices=ColorList)
	config.plugins.MyMetrixLiteColors.epgborderlinestransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.epgeventdescriptionforeground = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.epgeventdescriptionbackground = ConfigSelection(default="27408B", choices=ColorList)
	config.plugins.MyMetrixLiteColors.epgeventdescriptionbackgroundtransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.epgeventforeground = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.epgeventbackground = ConfigSelection(default="0F0F0F", choices=ColorList)
	config.plugins.MyMetrixLiteColors.epgeventbackgroundtransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.epgprimetimeforeground = ConfigSelection(default="008A00", choices=ColorList)
	config.plugins.MyMetrixLiteColors.epgprimetimebackground = ConfigSelection(default="0F0F0F", choices=ColorList)
	config.plugins.MyMetrixLiteColors.epgprimetimebackgroundtransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.epgeventnowforeground = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.epgeventnowbackground = ConfigSelection(default="000000", choices=ColorList)
	config.plugins.MyMetrixLiteColors.epgeventnowbackgroundtransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.epgeventselectedforeground = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.epgeventselectedbackground = ConfigSelection(default="27408B", choices=ColorList)
	config.plugins.MyMetrixLiteColors.epgeventselectedbackgroundtransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.epgserviceforeground = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.epgservicebackground = ConfigSelection(default="0F0F0F", choices=ColorList)
	config.plugins.MyMetrixLiteColors.epgservicebackgroundtransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.epgservicenowforeground = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.epgservicenowbackground = ConfigSelection(default="27408B", choices=ColorList)
	config.plugins.MyMetrixLiteColors.epgservicenowbackgroundtransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.epgtimelineforeground = ConfigSelection(default="F0A30A", choices=ColorList)
	config.plugins.MyMetrixLiteColors.epgtimelinebackground = ConfigSelection(default="000000", choices=ColorList)
	config.plugins.MyMetrixLiteColors.epgtimelinebackgroundtransparency = ConfigSelection(default="1A", choices=TransparencyList)

	config.plugins.MyMetrixLiteColors.buttonforeground = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.layeraclockforeground = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.layerbclockforeground = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.weatherborderlines = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.weatherborderlinestransparency = ConfigSelection(default="00", choices=TransparencyList)

	config.plugins.MyMetrixLiteColors.upperleftcornerbackground = ConfigSelection(default="27408B", choices=ColorList)
	config.plugins.MyMetrixLiteColors.upperleftcornertransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.lowerleftcornerbackground = ConfigSelection(default="27408B", choices=ColorList)
	config.plugins.MyMetrixLiteColors.lowerleftcornertransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.upperrightcornerbackground = ConfigSelection(default="0F0F0F", choices=ColorList)
	config.plugins.MyMetrixLiteColors.upperrightcornertransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.lowerrightcornerbackground = ConfigSelection(default="0F0F0F", choices=ColorList)
	config.plugins.MyMetrixLiteColors.lowerrightcornertransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.optionallayerhorizontalbackground = ConfigSelection(default="27408B", choices=ColorList)
	config.plugins.MyMetrixLiteColors.optionallayerhorizontaltransparency = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.optionallayerverticalbackground = ConfigSelection(default="27408B", choices=ColorList)
	config.plugins.MyMetrixLiteColors.optionallayerverticaltransparency = ConfigSelection(default="1A", choices=TransparencyList)

	config.plugins.MyMetrixLiteColors.scrollbarSlidercolor = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteColors.scrollbarSlidertransparency = ConfigSelection(default="00", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.scrollbarSliderbordercolor = ConfigSelection(default="27408B", choices=ColorList)
	config.plugins.MyMetrixLiteColors.scrollbarSliderbordertransparency = ConfigSelection(default="00", choices=TransparencyList)

	config.plugins.MyMetrixLiteColors.cologradient = ConfigSelection(default="0", choices=[("0", _("disabled"))] + ColorList)
	config.plugins.MyMetrixLiteColors.cologradient_show_background = ConfigYesNo(default=True)
	choicelist = []
	for x in list(range(0, 105, 5)):
		choicelist.append(("%d" % x, "%d%s" % (x, "%")))
	config.plugins.MyMetrixLiteColors.cologradient_size = ConfigSelection(default="25", choices=choicelist)
	config.plugins.MyMetrixLiteColors.cologradient_position = ConfigSelection(default="25", choices=choicelist)
	config.plugins.MyMetrixLiteColors.cologradient_transparencyA = ConfigSelection(default="1A", choices=TransparencyList)
	config.plugins.MyMetrixLiteColors.cologradient_transparencyB = ConfigSelection(default="FF", choices=TransparencyList)

#############################################################


def initFontsConfig():

	config.plugins.MyMetrixLiteFonts = ConfigSubsection()
# preset
	config.plugins.MyMetrixLiteFonts.SkinFontExamples = ConfigSelection(default="preset_0", choices=SkinFontPresetList)
# system fonts
	config.plugins.MyMetrixLiteFonts.Lcd_type = ConfigSelection(default="/usr/share/fonts/lcd.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.Lcd_scale = ConfigSelectionNumber(50, 150, 1, default=100)
	config.plugins.MyMetrixLiteFonts.Replacement_type = ConfigSelection(default="/usr/share/fonts/ae_AlMateen.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.Replacement_scale = ConfigSelectionNumber(50, 150, 1, default=100)
	config.plugins.MyMetrixLiteFonts.Console_type = ConfigSelection(default="/usr/share/fonts/tuxtxt.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.Console_scale = ConfigSelectionNumber(50, 150, 1, default=100)
	config.plugins.MyMetrixLiteFonts.Fixed_type = ConfigSelection(default="/usr/share/fonts/andale.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.Fixed_scale = ConfigSelectionNumber(50, 150, 1, default=100)
	config.plugins.MyMetrixLiteFonts.Arial_type = ConfigSelection(default="/usr/share/fonts/nmsbd.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.Arial_scale = ConfigSelectionNumber(50, 150, 1, default=100)
# skin fonts
	config.plugins.MyMetrixLiteFonts.Regular_type = ConfigSelection(default="/usr/share/enigma2/MetrixHD/fonts/OpenSans-Regular.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.Regular_scale = ConfigSelectionNumber(50, 150, 1, default=94)
	config.plugins.MyMetrixLiteFonts.RegularLight_type = ConfigSelection(default="/usr/share/enigma2/MetrixHD/fonts/OpenSans-Regular.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.RegularLight_scale = ConfigSelectionNumber(50, 150, 1, default=94)
	config.plugins.MyMetrixLiteFonts.SetrixHD_type = ConfigSelection(default="/usr/share/enigma2/MetrixHD/fonts/setrixHD.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.SetrixHD_scale = ConfigSelectionNumber(50, 150, 1, default=100)
# ------------------------------#
# for individual skinned screens#
# ------------------------------#
# global
	config.plugins.MyMetrixLiteFonts.globaltitle_type = ConfigSelection(default="/usr/share/enigma2/MetrixHD/fonts/setrixHD.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.globaltitle_scale = ConfigSelectionNumber(50, 150, 1, default=100)
	config.plugins.MyMetrixLiteFonts.globalbutton_type = ConfigSelection(default="/usr/share/enigma2/MetrixHD/fonts/setrixHD.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.globalbutton_scale = ConfigSelectionNumber(50, 150, 1, default=90)
	config.plugins.MyMetrixLiteFonts.globalclock_type = ConfigSelection(default="/usr/share/enigma2/MetrixHD/fonts/setrixHD.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.globalclock_scale = ConfigSelectionNumber(50, 150, 1, default=100)
	config.plugins.MyMetrixLiteFonts.globalweatherweek_type = ConfigSelection(default="/usr/share/enigma2/MetrixHD/fonts/OpenSans-Bold.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.globalweatherweek_scale = ConfigSelectionNumber(50, 150, 1, default=100)
	config.plugins.MyMetrixLiteFonts.globallarge_type = ConfigSelection(default="/usr/share/enigma2/MetrixHD/fonts/setrixHD.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.globallarge_scale = ConfigSelectionNumber(50, 150, 1, default=80)
	config.plugins.MyMetrixLiteFonts.globalsmall_type = ConfigSelection(default="/usr/share/enigma2/MetrixHD/fonts/OpenSans-Regular.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.globalsmall_scale = ConfigSelectionNumber(50, 150, 1, default=94)
	config.plugins.MyMetrixLiteFonts.globalmenu_type = ConfigSelection(default="/usr/share/enigma2/MetrixHD/fonts/setrixHD.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.globalmenu_scale = ConfigSelectionNumber(50, 150, 1, default=100)
# screens, plugins
	config.plugins.MyMetrixLiteFonts.screenlabel_type = ConfigSelection(default="/usr/share/enigma2/MetrixHD/fonts/OpenSans-Regular.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.screenlabel_scale = ConfigSelectionNumber(50, 150, 1, default=94)
	config.plugins.MyMetrixLiteFonts.screentext_type = ConfigSelection(default="/usr/share/enigma2/MetrixHD/fonts/OpenSans-Regular.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.screentext_scale = ConfigSelectionNumber(50, 150, 1, default=94)
	config.plugins.MyMetrixLiteFonts.screeninfo_type = ConfigSelection(default="/usr/share/enigma2/MetrixHD/fonts/setrixHD.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.screeninfo_scale = ConfigSelectionNumber(50, 150, 1, default=100)
# epg, channellist, movielist
	config.plugins.MyMetrixLiteFonts.epgevent_type = ConfigSelection(default="/usr/share/enigma2/MetrixHD/fonts/OpenSans-Regular.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.epgevent_scale = ConfigSelectionNumber(50, 150, 1, default=94)
	config.plugins.MyMetrixLiteFonts.epgtext_type = ConfigSelection(default="/usr/share/enigma2/MetrixHD/fonts/OpenSans-Regular.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.epgtext_scale = ConfigSelectionNumber(50, 150, 1, default=94)
	config.plugins.MyMetrixLiteFonts.epginfo_type = ConfigSelection(default="/usr/share/enigma2/MetrixHD/fonts/OpenSans-Regular.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.epginfo_scale = ConfigSelectionNumber(50, 150, 1, default=94)
# infobar, movieplayer
	config.plugins.MyMetrixLiteFonts.infobarevent_type = ConfigSelection(default="/usr/share/enigma2/MetrixHD/fonts/setrixHD.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.infobarevent_scale = ConfigSelectionNumber(50, 150, 1, default=100)
	config.plugins.MyMetrixLiteFonts.infobartext_type = ConfigSelection(default="/usr/share/enigma2/MetrixHD/fonts/OpenSans-Regular.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteFonts.infobartext_scale = ConfigSelectionNumber(50, 150, 1, default=94)

#######################################################################


def initWeatherConfig():
	pass


#######################################################################


def initOtherConfig():
	channelSelectionStyleList = [
		("CHANNELSELECTION-1", _("Focus left, no picon, 5 next Events")),
		("CHANNELSELECTION-2", _("Focus left, big picon, 1 next Events")),
		("CHANNELSELECTION-3", _("Focus right, big picon, 1 next Events")),
		("CHANNELSELECTION-4", _("Focus right, no picon, 5 next Events"))
		]

	movielistStyleList = [
		("left", _("Focus left, description right")),
		("right", _("Focus right, description left"))
		]

	infoBarChannelNameFontSizeList = [
		("INFOBARCHANNELNAME-5", "40"),
		("INFOBARCHANNELNAME-4", "50"),
		("INFOBARCHANNELNAME-3", "60"),
		("INFOBARCHANNELNAME-2", "70"),
		("INFOBARCHANNELNAME-1", "80")
		]

	skinDesignShowLayerList = [
		("no", _("No")),
		("screens", _("in Screens")),
		("menus", _("in Menus")),
		("both", _("in Menus and Screens"))
		]

	skinDesignPresetList = [
		("preset_0", _("No Design")),
		("preset_1", _("One Layer Design")),
		("preset_2", _("Contrast Layer Design")),
		("preset_3", _("Stripe Layer Design")),
		("preset_4", _("Blocks Layer Design")),
		("preset_5", _("Frame Layer Design"))
		]

	config.plugins.MyMetrixLiteOther = ConfigSubsection()
	config.plugins.MyMetrixLiteOther.Custom = ConfigYesNo(default=False)

	# OtherSettings
	# EHD-Option -> Enhanced HD
	BoxType = BoxInfo.getItem("machinebuild")
	config.plugins.MyMetrixLiteOther.EHDtested = ConfigText(default=f"{BoxType}_|_0")

	skinmodes = [("0", _("Standard HD (1280x720)"))]
	mode1080p = mode2160p = risk = False
	try:
		if exists("/proc/stb/video/videomode_choices"):
			vmodes = open("/proc/stb/video/videomode_choices").read()
			if "1080p" in vmodes:
				mode1080p = True
#			if "2160p" in vmodes:
#				mode2160p = True
		else:
			risk = True
	except Exception:
		print("[MyMetrixLite] - can't read video modes")
		risk = True

	tested = config.plugins.MyMetrixLiteOther.EHDtested.value.split("_|_")
	risktxt = _(" - box support unknown")
	if len(tested) == 2:
		if BoxType in tested[0] and "1" in tested[1]:
			skinmodes.append(("1", _("Full HD (1920x1080)")))
		elif mode1080p or risk:
			skinmodes.append(("1", _("Full HD (1920x1080) %s") % risktxt))
#		if BoxType in tested[0] and "2" in tested[1]:
#			skinmodes.append(("2", _("Ultra HD (3840x2160)")))
#		elif mode2160p or risk:
#			skinmodes.append(("2", _("Ultra HD (3840x2160) %s") % risktxt))
	else:
		if mode1080p or risk:
			skinmodes.append(("1", _("Full HD (1920x1080) %s") % risktxt))
		#if mode2160p or risk:
		#	skinmodes.append(("2", _("Ultra HD (3840x2160) %s") % risktxt))

	###no box supports at time uhd skins ...###
	dummy = _("Ultra HD (3840x2160)")
	dummy = _("Ultra HD (3840x2160) %s")

	###########################################
	config.plugins.MyMetrixLiteOther.EHDenabled = ConfigSelection(default="0", choices=skinmodes)
	config.plugins.MyMetrixLiteOther.EHDrounddown = ConfigYesNo(default=False)
	config.plugins.MyMetrixLiteOther.EHDfontoffset = ConfigSelectionNumber(-10, 5, 1, default=0)
	config.plugins.MyMetrixLiteOther.EHDpiconzoom = ConfigSelection(default="1.0", choices=[("0", _("No")), ("0.2", "20%"), ("0.4", "40%"), ("0.6", "60%"), ("0.8", "80%"), ("1.0", "100%")])
	config.plugins.MyMetrixLiteOther.piconresize_experimental = ConfigYesNo(default=False)
	sharpness = []
	for i in list(range(0, 525, 25)):
		x = str(format(float(i) / 100, ".2f"))
		sharpness.append((x, x))
	config.plugins.MyMetrixLiteOther.piconsharpness_experimental = ConfigSelection(default="1.00", choices=sharpness)
	# STB-Info
	config.plugins.MyMetrixLiteOther.STBDistance = ConfigSelectionNumber(1, 50, 1, default=10)
	config.plugins.MyMetrixLiteOther.showCPULoad = ConfigYesNo(default=True)
	config.plugins.MyMetrixLiteOther.showRAMfree = ConfigYesNo(default=False)
	config.plugins.MyMetrixLiteOther.showSYSTemp = ConfigYesNo(default=False)
	config.plugins.MyMetrixLiteOther.showCPUTemp = ConfigYesNo(default=False)
	# Infobar/Secondinfobar
	config.plugins.MyMetrixLiteOther.showInfoBarServiceIcons = ConfigYesNo(default=True)
	config.plugins.MyMetrixLiteOther.showChannelNumber = ConfigYesNo(default=True)
	config.plugins.MyMetrixLiteOther.showChannelName = ConfigYesNo(default=True)
	config.plugins.MyMetrixLiteOther.infoBarChannelNameFontSize = ConfigSelection(default="INFOBARCHANNELNAME-1", choices=infoBarChannelNameFontSizeList)
	config.plugins.MyMetrixLiteOther.showInfoBarResolution = ConfigYesNo(default=True)
	config.plugins.MyMetrixLiteOther.showInfoBarResolutionExtended = ConfigYesNo(default=False)
	config.plugins.MyMetrixLiteOther.showExtendedinfo = ConfigYesNo(default=False)

	config.plugins.MyMetrixLiteOther.showExtended_caid = ConfigYesNo(default=True)
	config.plugins.MyMetrixLiteOther.showExtended_prov = ConfigYesNo(default=False)
	config.plugins.MyMetrixLiteOther.showExtended_pid = ConfigYesNo(default=False)
	config.plugins.MyMetrixLiteOther.showExtended_source = ConfigYesNo(default=True)
	config.plugins.MyMetrixLiteOther.showExtended_reader = ConfigYesNo(default=False)
	config.plugins.MyMetrixLiteOther.showExtended_protocol = ConfigYesNo(default=False)
	config.plugins.MyMetrixLiteOther.showExtended_hops = ConfigYesNo(default=True)
	config.plugins.MyMetrixLiteOther.showExtended_ecmtime = ConfigYesNo(default=True)

	config.plugins.MyMetrixLiteOther.ExtendedinfoStyle = ConfigSelection(default="1", choices=[("1", _("Top of the screen")), ("2", _("Between Clock and Weather enclosed")), ("3", _("Between Clock and Weather centered")), ("4", _("Bottom of the screen"))])
	config.plugins.MyMetrixLiteOther.ExtendedinfoCaidStyle = ConfigSelection(default="2", choices=[("1", _("All CAID")), ("2", _("Only current"))])
	config.plugins.MyMetrixLiteOther.showSnr = ConfigYesNo(default=True)
	config.plugins.MyMetrixLiteOther.showRecordstate = ConfigYesNo(default=True)
	config.plugins.MyMetrixLiteOther.showOrbitalposition = ConfigYesNo(default=True)
	config.plugins.MyMetrixLiteOther.showInfoBarClock = ConfigYesNo(default=True)
	config.plugins.MyMetrixLiteOther.showSTBinfo = ConfigYesNo(default=False)
	config.plugins.MyMetrixLiteOther.showTunerinfo = ConfigYesNo(default=True)
	config.plugins.MyMetrixLiteOther.setTunerAuto = ConfigYesNo(default=True)
	config.plugins.MyMetrixLiteOther.setTunerManual = ConfigSelection(default="2", choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"), ("7", "7"), ("8", "8"), ("10", "10"), ("12", "12"), ("16", "16"), ("18", "18"), ("19", "19")])
	config.plugins.MyMetrixLiteOther.showInfoBarRunningtext = ConfigYesNo(default=False)
	# pig
	config.plugins.MyMetrixLiteOther.movielist_pig = ConfigYesNo(default=False)
	config.plugins.MyMetrixLiteOther.emc_pig = ConfigYesNo(default=False)
	# running text parameter
	config.plugins.MyMetrixLiteOther.runningTextStartdelay = ConfigSelectionNumber(600, 10000, 100, default=1200, wraparound=True)
	config.plugins.MyMetrixLiteOther.runningTextSpeed = ConfigSelectionNumber(20, 1000, 10, default=60, wraparound=True)
	# channel list
	config.plugins.MyMetrixLiteOther.channelSelectionStyle = ConfigSelection(default="CHANNELSELECTION-1", choices=channelSelectionStyleList)
	config.plugins.MyMetrixLiteOther.setItemDistance = ConfigSelectionNumber(1, 50, 1, default=5, wraparound=True)
	config.plugins.MyMetrixLiteOther.setFieldMargin = ConfigSelectionNumber(1, 50, 1, default=5, wraparound=True)
	config.plugins.MyMetrixLiteOther.channelSelectionShowPrimeTime = ConfigYesNo(default=False)
	config.plugins.MyMetrixLiteOther.graphicalEpgStyle = ConfigSelection(default="1", choices=[("1", _("Standard")), ("2", _("more Events or 'mini TV' greater"))])
	config.plugins.MyMetrixLiteOther.showChannelListScrollbar = ConfigYesNo(default=False)
	config.plugins.MyMetrixLiteOther.showChannelListRunningtext = ConfigYesNo(default=False)
	# EMC/MoviePlayer
	config.plugins.MyMetrixLiteOther.movielistStyle = ConfigSelection(default="left", choices=movielistStyleList)
	config.plugins.MyMetrixLiteOther.InfoBarMoviePlayerDesign = ConfigSelection(default="2", choices=[("1", _("Large")), ("2", _("Standard")), ("3", _("Small"))])
	config.plugins.MyMetrixLiteOther.showMovieName = ConfigYesNo(default=True)
	config.plugins.MyMetrixLiteOther.showInfoBarClockMoviePlayer = ConfigYesNo(default=True)
	config.plugins.MyMetrixLiteOther.showMoviePlayerResolutionExtended = ConfigYesNo(default=False)
	config.plugins.MyMetrixLiteOther.showSTBinfoMoviePlayer = ConfigYesNo(default=False)
	config.plugins.MyMetrixLiteOther.showMovieTime = ConfigSelection(default="2", choices=[("1", _("No")), ("2", _("In Moviebar")), ("3", _("Side by PVR-Symbol"))])
	config.plugins.MyMetrixLiteOther.showPVRState = ConfigSelection(default="1", choices=[("1", _("Standard")), ("2", _("Top of the screen")), ("3", _("Top of the screen with current time"))])
	config.plugins.MyMetrixLiteOther.showMovieListScrollbar = ConfigYesNo(default=False)
	config.plugins.MyMetrixLiteOther.showMovieListRunningtext = ConfigYesNo(default=False)
	# EMC
	config.plugins.MyMetrixLiteOther.showEMCMediaCenterCover = ConfigSelection(default="no", choices=[("no", _("No")), ("small", _("Small")), ("large", _("Large"))])
	config.plugins.MyMetrixLiteOther.showEMCMediaCenterCoverInfobar = ConfigYesNo(default=True)
	config.plugins.MyMetrixLiteOther.showEMCSelectionCover = ConfigSelection(default="no", choices=[("no", _("No")), ("small", _("Small")), ("large", _("Large"))])
	config.plugins.MyMetrixLiteOther.showEMCSelectionCoverLargeDescription = ConfigYesNo(default=True)
	config.plugins.MyMetrixLiteOther.showEMCSelectionRows = ConfigSelection(default="0", choices=[("-4", "-4"), ("-2", "-2"), ("0", _("No")), ("+2", "+2"), ("+4", "+4"), ("+6", "+6"), ("+8", "+8")])
	config.plugins.MyMetrixLiteOther.showEMCSelectionPicon = ConfigSelection(default="no", choices=[("no", _("No")), ("left", _("left")), ("right", _("right"))])
	choicelist = [("0", _("off"))]
	for x in list(range(50, 202, 2)):
		choicelist.append(("%d" % x, "%d" % x))
	config.plugins.MyMetrixLiteOther.setEMCdatesize = ConfigSelection(default="104", choices=choicelist)
	config.plugins.MyMetrixLiteOther.setEMCdirinfosize = ConfigSelection(default="140", choices=choicelist)
	choicelist = [("0", _("off"))]
	for x in list(range(20, 82, 2)):
		choicelist.append(("%d" % x, "%d" % x))
	config.plugins.MyMetrixLiteOther.setEMCbarsize = ConfigSelection(default="50", choices=choicelist)
	# SkinDesign
	config.plugins.MyMetrixLiteOther.SkinDesignScrollbarSliderWidth = ConfigSelectionNumber(0, 15, 1, default=10)
	config.plugins.MyMetrixLiteOther.SkinDesignScrollbarBorderWidth = ConfigSelectionNumber(0, 5, 1, default=1)
	config.plugins.MyMetrixLiteOther.SkinDesignMenuButtons = ConfigYesNo(default=True)
	config.plugins.MyMetrixLiteOther.SkinDesignMenuScrollInfo = ConfigYesNo(default=True)
	config.plugins.MyMetrixLiteOther.SkinDesign = ConfigSelection(default="1", choices=[("1", _("Standard")), ("2", _("Layer A and B same height, Clock in Layer A")), ("3", _("Layer A and B same height, Clock in Layer B"))])
	config.plugins.MyMetrixLiteOther.SkinDesignSpace = ConfigYesNo(default=False)
	config.plugins.MyMetrixLiteOther.SkinDesignInfobarPicon = ConfigSelection(default="1", choices=[("1", _("XPicons")), ("2", _("ZZZPicons"))])
	config.plugins.MyMetrixLiteOther.SkinDesignInfobarXPiconPosX = ConfigSelectionNumber(-33, 33, 1, default=0)
	config.plugins.MyMetrixLiteOther.SkinDesignInfobarXPiconPosY = ConfigSelectionNumber(-14, 14, 1, default=0)
	config.plugins.MyMetrixLiteOther.SkinDesignInfobarZZZPiconPosX = ConfigSelectionNumber(0, 66, 1, default=0)
	config.plugins.MyMetrixLiteOther.SkinDesignInfobarZZZPiconPosY = ConfigSelectionNumber(0, 28, 1, default=0)
	config.plugins.MyMetrixLiteOther.SkinDesignInfobarZZZPiconSize = ConfigSelectionNumber(-28, 0, 1, default=0)
	config.plugins.MyMetrixLiteOther.SkinDesignShowLargeText = ConfigSelection(default="both", choices=skinDesignShowLayerList)
	config.plugins.MyMetrixLiteOther.SkinDesignLUC = ConfigSelection(default="no", choices=skinDesignShowLayerList)
	config.plugins.MyMetrixLiteOther.SkinDesignLLC = ConfigSelection(default="no", choices=skinDesignShowLayerList)
	config.plugins.MyMetrixLiteOther.SkinDesignRUC = ConfigSelection(default="no", choices=skinDesignShowLayerList)
	config.plugins.MyMetrixLiteOther.SkinDesignRLC = ConfigSelection(default="no", choices=skinDesignShowLayerList)
	config.plugins.MyMetrixLiteOther.SkinDesignOLH = ConfigSelection(default="no", choices=skinDesignShowLayerList)
	config.plugins.MyMetrixLiteOther.SkinDesignOLV = ConfigSelection(default="no", choices=skinDesignShowLayerList)
	config.plugins.MyMetrixLiteOther.SkinDesignLUCwidth = ConfigInteger(default=40, limits=(0, 1280))
	config.plugins.MyMetrixLiteOther.SkinDesignLUCheight = ConfigInteger(default=25, limits=(0, 720))
	config.plugins.MyMetrixLiteOther.SkinDesignLUCposz = ConfigInteger(default=0, limits=(0, 5))
	config.plugins.MyMetrixLiteOther.SkinDesignLLCwidth = ConfigInteger(default=40, limits=(0, 1280))
	config.plugins.MyMetrixLiteOther.SkinDesignLLCheight = ConfigInteger(default=45, limits=(0, 720))
	config.plugins.MyMetrixLiteOther.SkinDesignLLCposz = ConfigInteger(default=0, limits=(0, 5))
	config.plugins.MyMetrixLiteOther.SkinDesignRUCwidth = ConfigInteger(default=40, limits=(0, 1280))
	config.plugins.MyMetrixLiteOther.SkinDesignRUCheight = ConfigInteger(default=60, limits=(0, 720))
	config.plugins.MyMetrixLiteOther.SkinDesignRUCposz = ConfigInteger(default=0, limits=(0, 5))
	config.plugins.MyMetrixLiteOther.SkinDesignRLCwidth = ConfigInteger(default=40, limits=(0, 1280))
	config.plugins.MyMetrixLiteOther.SkinDesignRLCheight = ConfigInteger(default=80, limits=(0, 720))
	config.plugins.MyMetrixLiteOther.SkinDesignRLCposz = ConfigInteger(default=0, limits=(0, 5))
	config.plugins.MyMetrixLiteOther.SkinDesignOLHwidth = ConfigInteger(default=1127, limits=(0, 1280))
	config.plugins.MyMetrixLiteOther.SkinDesignOLHheight = ConfigInteger(default=30, limits=(0, 720))
	config.plugins.MyMetrixLiteOther.SkinDesignOLHposx = ConfigInteger(default=0, limits=(0, 1280))
	config.plugins.MyMetrixLiteOther.SkinDesignOLHposy = ConfigInteger(default=655, limits=(0, 720))
	config.plugins.MyMetrixLiteOther.SkinDesignOLHposz = ConfigInteger(default=0, limits=(0, 5))
	config.plugins.MyMetrixLiteOther.SkinDesignOLVwidth = ConfigInteger(default=60, limits=(0, 1280))
	config.plugins.MyMetrixLiteOther.SkinDesignOLVheight = ConfigInteger(default=669, limits=(0, 720))
	config.plugins.MyMetrixLiteOther.SkinDesignOLVposx = ConfigInteger(default=102, limits=(0, 1280))
	config.plugins.MyMetrixLiteOther.SkinDesignOLVposy = ConfigInteger(default=51, limits=(0, 720))
	config.plugins.MyMetrixLiteOther.SkinDesignOLVposz = ConfigInteger(default=0, limits=(0, 5))
	config.plugins.MyMetrixLiteOther.layeraunderlinesize = ConfigSelectionNumber(0, 10, 1, default=1)
	config.plugins.MyMetrixLiteOther.layeraunderlineposy = ConfigSelectionNumber(-5, 5, 1, default=0)
	config.plugins.MyMetrixLiteOther.layeraunderlineshowmainlayer = ConfigYesNo(default=False)
	# preset
	config.plugins.MyMetrixLiteOther.SkinDesignExamples = ConfigSelection(default="preset_0", choices=skinDesignPresetList)
	# Buttons
	config.plugins.MyMetrixLiteOther.SkinDesignButtons = ConfigYesNo(default=False)
	config.plugins.MyMetrixLiteOther.SkinDesignButtonsBackColor = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteOther.SkinDesignButtonsBackColorTransparency = ConfigSelection(default="00", choices=TransparencyList)
	config.plugins.MyMetrixLiteOther.SkinDesignButtonsFrameColor = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteOther.SkinDesignButtonsFrameColorTransparency = ConfigSelection(default="00", choices=TransparencyList)
	config.plugins.MyMetrixLiteOther.SkinDesignButtonsTextColor = ConfigSelection(default="000000", choices=ColorList)
	config.plugins.MyMetrixLiteOther.SkinDesignButtonsTextColorTransparency = ConfigSelection(default="00", choices=TransparencyList)
	config.plugins.MyMetrixLiteOther.SkinDesignButtonsTextFont = ConfigSelection(default="/usr/share/enigma2/MetrixHD/fonts/OpenSans-Regular.ttf", choices=FontTypeList)
	config.plugins.MyMetrixLiteOther.SkinDesignButtonsTextSize = ConfigSelectionNumber(10, 30, 1, default=24)
	config.plugins.MyMetrixLiteOther.SkinDesignButtonsFrameSize = ConfigSelectionNumber(0, 5, 1, default=0)
	config.plugins.MyMetrixLiteOther.SkinDesignButtonsTextPosition = ConfigSelectionNumber(-10, 10, 1, default=0)
	config.plugins.MyMetrixLiteOther.SkinDesignButtonsGlossyEffect = ConfigSelection(default="no", choices=[("no", _("None")), ("solidframe", _("Solid")), ("solid", _("Solid without Frame")), ("gradientframe", _("Flat Gradient")), ("gradient", _("Flat Gradient without Frame")), ("circleframe", _("Circle Gradient")), ("circle", _("Circle Gradient without Frame"))])

	choicelist = [(f"{x / 10:.1f}", "%d%%" % (x * 10)) for x in range(1, 11)]
	config.plugins.MyMetrixLiteOther.SkinDesignButtonsGlossyEffectSize = ConfigSelection(default="0.5", choices=choicelist)

	choicelist = [(f"{x / 10:.1f}", "%d" % (x * 10)) for x in range(11)]
	config.plugins.MyMetrixLiteOther.SkinDesignButtonsGlossyEffectPosX = ConfigSelection(default="0.5", choices=choicelist)
	config.plugins.MyMetrixLiteOther.SkinDesignButtonsGlossyEffectPosY = ConfigSelection(default="0.5", choices=choicelist)
	config.plugins.MyMetrixLiteOther.SkinDesignButtonsGlossyEffectColor = ConfigSelection(default="FFFFFF", choices=ColorList)
	config.plugins.MyMetrixLiteOther.SkinDesignButtonsGlossyEffectOverText = ConfigYesNo(default=False)
	config.plugins.MyMetrixLiteOther.SkinDesignButtonsGlossyEffectIntensity = ConfigSelection(default="00", choices=TransparencyList)
	config.plugins.MyMetrixLiteOther.menuDescription = ConfigYesNo(default=True)


#######################################################################


def getTunerPositionList():
	tunerPositionList = [
		("286,666", "286,693", "1", "0,0"),
		("306,666", "306,693", "2", "1,1"),
		("326,666", "326,693", "4", "2,2"),
		("346,666", "346,693", "8", "3,3"),
		("366,666", "366,693", "16", "4,4"),
		("386,666", "386,693", "32", "5,5")
	]

	return tunerPositionList

#######################################################################


def appendSkinFile(appendFileName, skinPartSearchAndReplace):
	"""
	add skin file to main skin content

	appendFileName:
		xml skin-part to add

	skinPartSearchAndReplace:
		(optional) a list of search and replace arrays. first element, search, second for replace
	"""
	rsSkinLines = []

	with open(appendFileName) as fd:
		file_lines = fd.readlines()

	for skinLine in file_lines:
		for item in skinPartSearchAndReplace:
			skinLine = skinLine.replace(item[0], item[1])
		rsSkinLines.append(skinLine)

	return rsSkinLines
