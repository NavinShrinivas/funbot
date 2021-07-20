import os

retval=os.system("bash update.sh")
if retval=="0":
    print("No diff to update or merge.")
else:
    print("Changes present , Updating...Will notify once done!")