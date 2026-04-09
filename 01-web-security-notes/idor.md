# IDOR Testing Notes

IDOR = Insecure Direct Object Reference

Test cases:

- Change user_id parameter
- Modify object reference
- Replace numeric IDs with another user ID
- Try UUID replacement
- Access another user's order history
- Access another user's invoice

Impact:

Unauthorized data access between users
