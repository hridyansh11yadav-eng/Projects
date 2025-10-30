def shutdown():
    choice = input("Type 'yes' to shut down: ").lower()
    if choice == 'yes':
        print("System shutting down...")
    else:
        print("Shutdown cancelled.")

shutdown()
