# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
# use key as their names. Assume that the names are unique.
# a.items(): Returns a list of (key,value) tuples.
# a.keys(): Returns a list containing dictionary's keys.
# a.update({"friends":}): Updates the dictionary with supplied key-value pairs.
# a.get("name"): Returns the value of the specified keys.

sub = {"Ashwed":"" , "Umesh": "","Shubham":"","Atharva":"" }

sub.update({"Ashwed":input("Ashwed Enter your Fav sub ")})
sub.update({"Umesh":input("Umesh Enter your Fav sub ")})
sub.update({"Shubham":input("Shubham Enter your Fav sub ")})
sub.update({"Atharva":input("Atharva Enter your Fav sub ")})

print(sub)

