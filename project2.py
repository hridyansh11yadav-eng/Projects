def shutdown():
    answer = input("Do you want to shut down? (yes/no): ")
    if answer == "yes":
        print("Shutting down...")
    else:
        print("Cancelled.")

shutdown()
