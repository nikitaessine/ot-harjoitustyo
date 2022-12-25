# Ohjelmistotekniikka

## Lasten matematiikkasovellus


### Dokumentaatio

- [Työaikakirjnapito](https://github.com/nikitaessine/ot-harjoitustyo/blob/master/dokumentaatio/tyokirjanpito.md)

- [Vaatimusmäärittely](https://github.com/nikitaessine/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

- [Arkkitehtuuri](https://github.com/nikitaessine/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

- [Changelog](https://github.com/nikitaessine/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

- [Testausdokumentti](https://github.com/nikitaessine/ot-harjoitustyo/blob/master/dokumentaatio/testausdokumentti.md)

- [Release](https://github.com/nikitaessine/ot-harjoitustyo/releases)

### Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

### Komentorivitoiminnot

#### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

#### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

#### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

#### Formatointi

Koodin formatointi onnistuu komennolla:

```bash
poetry run invoke format
```

#### Koodin staattinen analyysi

Koodin analyysi onnistuu komennolla:

```bash
poetry run pylint src
```

