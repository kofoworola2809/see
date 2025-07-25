admins = {"Dedans", "Chakin"}
editors = {"Chakin", "Aaron"}

# Combine both groups
all_users = admins.union(editors)
print("All Users", all_users)

# who is both admin and editor ?
both_roles = admins.intersection(editors)
print("users with both roles", both_roles)

# who is admins only
admin_only = admins.difference(editors)
print("Admin only", admin_only)

editors_only = editors.difference(admins)
print("Editors only", editors_only)