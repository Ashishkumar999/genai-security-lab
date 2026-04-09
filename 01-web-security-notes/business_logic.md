# Business Logic Vulnerabilities

Business logic flaws occur when application workflow rules are bypassed.

Examples:

- Apply coupon multiple times
- Change product price in request
- Skip payment step
- Reuse expired tokens
- Bypass OTP verification

Testing approach:

Intercept requests using Burp Suite
Modify parameters
Replay workflow steps
Observe server behavior
