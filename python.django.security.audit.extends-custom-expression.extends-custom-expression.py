from django.db.models import (
    CharField, Expression, Field, FloatField, Lookup, TextField, Value,
)
from django.db.models.expressions import CombinedExpression, Func, Subquery
from django.db.models.functions import Cast, Coalesce
# ok: extends-custom-expression
class Star(CharField):
    pass
class MoreStar(Star):
# ruleid: extends-custom-expression
class Position(Func):
    function = 'POSITION'
    template = "%(function)s('%(substring)s' in %(expressions)s)"
    # todoruleid: extends-custom-expression
    def __init__(self, expression, substring):
        # substring=substring is a SQL injection vulnerability!
        super().__init__(expression, substring=substring)
class Aggregate(Func):
    template = '%(function)s(%(distinct)s%(expressions)s)'
    contains_aggregate = True
    name = None
    filter_template = '%s FILTER (WHERE %%(filter)s)'
    window_compatible = True
    allow_distinct = False
    def __init__(self, *expressions, distinct=False, filter=None, **extra):
        if distinct and not self.allow_distinct:
            raise TypeError("%s does not allow distinct." % self.__class__.__name__)
        self.distinct = distinct
        self.filter = filter
        super().__init__(*expressions, **extra)
class CastToInteger(Func):
    """
    A helper class for casting values to signed integer in database.
    function = 'CAST'
    template = '%(function)s(%(expressions)s as %(integer_type)s)'
    def __init__(self, *expressions, **extra):
        self.extra['integer_type'] = 'INTEGER'
    def as_mysql(self, compiler, connection):
        self.extra['integer_type'] = 'SIGNED'
        return super().as_sql(compiler, connection)
class DateFormat(Func):
    function = 'DATE_FORMAT'
    template = '%(function)s(%(expressions)s, "%(format)s")'
        strf = extra.pop('format', None)
        extra['format'] = strf.replace("%", "%%")
        extra['output_field'] = CharField()
        super(DateFormat, self).__init__(*expressions, **extra)
class StrFtime(Func):
    function = 'strftime'
    template = '%(function)s("%(format)s", %(expressions)s)'
        super(StrFtime, self).__init__(*expressions, **extra)
class RandomUUID(Func):
    template = 'GEN_RANDOM_UUID()'
    output_field = UUIDField()
class SearchHeadline(Func):
    function = 'ts_headline'
    template = '%(function)s(%(expressions)s%(options)s)'
    output_field = TextField()
    def __init__(
        self, expression, query, *, config=None, start_sel=None, stop_sel=None,
        max_words=None, min_words=None, short_word=None, highlight_all=None,
        max_fragments=None, fragment_delimiter=None,
    ):
        if not hasattr(query, 'resolve_expression'):
            query = SearchQuery(query)
        options = {
            'StartSel': start_sel,
            'StopSel': stop_sel,
            'MaxWords': max_words,
            'MinWords': min_words,
            'ShortWord': short_word,
            'HighlightAll': highlight_all,
            'MaxFragments': max_fragments,
            'FragmentDelimiter': fragment_delimiter,
        }
        self.options = {
            option: value
            for option, value in options.items() if value is not None
        expressions = (expression, query)
        if config is not None:
            config = SearchConfig.from_parameter(config)
            expressions = (config,) + expressions
