def eye_ai():
    print("👁️ Eye AI Assistant")
    
    redness = input("Do you have redness? (yes/no): ")
    pain = input("Do you have eye pain? (yes/no): ")
    dryness = input("Do you feel dryness? (yes/no): ")
    blurred = input("Do you have blurred vision? (yes/no): ")

    if redness == "yes" and pain == "yes":
        print("Possible condition: Eye Infection or Conjunctivitis")
    elif dryness == "yes":
        print("Possible condition: Dry Eye Syndrome (MGD possible)")
    elif blurred == "yes":
        print("Possible condition: Vision issue (check doctor)")
    else:
        print("No major issue detected, but consult doctor if needed")

eye_ai()
