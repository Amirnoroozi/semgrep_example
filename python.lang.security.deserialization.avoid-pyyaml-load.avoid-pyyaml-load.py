import yaml
#ruleid:avoid-pyyaml-load
yaml.unsafe_load("!!python/object/new:os.system [echo EXPLOIT!]")
def thing(**kwargs):
    #ruleid:avoid-pyyaml-load
    yaml.unsafe_load("!!python/object/new:os.system [echo EXPLOIT!]", **kwargs)
def other_thing(**kwargs):
    yaml.load("!!python/object/new:os.system [echo EXPLOIT!]", Loader=yaml.Loader, **kwargs)
def other_thing_two(**kwargs):
    yaml.load("!!python/object/new:os.system [echo EXPLOIT!]", Loader=yaml.UnsafeLoader, 
    **kwargs)
def other_thing_three(**kwargs):
    yaml.load("!!python/object/new:os.system [echo EXPLOIT!]", Loader=yaml.CLoader, 
def other_thing_four(**kwargs):
    yaml.load_all("!!python/object/new:os.system [echo EXPLOIT!]", Loader=yaml.Loader, 
def other_thing_five(**kwargs):
    yaml.load_all("!!python/object/new:os.system [echo EXPLOIT!]", Loader=yaml.
    UnsafeLoader, **kwargs)
def other_thing_six(**kwargs):
    yaml.load_all("!!python/object/new:os.system [echo EXPLOIT!]", Loader=yaml.CLoader, 
def this_is_ok(stream):
    #ok:avoid-pyyaml-load
    return yaml.load(stream, Loader=yaml.CSafeLoader)
def this_is_also_ok(stream):
    return yaml.load(stream, Loader=yaml.SafeLoader)
def this_is_additionally_ok(stream):
    return yaml.load_all(stream, Loader=yaml.CSafeLoader)
def this_is_ok_too(stream):
    return yaml.load_all(stream, Loader=yaml.SafeLoader)
def this_is_ok_as_well(stream):
    return yaml.load(stream, Loader=yaml.BaseLoader)
def this_is_ok_too_two(stream):
    return yaml.load_all(stream, Loader=yaml.BaseLoader)
def check_ruamel_yaml():
    from ruamel.yaml import YAML
    yaml = YAML(typ="rt")
    # ok:avoid-pyyaml-load
    yaml.load("thing.yaml")
    yaml.load_all("thing.yaml")
