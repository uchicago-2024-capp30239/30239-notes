# Narratives

## CAPP 30239

---

## Today

- What types of data visualization narratives exist?
- Practical advice on creating publications & pages.
- Narrative Examples

---

## Crafting a Narrative

**Narrative** = **Visualization** + **Context**

### Benefits

- More engaged audience.
    - Greussing & Boomgaarden, Digital Journalism 2019.
- Better learning outcomes.
    - Mayer, Multimedia Principles, 2005.
- Promote active reading.
    - Victor, Explorable Explanations, 2011.
- Persuasiveness of data.
    - Murray, Data Visualization And The Power Of Persuasion, 2019.

---

## Storytelling

Instead of a loosely connected series of images, take reader on a journey with a beginning, middle, and end.

- Beginning: Required Context, Pose Questions
- Middle: Exposition & Exploration
- End: Conclusion and/or Further Questions

---

## Risks

**Oversimplification.** Constraints of format can lead to the need to simplify, finding the right balance requires skill, practice, and knowledge of audience.

**Bias.** All narratives require interpretation, which can be a source of bias. We should not compromise on **graphical integrity** to make our point, or suggest conclusions that are not supported by the data.

---

## News Article Format

**Lede/Lead** - Opening paragraph. Summarize key ideas & grab attention.
**"Nut Graf"** - Nutshell paragraph. Immediately follows lead. Gives overview of why topic is important, and introduce key ideas to be explored in article.

"**Inverted Pyramid**"

![bg right fit](pyramid.svg)

Other Formats: <https://en.wikipedia.org/wiki/Article_structure>

TODO: examples

---

## Medium is the Message

The nature of a narrative is shaped by (dominated by?) the medium chosen.

Marshall McLuhan, Understanding Media: The Extensions of Man, 1964.

---

## Infographic

Typically a single-page image with an arrangement of graphics, tables, and brief narratives.

Typically aimed at general audiences, easy to share online, can be designed to work well in print.

TODO: examples

---

## Live Presentation

A live presentation with slides.

Special consideration should be given to legibility from a distance.

If detailed visualizations play a role: consider print versions.

TODO: examples

---

## Animations & Videos

Animation can be used to show change, uncertainty, or relationships.

Video can blend presentation with commentary and narrative.

### Examples

- [The best stats you've ever seen - Hans Rosling](https://www.ted.com/talks/hans_rosling_the_best_stats_you_ve_ever_seen?subtitle=en)
TODO: examples

---

## Interactive Stories

Take advantage of web as a medium.

Can seamlessly blend text, images, audio and video, and interactive elements.

- [NYT Snow Fall](https://www.nytimes.com/projects/2012/snow-fall/index.html#/?part=tunnel-creek)
TODO: examples

---

## Interactive Articles

TODO: 5 affordances

---

## What Skills Do You Need?

- Writing
- Design
- Programming (particularly for interactives)
- Subject-matter expertise

---

## SVG vs PNG vs JPG

- **SVG** - Scalable Vector Graphics format.
- **PNG** - Lossless raster image format. Should be preferred if SVG is not an option.
- **JPG** - Image format that uses compression, suitable for photographs but not fine details in visualizations.

TODO: images

---

## Document Formats

- **PDF** - Portable Document Format - A vector-based format aimed at entire documents. PDF documents are aligned to paper sizes, great for printing, but less flexible on modern devices.
- **HTML** - HyperText Markup Language - The language of the web, focused on *semantics* over layout. A document can appear differently on different devices.
- **CSS** - Cascading Style Sheets - A *styling* language that, when applied to an HTML document controls visual appearance.
- **Markdown** - Simplified markup language that can be converted to HTML or PDF with various tools. Offers **much** less control over formatting than other options.

---

## In Practice

1. Most professional data visualization starts with data-driven tools (code-driven like Altair or no-code like Tableau), which are then exported as SVG.

2. Those SVGs will then be embedded in a larger graphic or HTML page.

3. Export/render to final form(s):
  - For web presentation: HTML/CSS will be the final form. If interactivity is at play, JavaScript will be a part of the process.
  - For print or PDF: The intermediate format used by a print design tool will be exported to a PDF of the appropriate size & resolution.


---

## Tools: Typesetting Languages

- **LaTeX** - PDF-focused, almost anything via plugins/pandoc.
    - [Overleaf](https://overleaf.com) - online editor and compiler.
    - [Tectonic](https://tectonic-typesetting.github.io/en-US/) - local LateX compiler.
- **[Typst](https://typst.app)** - PDF-focused, (HTML coming soon).
- **[Quarto](https://quarto.org)** - Can use mix of Markdown, Python, R, and Julia.  Jupyter notebook compatible.  Can generate PDFs or HTML from same source document.

<!--
**LaTeX** is the most widely used in academic & scientific circles. It is a document typesetting language designed originally for Computer Science text.  The author, Donald Knuth, created the original (TeX) so he could typeset his magnum opus, *The Art of Computer Programming*.  The easiest way to work with LaTeX is to use , an online editor & compiler. Many versions exist that can be run locally, such as 
-->

---

## Tools: Vector Graphics Editors

- **[Inkscape](https://inkscape.org)** - Free & Open Source SVG editor. My recommendation for this class if you don't have prior experience with other options.
- **Adobe Illustrator** - Vector graphics editor, part of Adobe Creative Suite. Dominant option for many years. (Most expensive.)
- **Affinity Designer** - Competitor to Illustrator, much cheaper, full-featured, and gaining popularity because of Adobe's subscription model & business practices.

### Honorable Mentions

- **BoxySVG** - Online/browser-based SVG editor.
- **Canva** - Popular for infographics, collection of free clip art/etc. 


---

## References & Acknowledgements

- Thanks to Alex Kale.
- <https://www.forbes.com/sites/evamurray/2019/02/11/data-visualization-and-the-power-of-persuasion/>
