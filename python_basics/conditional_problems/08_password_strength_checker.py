# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 char (Strong).

password = input("Set a password:\t")
pass_len = len(password)

if pass_len < 6: print("Strength: Weak")
elif pass_len <= 10: print("Strength: Medium")
elif pass_len > 10: print("Strength: Strong")