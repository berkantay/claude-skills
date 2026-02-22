# Breakpoint Reference

## Standard Breakpoints (Mode 1)

| Width | Name | Real-World Devices | CSS Context |
|-------|------|--------------------|-------------|
| 320px | Mobile S | iPhone SE, Galaxy S series (older) | `max-width: 374px` |
| 375px | Mobile | iPhone 12/13/14, Pixel 5 | `375px - 767px` typical mobile range |
| 768px | Tablet | iPad portrait, Galaxy Tab | Common `md` breakpoint |
| 1024px | Tablet L / Desktop S | iPad landscape, small laptops | Common `lg` breakpoint |
| 1280px | Desktop | 13" MacBook, standard laptops | Common `xl` breakpoint |
| 1440px | Desktop L | 15" MacBook, external monitors | Common `2xl` breakpoint |
| 1920px | Full HD | 1080p monitors, most desktop users | Full HD standard |
| 2560px | QHD / 2.5K | 27" monitors, iMac, ultrawide | High-res desktop |

## Sweep Breakpoints (Mode 2)

Every 160px from 320 to 2560. The 160px interval is chosen because it's wide enough to be meaningful but narrow enough to catch transitional breaks.

| Width | What typically breaks here |
|-------|--------------------------|
| 320px | Minimum viable mobile |
| 480px | Larger phones in portrait, small phones in landscape |
| 640px | Phablets, large phones in landscape |
| 800px | Small tablets, awkward gap between mobile and tablet layouts |
| 960px | Tablet territory -- menus may be mid-transition |
| 1120px | **Common break zone** -- desktop nav may not fit, columns may collapse unevenly |
| 1280px | Standard laptop -- sidebar + content layouts start working |
| 1440px | Comfortable desktop, most designs optimise for this |
| 1600px | Wide desktop -- check for excessive whitespace or stretched content |
| 1760px | Uncommon width, catches missing max-width constraints |
| 1920px | Full HD -- the "normal" desktop |
| 2080px | Between FHD and QHD -- rarely tested, often reveals issues |
| 2240px | Wide monitor territory |
| 2400px | Near-ultrawide |
| 2560px | QHD / 2.5K -- content should still be readable and centred |

## Trouble Zones

These ranges are where the most bugs hide:

### 768-1024px (Tablet Transition)
Where responsive layouts switch from single-column to multi-column. Navigation bars toggle between hamburger and full menu. Sidebars appear/disappear. Most CSS frameworks have a breakpoint here but real content often doesn't fit cleanly.

### 1024-1280px (Small Laptop)
Designers working on 27" monitors rarely see this. Sidebars may squeeze content. Data tables may overflow. Horizontal navigation items may wrap to a second line.

### 1440-1920px (Desktop Scaling)
Content may stretch too wide without max-width constraints. Excessive whitespace in centred layouts. Images may upscale and blur. Multi-column layouts may create overly wide columns that harm readability.

### 1920-2560px (High-Res Desktop)
Missing max-width on containers. Text line lengths exceeding comfortable reading width (~75 characters). Layout elements floating in a sea of whitespace. Background images not covering properly.

## Viewport Height

Default viewport height is **900px** for all checks. This represents a typical browser window on a desktop monitor with toolbar chrome. It's important for:
- Determining what's "above the fold"
- Testing sticky header/footer behaviour
- Checking whether CTAs appear without scrolling

For mobile breakpoints (320-375px), the height still matters for above-the-fold checks even though physical phone screens vary (667px to 932px).
