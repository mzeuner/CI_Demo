Using Github Actions for Continuous Integration
===============================================

This dummy repo is supposed to show how to get started with Github actions if you want to
use it for continuous integration (CI) in your projects. Below are some links to the relevant pages
where you can learn more about the topic and find more example code.

Learning Github Actions
-----------------------
Suppose we have a python script `Experiment.py` on which the team is working in the repo
and for which some unit tests have been written in `Experiment_test.py`. In order to make sure
that the script is still working whenever some changes are pushed we want Github to
run the tests automatically and tell us if some of the tests failed.

If we are working in a bigger team where the developers have to make pull requests
from different branches, we might want to require that Github runs the tests
on the new branch before we can even merge the pr.

The main addition to our repo is a `.yaml` or `.yml` file that should be put
in a separate directory `.github/workflows`.
Github has a good tutorial, look no further than here

https://docs.github.com/en/actions/quickstart

and here

https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions


Actions for Python
------------------
The support for python in Github actions is pretty good and setting it up is relatively straightforward.
The basics can be found here

https://docs.github.com/en/actions/guides/building-and-testing-python

or here

https://docs.github.com/en/actions/guides/building-and-testing-nodejs-or-python?langId=py

If you are using some special version of python that is not the default of your runner,
you can install it like this:
https://github.com/marketplace/actions/setup-python

I really recommend working through the guide and make good use of features like caching
dependencies to reduce the runtime of your workflows etc.


Actions for Java
----------------
Things are tiny bit more complicated here due to all the different versions of java out there.
To be continued if some groups want to write their project in java and use Github actions...
