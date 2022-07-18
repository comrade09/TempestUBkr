from Tempest.core.database.postgres.afk_sql import AFKSQL
from Tempest.core.database.postgres.notes_sql import NOTESSQL
from Tempest.core.database.postgres.pmpermit_sql import PMPERMITSQL
from Tempest.core.database.postgres.dv_sql import DVSQL
from Tempest.core.database.postgres.welcome_sql import WELCOMESQL




class Database(
    AFKSQL,
    NOTESSQL,
    PMPERMITSQL,
    DVSQL,
    WELCOMESQL
    ):
    pass
