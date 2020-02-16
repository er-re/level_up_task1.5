### Migrating data from a database with the aim of adding one calculated column

---
*Notes*
*   It is assumed that there are limitations in the resources.
therefore the solution extracts data using stream method in order to memory management.
*   we used Postgresql as database

**For running the script:**
1. Fill the database connection information on `engine.py`
2. Run `entity_class.py`. (It creates all table schemas)
3. Replace you desired number in the `factory.py` and run it to fill the database
4. Replace you acceptable chunk size in the `migrate.py` and run it for adding 'order' column incrementally.
