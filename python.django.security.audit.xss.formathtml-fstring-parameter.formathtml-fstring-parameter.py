from django.utils.html import format_html
planet = "world"
markup = "<marquee>" + planet
#############################################################
# ok: formathtml-fstring-parameter
print(format_html("hello {}", markup))
print(format_html("hello {}", "<marquee>world"))
print(format_html("hello {}", "<marquee>" "world"))
print(format_html("hello {}", "<marquee>" + "world"))
print(format_html("hello {}", f"<marquee>{planet}"))
print(format_html("hello {}", "<marquee>%s" % planet))
print(format_html("hello {}", "<marquee>{}".format(planet)))
print(format_html("hello " "{}", "<marquee>world"))
print(format_html("hello " + "{}", "<marquee>world"))
# ruleid: formathtml-fstring-parameter
print(format_html("hello %s" % markup))
print(format_html(f"hello {markup}"))
print(format_html("hello {}".format(markup)))
print(format_html("hello %s {}" % markup, markup))
print(format_html(f"hello {markup} {{}}", markup))
print(format_html("hello {} {{}}".format(markup), markup))
