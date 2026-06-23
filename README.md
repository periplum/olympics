<table align="center">
<tr><td align="center" width="640">

## ▶&nbsp; [Open the interactive map](https://periplum.github.io/olympics/)

🌍 &nbsp;Every Olympic host city, 1896–2032 — ☀️ Summer · ❄️ Winter

</td></tr>
</table>

# olympics

[![Built with Periplum](https://img.shields.io/badge/built_with-Periplum-4da3ff)](https://periplum.js.org)

Every Summer and Winter Olympic host city in chronological order, using Periplum's
`statusIcons` (☀️ Summer, ❄️ Winter). Press play to watch the Games travel the globe, or
drag the date slider.

## Data & updates

The host list is curated in [`build.py`](build.py), which emits `data.json` (Python
standard library only):

```sh
python build.py > data.json      # add a new host to the GAMES list, then re-run
```

### GitHub Actions

[`.github/workflows/refresh-data.yml`](.github/workflows/refresh-data.yml) regenerates
`data.json` **yearly** (and on manual *Run workflow*) and uploads it as a build
**artifact**. The periplum org blocks Actions from pushing or opening PRs, so download the
artifact and commit it.

---

Built with [Periplum](https://periplum.js.org) · [periplum.js.org](https://periplum.js.org)
