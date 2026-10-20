# Gobos

What each colored gobo looks like, checked on the lights on 2026-10-20 (Tony watching, CAL Test in Bank 4). Both fixtures make their color with colored glass gobos in front of a white LED, so in the custom profiles the gobo channel is mapped as a **color wheel**: a loop that asks for a color gets the gobo of that color.

## Scan 110s (L1-L3, R1-R3), ch6
| Value | Gobo | Color seen | Shape (QRG picture) | Wheel slot in "Intimidator Scan 110 Claude" |
|---|---|---|---|---|
| 0-28 | open | white | round beam | #ffffff |
| 29-56 | 1 | yellow | three curved blades | #ffff00 |
| 57-85 | 2 | red | spiral | #ff0000 |
| 86-113 | 3 | green | slanted bars | #00ff00 |
| 114-142 | 4 | dark blue | sunburst rays | #0000ff |
| 143-170 | 5 | tricolor (orange, green, blue) | two swirls | #808000 olive (placeholder, reach on purpose) |
| 171-199 | 6 | purple / UV | dot cluster | #8000ff |
| 200-227 | 7 | orange | shattered glass | #ff8000 |
| 228-255 | 8 | cyan + magenta | broken ring | #ff00aa (pink) |

Sources agree: a Pioneer DJ community list Tony found, and SoundSwitch's own stock "Intimidator Scan 110 (Colors)" profile (which has orange, cyan and magenta squeezed into gobo 7's range by mistake).

## Vortex (F Vortex 405), ch3
| Value | Gobo | Color seen | Shape (manual) | Wheel slot in "Vortex Claude" |
|---|---|---|---|---|
| 0-7 | open | white | big spots | #ffffff |
| 8-13 | 1 | red | tri-bar | #ff0000 |
| 14-19 | 2 | blue | hazard | #0040ff |
| 20-25 | 3 | green | triangle | #00ff00 |
| 26-31 | 4 | yellow | shattered glass | #ffc850 |
| 32-37 | 5 | tricolor | quad dots | #808000 olive (placeholder) |
| 38-43 | 6 | purple (manual says magenta) | square rays | #8000ff |
| 44-49 | 7 | light teal | four-point star | #00c8ff |
| 50-55 | 8 | lime / yellow-green | multi dots | #a0ff40 |
| 56-64 | 9 | white | small dots | #aac8ff |

65-127 are the same gobos with shake, and 128-255 is auto gobo change. The Color Wheel mapping leaves those out.

## Matching colors across the two
| Color | Scan 110 | Vortex |
|---|---|---|
| Red | G2 spiral | G1 tri-bar |
| Yellow | G1 blades | G4 shattered glass |
| Green | G3 bars | G3 triangle |
| Blue | G4 sunburst | G2 hazard |
| Purple | G6 dots | G6 square rays |
| Multicolor | G5 swirls | G5 quad dots |
| Orange | G7 shattered glass | none (lands on red or yellow) |
| Cyan / teal | G8 ring (with magenta) | G7 star |
| Lime | none | G8 dots |

## Ideas to discuss (not decided)
- **Paired palettes:** a loop color lands on matching gobos on both fixtures at once, for example green bars on the floor plus a green triangle spray from the Vortex.
- **Multicolor as a moment:** olive on the 110 and Vortex tracks only (not the Main Track) puts both multicolor gobos up together for a drop or a party peak.
- **The ring (110 G8) as a frame:** a lone 110 putting the cyan and magenta ring on the floor in a breakdown.
- **Textures on the floor:** six 110s in one gobo pointed at Lanes make a carpet; mixing gobos within a group breaks it up.
- **Wheel travel:** a color change makes the wheel pass through the gobos in between. Snap it with ch9 110-129 (blackout while the gobo wheel moves) or use the scroll as a deliberate transition.
- **Vortex shake (65-127)** isn't reachable through the color wheel; it would need an attribute cue or a second mapping.
