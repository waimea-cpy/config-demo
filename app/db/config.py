#============================================================================
# Database schema and seed data configuration
#============================================================================


#----------------------------------------------------------------------------
# Table definitions
#----------------------------------------------------------------------------
# Define your tables with a name, a schema and optional seed/sample data,
# using this format, and then add the tables to the Table Registry below:
#
# class TableName:
#     NAME      = "name"
#     SCHEMA    = "CREATE TABLE name (...)"
#     SEED_DATA = "INSERT INTO name (...)" or None
#----------------------------------------------------------------------------

class MbTable:

    NAME = "mbs"

    SCHEMA = """
        CREATE TABLE mbs (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            socket TEXT NOT NULL,
            ram    TEXT NOT NULL
        )
    """

    SEED_DATA = """
        INSERT INTO mbs (name, socket, ram)
        VALUES
            ("ASUS Uber",    "BIG",   "DDR7"),
            ("ASUS Weak",    "SMALL", "DDR1"),
            ("ASUS Stellar", "BIG",   "DDR8")
    """

class CpuTable:

    NAME = "cpus"

    SCHEMA = """
        CREATE TABLE cpus (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            socket TEXT NOT NULL
        )
    """

    SEED_DATA = """
        INSERT INTO cpus (name, socket)
        VALUES
            ("Intel Plopper", "SMALL"),
            ("Intel Ripper",  "BIG"),
            ("AMD Crud",      "SMALL"),
            ("AMD Zoomer",    "BIG")
    """

class RamTable:

    NAME = "rams"

    SCHEMA = """
        CREATE TABLE rams (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            type   TEXT NOT NULL
        )
    """

    SEED_DATA = """
        INSERT INTO rams (name, type)
        VALUES
            ("Jim's Awesome RAM",    "DDR8"),
            ("Jim's Special RAM",    "DDR7"),
            ("Jim's Fast RAM",       "DDR5"),
            ("Jim's Basic RAM",      "DDR1"),
            ("Powerful Awesome RAM", "DDR8"),
            ("Powerful Special RAM", "DDR7"),
            ("Powerful Fast RAM",    "DDR5"),
            ("Powerful Basic RAM",   "DDR1")
    """

#----------------------------------------------------------------------------
# Table registry
#----------------------------------------------------------------------------
# Register all of your tables by adding them to the TABLES list here:
#
# TABLES = [
#     Table1,
#     Table2,
#     etc.
# ]
#
# Note: The table order is important - Create the tables that have
#       foreign keys AFTER the tables they link to have been created
#----------------------------------------------------------------------------

TABLES = [
    MbTable,
    CpuTable,
    RamTable
]

