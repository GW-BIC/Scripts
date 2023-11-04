# Scripts

Here are scripts that we have developed that could be deployed for general use

1. 🐍 txtHighlight - This script crawls a directory (you can remove the nesting if you don't need it), generates HTML files from txt files found, and applies user-defined HTML style formatting to a list of words. We developed this to assist clinicians during patient chart review: it highlights keywords making identifying relevant notes easier.
2. 🐍 rxnorm_namer - This script accepts a csv of drug names, and returns a csv file with the RxNorm Ingredients for the drug. We developed this to standarize drug names in a table that contained mixed generic and brand-name drugs. The output may requirs more cleaning dependent on your needs. 
3. 🧮 PackingIntervals - This is a SQL query that takes in a table with (at least) unique patient/user identifiers and start/end datetimes. It then checks for overlap between intervals (with allowances for a set grace period), and combines these intervals.
4. 📓 ChatGPT4API - This is an example notebook for getting started using the center's OpenAI API
