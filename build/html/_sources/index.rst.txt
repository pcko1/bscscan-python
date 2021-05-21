.. bscscan-python documentation master file, created by
   sphinx-quickstart on Fri May 21 14:47:20 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to bscscan-python's documentation!
==========================================

This is an unofficial ``Python 3.8+`` wrapper for the endpoints provided by `BscScan`_.

It supports asynchronous calls and it is available on PyPI.

Powered by `BscScan APIs`_.

Disclaimer: The author assumes no responsibility neither for the way this software is used
nor for its behavior. The code is open-source and everyone is encouraged to inspect it before
integrating into their products.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Cite
===========

   @misc{Kotsias2021,
   author = {Kotsias, P.C.},
   title = {pcko1/bscscan-python},
   year = {2021},
   publisher = {Zenodo},
   url = {https://github.com/pcko1/bscscan-python},
   doi = {10.5281/zenodo.4580473}
   }


FAQ
============

* Why async?

   Because your application might not want to wait for BscScan to respond before
   proceeding to the next step. Async calls execute in the background.

* How do I use method *X*?

   Kindly read the documentation of this package since detailed examples have been added for all methods.

* Can you add support for *X*?

   If (and only if) *X* is a method on BscScan.com that I have missed, kindly open an issue.

* Is a particular functionality provided?

   Kindly read the documentation of this package. If it's not there, it's not provided.

* May I suggest some improvements?

   Absolutely, PRs are more than just welcome. Just make sure the unittests pass and that coverage
   remains at 100% in order for me to accept it.

* Are you affiliated with BscScan.com?

   Not at all. I independently composed this package for my daily tasks and thought of open-sourcing it.

* Are you open for collaboration?

   Surprisingly, I have received several emails asking for collaboration. I am currently working full-time on my 
   own projects so unfortunately I cannot promise anything - yet, do reach out :)

* How can I reach you?

   My contact details may be found at https://pankotsias.com. For professional matters, kindly do prioritize LinkedIn.




.. _BscScan: https://bscscan.com
.. _BscScan APIs: https://bscscan.com/apis
