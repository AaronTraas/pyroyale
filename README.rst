==================================================
pyroyale -- Clash Royale API wrapper
==================================================

This is a tool for data from the official ClashRoyale developer API.
See https://developer.clashroyale.com to sign up for a developer account and
create an API key to use with this.

==================================================
Work in Progress
==================================================

You probably shouldn't use this yet. It's very much a work in progress. It's
also an incomplete implementation at this time. I've only implemented the few
API endpoints required for `crtools <https://github.com/AaronTraas/Clash-Royale-Clan-Tools>`_,
which are:

- /v1/clans/{clan_tag}
- /v1/clans/{clan_tag}/warlog
- /v1/clans/{clan_tag}/currentwar

I plan on implementing the entire API eventually, but it's not present at this time.

==================================================
Development links
==================================================

This project uses SonarQube for static analysis. The results of analysis
are at `SonarCloud <https://sonarcloud.io/dashboard?id=AaronTraas_pyroyale>`_.
The code quality and test coverage are a work in progress.
