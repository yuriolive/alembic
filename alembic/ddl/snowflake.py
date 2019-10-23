from sqlalchemy.ext.compiler import compiles

from .base import alter_table
from .base import ColumnName
from .base import format_column_name
from .impl import DefaultImpl


class SnowflakeImpl(DefaultImpl):
    __dialect__ = "snowflake"


@compiles(ColumnName, "snowflake")
def visit_column_name(element, compiler, **kw):
    return '%s RENAME COLUMN %s TO %s' % (
        alter_table(compiler, element.table_name, element.schema),
        format_column_name(compiler, element.column_name),
        format_column_name(compiler, element.newname),
    )
