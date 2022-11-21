# Ohjelmistotekniikka

## Lasten matematiikkasovellus


### Dokumentaatio

- [Työaikakirjnapito](https://github.com/nikitaessine/ot-harjoitustyo/blob/master/dokumentaatio/tyokirjanpito.md)

- [Vaatimusmäärittely](https://github.com/nikitaessine/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

- [Changelog](https://github.com/nikitaessine/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

### Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
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

