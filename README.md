# Installation
```
pip install git+https://github.com/electiontables/electiontables
```

# Examples
```python
import electiontables

D = electiontables.load('...')
```

# API

# Dataset fields
electoral_id - ascii строка

region_name - unicode строка, человекочитаемое нормализованное название региона

region_code - ascii строка, короткий код региона (в редких случаях административной единицы). предполагается, что эти коды из ISO_3166-2, возможно, с небольшими расширениями

territory - unicode строка

election_name - unicode строка

voters_registered - int, количество избирателей в списке. Точнее: "число избирателей, внесенных в список избирателей на момент окончания голосования"

voters_voted_at_station - int, количество бюллетеней, выданных на участке. Точнее: "число бюллетеней, выданных в помещении в день голосования"

voters_voted_outside_station - int, количество бюллетеней, выданных вне участка. Точнее: "число бюллетеней, выданных вне помещения в день голосования"

voters_voted_early - int, количество бюллетеней, выданных досрочно. Точнее: "число бюллетеней, выданных досрочно"

ballots_valid - int, количество действительных бюллетеней. Точнее: "число действительных бюллетеней"

ballots_invalid - int, количество недейтсвительных бюллетеней. Точнее: "число недействительных бюллетеней"

voters_voted - int
