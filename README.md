I wanted to do some research in the cybersecurity domain that piqued my interest. I decided to test what XSS strings in the FuzzDB and SecLists lists bypassed mod_security OWASP ruleset on a standard Apache2 web server. 

I combined all separate XSS lists within FuzzDB as well as SecLists. I then proceeded to run these on the login parameter of a quick PHP login script I acquired for testing.

As you can see from the preceding Python code, I would print out the string that received a 200 response code from the Apache2 server. This shows that the string is not being filtered by the WAF and thus not receiving a 403 Forbidden response from the server.
