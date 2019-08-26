import re

fields = dict(
    region_code = r'[A-Z]{2}(-[A-Z0-9]{2,3})?',
    date = r'\d{4}-\d{2}-\d{2}',
    election_name = r'[a-z]+',
    extra = r'([A-Z]+)[=]?([a-z0-9+]+)'
)

alias = dict(district = ['D'], territory = ['T'], station = ['V'])

def parse(electoral_id):
  return dict((k, f) if k != 'extra' else (([k for k, a in alias.items() if m.group(1) in a] + [k])[0], val(m.group(2))) for f in electoral_id.split('_') for k, r in fields.items() for m in [re.fullmatch(r, f)] if m is not None)

def make(region_code = None, date = None, election_name = None, district = None, territory = None, station = None, **extra):
  val = lambda val, int_or_str = (lambda x: int(x) if x.isdigit() else x): list(map(int_or_str, val.split('+'))) if '+' in val else int_or_str(val)
  spacize = lambda o: str(o).replace(' ', '-')
  plusize = lambda k, val: alias.get(k, [k])[0] + '+'.join(map(spacize, val if isinstance(val, list) else [spacize(val)]))
  return '_'.join(str(f) for f in [region_code, plusize('district', district) if district else None, plusize('territory', territory) if territory else None, plusize('station', station) if station else None, date, election_name] + [plusize(k, v) if v else None for k, v in extra.items()] if f is not None)
