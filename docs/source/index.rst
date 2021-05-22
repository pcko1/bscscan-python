.. bscscan-python documentation master file, created by
   sphinx-quickstart on Fri May 21 14:47:20 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to bscscan-python's documentation!
==========================================

This is an unofficial ``Python >=3.8`` wrapper for the endpoints provided by `BscScan`_.

It supports asynchronous calls and it is available on `PyPI`_. Powered by `BscScan APIs`_.

For a detailed list of all methods and their arguments, please refer to :doc:`this page <bscscan.modules>`.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Install
=======

There are two ways to install this package; from PyPI or from source.

Install from PyPI as::

   pip install bscscan-python

Install from source as::

   pip install git+https://github.com/pcko1/bscscan-python.git@stable


Basic Usage
===========

This package supports both synchronous and asynchronous calls.

Both implementations need to be run inside a content manager, which is the 
*de facto pythonic* way for resource allocation.

Async client (default)::

   from bscscan import BscScan

   async with BscScan(YOUR_API_KEY) as client:
      print(await client.get_bnb_last_price())

Sync client::

   from bscscan import BscScan

   with BscScan(YOUR_API_KEY, asynchronous=False) as client:
      print(client.get_bnb_last_price())


Using an existing ``Session`` object   
====================================

It is possible that you might already have a running ``Session`` object in your code.
If that's the case, you can always pass it to ``BscScan`` with a slightly different instantiation.

For the async client::

   from aiohttp import ClientSession
   from bscscan.core.async_client import AsyncClient as BscScan

   # you can substitute the session with your aiohttp.ClientSession
   client = await BscScan.from_session(api_key=YOUR_API_KEY, session=ClientSession())

For the sync client::

   from requests import Session
   from bscscan.core.sync_client import SyncClient as BscScan

   # you can substitute the session with your requests.Session
   client = BscScan.from_session(api_key=YOUR_API_KEY, session=Session())

In this case, you don't need to use a context manager because it is assumed 
that you will close the open session somewhere else in your code.


Migration from ``v1.0.0``
=========================

The most significant change between versions 1 and 2 is the instantiation of the 
client. You are highly advised to modify that part in your existing scripts by
following the examples shown above. The underlying API calls are mostly unaffected.
Refer to the next section for the exhaustive changelog. 

If you still want to use the old implementation, you can always grab it from PyPI::

   pip install bscscan-python==1.0.0


Changelog (``v2.0.0``)
======================

#. Added async client
#. All clients should now be instantiated within a context manager
#. Added BEP721 endpoints in ``bscscan.modules.Accounts``
#. ``block_no`` in ``client.get_block_reward_by_block_number`` is now ``int``
#. Added more methods in ``bscscan.modules.Stats``
#. Added documentation for every method

Disclaimer
==========

The author assumes no responsibility for the way this software is used, for its 
behavior or for any loss of funds. The code is open-source and everyone is 
encouraged to inspect it before integrating it into their own products.


Cite
====

Please cite this software as:

   Kotsias, P. C., pcko1/bscscan-python: v1.0.0. *https://github.com/pcko1/bscscan-python (2021)*. 
   doi:10.5281/zenodo.4580473

or in ``bibtex``::

   @misc{Kotsias2021,
      author = {Kotsias, P.C.},
      title = {pcko1/bscscan-python},
      year = {2021},
      publisher = {Zenodo},
      url = {https://github.com/pcko1/bscscan-python},
      doi = {10.5281/zenodo.4580473}
   }


FAQ
===

* Why async?

   Because your application might not want to wait for BscScan to respond before
   proceeding to the next line. Async calls execute in the background and are 
   ideal for I/O bound scenarios such as HTTP requests.

* How do I use method *X*?

   Kindly read the :doc:`documentation <bscscan.modules>` of this package since 
   detailed examples have been added for all methods.

* Can you add support for *X*?

   If (and only if) *X* is a method on BscScan.com that I have missed, please 
   open a GitHub `issue`_.

* Is a particular functionality provided?

   Kindly read the :doc:`documentation <bscscan.modules>` of this package. 
   If it's not there, it's not provided.

* May I suggest some improvements?

   Absolutely, PRs are more than just welcome. Just make sure the unittests pass 
   and that coverage remains at 100% in order for me to accept it.

* Are you affiliated with BscScan.com?

   Not at all. I independently composed this package for my daily tasks and 
   thought of open-sourcing it.

* Are you open for collaboration?

   Surprisingly, I have received several emails asking for collaboration. 
   I am currently working full-time on my own projects so unfortunately 
   I cannot promise much - yet, do reach out :)

* How can I reach you?

   My contact details may be found at https://pankotsias.com. 
   For professional matters, kindly do prioritize LinkedIn.


.. _BscScan: https://bscscan.com
.. _BscScan APIs: https://bscscan.com/apis
.. _PyPI: https://pypi.org/project/bscscan-python/
.. _issue: https://github.com/pcko1/bscscan-python/issues/new
