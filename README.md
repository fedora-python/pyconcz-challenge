# Red Hat–PyCon CZ 2017 Coding Challenge

We have prepared 3 programming problems for you to solve. By competing, you may get a job at Red Hat, and the first three people with the most solved problems (ideally all three) win a prize!

## Rules

To solve the 3 problems you may use *only* the Python 3 programming language and its standard library, __no external libraries are allowed__. Your script must be compatible with Python 3.6 and also finish within 2 minutes on a reasonably powerful machine.

**Submit** your scripts through our [web interface](https://pyconcz.fedoralovespython.org/) before the **deadline on Friday at 14:00**.

We have prepared tests which you can use to verify that your solution is correct. However, after submission your script will be checked by more rigorous private tests to make it infeasible to exploit them.

## Problems

1. [Restricted sum](level1-restricted-sum/README.md)
2. [Brackets](level2-brackets/README.md)
3. [Build Order](level3-dependencies/README.md)

## How to & Testing

As a first step, clone this repository to your computer:

    $ git clone https://github.com/fedora-python/pyconcz-challenge.git

Inside the repository you will find three directories corresponding to the three problems, each containing a README for the problem, a file into which you should write your solution and two test files.

To run the tests, run the following command in the problem's directory:

    $ python3 -m pytest

Beware that the tests do not check whether your script terminates within the allotted 2 minutes.

## Contact

If you have any questions, contact us at the Red Hat booth or at python-maint@redhat.com.
