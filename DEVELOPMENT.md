
# Integration tests

If you wish to work on this project, and run integration tests whenever you
run `make test` or `python3 setup.py test`, you need to create a file called
`.crtools` in your home folder (must resolve as `~/.crtools`), and it must
contain the following:

.. code:: ini

  [API]
  api_key=<YOUR-API-KEY>

The API key can be acquired at https://developer.clashroyale.com

Note that the key is limited to a specific list of public IP addresses. This
is why integration tests aren't done on Travis -- we need a static IP.

# Development links

This project uses SonarQube for static analysis. The results of analysis
are at `SonarCloud <https://sonarcloud.io/dashboard?id=AaronTraas_pyroyale>`_.
The code quality and test coverage are a work in progress.
