# Election Results

Coding Challenge as per The Gaurdian's coding exercises [here](https://github.com/guardian/coding-exercises/tree/main/election-results).

Here's what you'll get, but I might come back and make this more robust, have it store properly in some sort of db, even sqlite,
and add some IaC and CI/CD, but for now, here's an example of covering the base case talked about in the above referenced `README.md`:
```
^_^[jhitch.03:02 PM]$ ./election_results.py
****************************Results for Cardiff West****************************
Conservative Party votes: 11014
Labour Party votes: 17803
UKIP votes: 4923
Liberal Democrats votes: 2069
Green Party votes: 0
Independent votes: 0
SNP votes: 0
Total votes for Cardiff West: 35809
*********************Results for Islington South & Finsbury*********************
Conservative Party votes: 9389
Labour Party votes: 22547
UKIP votes: 3375
Liberal Democrats votes: 4829
Green Party votes: 3371
Independent votes: 309
SNP votes: 0
Total votes for Islington South & Finsbury: 43820
*********************************Final Results**********************************
Total votes in election: 79629
Percentages of total votes, by constituency:
Cardiff West: 44%
Islington South & Finsbury: 55%
```
