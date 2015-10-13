# Rolodex
simple rolodex application

## Setup Environment:

1. Create a virtual env (let's call it 'rolo') on your machine with Python 2.7.x
2. switch to your 'rolo' virtual env
3. Untar the tar.gz file and cd /path/to/rolodex
4. Then run 
		
		python setup.py develop


## Usage
After setting up your environment and dependencies,

1. cd /path/to/rolodex/rolodex, run this:
		
		python roldy.py

	This will spit a message on stdout that looks something like this:

      output available at: /path/to/rolodex/rolodex/data/output.json

2. An input data file (data.in) and a configuration file (config.yaml) reside in /path/to/rolodex/rolodex/data
		
3. You can change the config.yaml file to add more patterns


## Tests
You can simply run nosetests from /path/to/rolodex. I wrote tests to only cover the actual rolodex logic.
If all goes well, it should appear like this

(rolo)$ cd /path/to/rolodex
(rolo)$ nosetests
test_invalid_cases (rolodex.tests.test_roldy.TestRolodex) ... ok
test_valid_cases (rolodex.tests.test_roldy.TestRolodex) ... ok

Name               Stmts   Miss  Cover   Missing
------------------------------------------------
rolodex.py             0      0   100%   
rolodex/roldy.py      56      9    84%   30-32, 73-82, 86
------------------------------------------------
TOTAL                 56      9    84%   
----------------------------------------------------------------------
Ran 2 tests in 0.096s

OK


## Notes
1. There's a config.yaml file holding different patterns and formats.
   So that, we can always add/remove patterns based on our needs.

2. Name parsing can be very tricky.
	
   We can always expand the scope of name parsing by adding patterns of our choice or generalizing the existing patterns.
   
   For example, instead of saying this for first name and last name

   ([a-z]+) ([a-z]+)

   I can say something like this

   ([a-z\s]+)

   But now we are giving a chance to put multiple words. And that might not always be good.

   So, it's a matter of personal choice and what the requirments are.

   I strictly adhered to the patterns that I found in the data set provided to me in the data.in file.
