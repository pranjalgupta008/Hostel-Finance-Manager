# ============================================
# HOSTEL FINANCE MANAGER
# Student Profile Module
# ============================================

import json
import os


DATA_FOLDER = "data"
PROFILE_FILE = os.path.join(
    DATA_FOLDER,
    "student.json"
)


def initialize_profile_file():
    """Create the profile file if it does not exist."""

    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    if not os.path.exists(PROFILE_FILE):

        with open(
            PROFILE_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump({}, file, indent=4)


def load_profile():
    """Load the student profile."""

    initialize_profile_file()

    with open(
        PROFILE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_profile(profile):
    """Save the student profile."""

    initialize_profile_file()

    with open(
        PROFILE_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            profile,
            file,
            indent=4
        )


def create_or_update_profile():
    """Create or update student profile."""

    print()
    print("=" * 55)
    print("             STUDENT PROFILE")
    print("=" * 55)

    print()
    print("Enter your details below.")
    print("You can update them later.")

    # -----------------------------------------
    # Name
    # -----------------------------------------

    while True:

        name = input(
            "Name: "
        ).strip()

        if name:
            break

        print("❌ Name cannot be empty.")


    # -----------------------------------------
    # College
    # -----------------------------------------

    while True:

        college = input(
            "College: "
        ).strip()

        if college:
            break

        print("❌ College name cannot be empty.")


    # -----------------------------------------
    # Course
    # -----------------------------------------

    while True:

        course = input(
            "Course: "
        ).strip()

        if course:
            break

        print("❌ Course cannot be empty.")


    # -----------------------------------------
    # Year
    # -----------------------------------------

    while True:

        year = input(
            "Year of study: "
        ).strip()

        if year.isdigit():

            year = int(year)

            if 1 <= year <= 6:
                break

        print(
            "❌ Please enter a valid year "
            "(1-6)."
        )


    # -----------------------------------------
    # Hostel
    # -----------------------------------------

    while True:

        hostel = input(
            "Hostel name: "
        ).strip()

        if hostel:
            break

        print("❌ Hostel name cannot be empty.")


    # -----------------------------------------
    # Room
    # -----------------------------------------

    while True:

        room = input(
            "Room number: "
        ).strip()

        if room:
            break

        print("❌ Room number cannot be empty.")


    # -----------------------------------------
    # Monthly allowance
    # -----------------------------------------

    while True:

        allowance_input = input(
            "Monthly allowance/budget: ₹"
        ).strip()

        try:

            allowance = float(
                allowance_input
            )

            if allowance >= 0:
                break

            print(
                "❌ Amount cannot be negative."
            )

        except ValueError:

            print(
                "❌ Please enter a valid number."
            )


    # -----------------------------------------
    # Create profile
    # -----------------------------------------

    profile = {
        "name": name,
        "college": college,
        "course": course,
        "year": year,
        "hostel": hostel,
        "room": room,
        "monthly_allowance": allowance
    }


    # Save profile
    save_profile(profile)


    # -----------------------------------------
    # Confirmation
    # -----------------------------------------

    print()
    print("=" * 55)
    print("          PROFILE SAVED SUCCESSFULLY")
    print("=" * 55)

    print(f"Name              : {name}")
    print(f"College            : {college}")
    print(f"Course             : {course}")
    print(f"Year               : {year}")
    print(f"Hostel             : {hostel}")
    print(f"Room               : {room}")
    print(f"Monthly Allowance  : ₹{allowance:.2f}")

    print("=" * 55)


def view_profile():
    """Display the saved student profile."""

    profile = load_profile()


    # Check whether profile exists
    if not profile:

        print()
        print("=" * 55)
        print("             STUDENT PROFILE")
        print("=" * 55)

        print()
        print("No student profile has been created yet.")

        print("=" * 55)

        return


    print()
    print("=" * 55)
    print("             STUDENT PROFILE")
    print("=" * 55)

    print()

    print(f"Name              : {profile['name']}")
    print(f"College            : {profile['college']}")
    print(f"Course             : {profile['course']}")
    print(f"Year               : {profile['year']}")
    print(f"Hostel             : {profile['hostel']}")
    print(f"Room               : {profile['room']}")
    print(
        f"Monthly Allowance  : "
        f"₹{float(profile['monthly_allowance']):.2f}"
    )

    print()
    print("=" * 55)


def profile_menu():
    """Display the student profile menu."""

    while True:

        print()
        print("=" * 55)
        print("             PROFILE MANAGEMENT")
        print("=" * 55)

        print("1. Create / Update Profile")
        print("2. View Profile")
        print("3. Back to Main Menu")

        print()

        choice = input(
            "Enter your choice: "
        ).strip()


        if choice == "1":

            create_or_update_profile()


        elif choice == "2":

            view_profile()


        elif choice == "3":

            break


        else:

            print(
                "❌ Invalid choice. "
                "Please select 1, 2 or 3."
            )