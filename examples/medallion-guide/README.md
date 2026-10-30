# Medallion guide diagrams

The `.mmd` files are the editable Mermaid sources for the diagrams in
`_posts/2026-10-09-medallion-software-guide.md`.
The matching SVG files are stored in `images/medallion-guide/`.

The article uses the saved SVGs rather than live mermaid.ink URLs. Readers
can load every diagram directly from the website, without a separate
rendering service.

The Mermaid settings use Arial and native SVG text labels to avoid
browser-dependent clipping of HTML labels. The saved SVGs omit the
renderer’s unused external icon-font import.

To update a diagram, edit its `.mmd` source and export a matching SVG with
a Mermaid renderer. Keep both files together in the change. Check that
all node labels appear in the SVG and that the built article displays
all five diagrams at desktop and mobile widths.
