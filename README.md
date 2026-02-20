# hyouiyoon.github.io

Personal academic website of **Hyoui Yoon**.

M.S. student at [Computational Materials Modeling & Design Lab](https://sites.google.com/view/sangryunlab), Ewha Womans University.

**Research interests:** Data-driven design, Design optimization, Multiphysics modeling

## Built with

- [Jekyll](https://jekyllrb.com/) + [al-folio](https://github.com/alshedivat/al-folio) theme
- Hosted on [GitHub Pages](https://pages.github.com/)

## News Copy Automation

Generate polished news copy (title + description) and optionally create `_news/<year>/*.md` in one command.

```bash
python3 bin/news_update_generator.py \
  --event-type publication \
  --subject "Layered Hybrid Lattice Architectures for Energy Absorption" \
  --venue "Materials & Design" \
  --date 2026-02-20 \
  --lang en \
  --write-file
```

For scholarship/award/presentation updates, switch `--event-type` and pass `--org` or `--venue` as needed.

## License

The theme is available as open source under the terms of the [MIT License](LICENSE).
