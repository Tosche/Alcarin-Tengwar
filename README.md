![Title image](title.svg)

# Alcarin Tengwar

Alcarin Tengwar is a Tengwar typeface designed to pair well with the [Brill](https://www.brill.com/brill-typeface) typeface; Tengwar is an fictional writing system invented by J.R.R. Tolkien, used in his Lord Of The Rings works.

It is designed to look more typographic and of high quality, with academic context in mind. It works best with Brill, but can work with other roman typefaces. More detailed design notes can be seen [here](https://tosche.net/fonts/alcarin-tengwar).

The word 'alcarin' means 'brilliant' in the Quenya language, the High-Elven language by J.R.R. Tolkien.

Alcarin Tengwar is released under Open Font License 1.1.

## Contents
- Font Source: Glyphs 2 font source file as well as GlyphsData.xml to be installed in the ~/Library/Application Support/Glyphs 3/Info folder. [Further reading](https://glyphsapp.com/learn/roll-your-own-glyph-data)
- Fonts Static: OTF and web font versions. OTFs are autohinted, so are the OTF-based web fonts, but TTFs aren't due to the ttfautohint error with this source file.
- Fonts Variable: variable fonts in TTF and web font formats.
- Mak Keyboard Layout: My custom keyboard layout for macOS that is based on [FreeTengwar's tengwarQWERTY](http://freetengwar.sourceforge.net/keylayouts.html). It should appear as 'tengwarQWERTY Toshi'.
- README: This document.
- OFL.txt: The Open Font License 1.1 license text.
- PDFs: Some PDFs including the glyph set, manual, and simple specimens. The glyph mapping requires a special attention, as it uses my custom mapping based on [Free Tengwar's](http://freetengwar.sourceforge.net/mapping.html).
- Sample Text: Try the font with these text. (Note: the font doesn't contain Latin)

## Disclaimer
The Brill fonts are owned by Koninklijke Brill NV. They are not licensed under the OFL but under licenses of their own, both [non-commercial](https://brill.com/page/BrillFont/brill-typeface) and [commercial](https://fonts.ilovetypography.com/superfamily/Brill).

Alcarin Tengwar is not in any official way associated with either Koninklijke Brill NV or Tolkien Estate (though I have received the blessing of the former; not 100% unofficial). It also does not contain any graphical elements of Brill.

Also, I am a typeface designer, not a linguist. My knowledge on Tengwar and is rusty; if/when you raise issues, I would appreciate an attitude and vocabulary as if you would explain to a newbie.

## Font change log
0.82 2 Jul 2023
- Added missing bottom anchor to silme_harma.

0.81 2 Jul 2023
- Added secondary bottom anchor to lambe and alda to avoid second bottom diacritic to crash.
- Renamed calma_thuule ligature to harma_tinco; the former was seemingly a misinterpretation.

0.80 : 2 Jul 2023
- Aligned the macron height in Silme and Aare (was previously higher).
- Added top and bottom anchors to pusta, double pusta, and triple pusta, allowing them to carry diacritics.

0.70 : 8 Apr 2022
- Kerned /carrier/tehta/carrier/tehta combinations.
- Added silme_harma-teng ligature for Old English.
- Added discretionary ligature support by zerowidthjoiner in addition to the existing dlig feature.
- Added vowel carrier as below combining mark when followed by zerowidthjoiner.
- Added Unicode code points to the double acute marks above and below.

0.68 : 7 Jan 2022
- Set the existing letters to lowercase in anticipation of adding capitals.

0.67 : 6 Jan 2022
- Set the numerals to RTL (edit: this turned out to have no effect)
- Set the Rumilian numerals to bidirectional (I don't know if it's exclusively RTL or LTR)
- Set all diacritics to bidirectional (technically I could have set to RTL to only those used in the numerals, but I wanted to avoid making pockets of exceptions)

0.66 : 5 Jan 2022
- Hook-shaped tehtar are slightly enlarged for legibility.
- Silme and reverse silme are slightly thickened for legibility.
- Numerals with overscores can now be input by typing macron-teng (u+E050) after.
- Minor glyphs’ codepoints have been fixed (there were typos in the codepoints). Since they go beyond the designated Tengwar table of ConScript’s unofficial Unicode registory, any characters beyond E07F are subject to yet another migration.

0.65 : Jan 2022
- Added Latin from Noto Serif to make the font appear on macOS.

0.61 : 4 Jan 2022
- Added Unicode-standard dot punctuations for three-dots and four-dots (⁝ ⁘).
- silme and reversed silme spaced a little wider.
- U and O tehta (the hook-shaped diacritics) and acutes have been slightly enlarged.

0.6 : 4 Jan 2022
- Initial public release.


