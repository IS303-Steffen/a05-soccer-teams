max_score = 25  # This value is pulled by yml_generator.py to assign a score to this test.
from conftest import normalize_text, load_student_code, format_error_message, exception_message_for_students

# Checks if a correct dictionary is created given certain inputs
def test_5_storing_win_and_loss_teams(test_cases):
    try:
        # Ensure test_cases is valid and iterable
        if not isinstance(test_cases, list):
            raise ValueError("test_cases should be a list of dictionaries. Contact your professor.")

        for test_case in test_cases:
            try:
                inputs = test_case["inputs"]
                # This provides a dictionary of dictionaries. Each key is a variable name,
                # the value is the actual dictionary we care about.

                expected_team_names = ["UVU", "Utah State", "UNLV", "TCU", "University of Utah"]
                expected_team_names = [normalize_text(name) for name in expected_team_names]

                # Load in the student's code and get globals
                _, _, student_globals = load_student_code(inputs, test_case)
                
                # Get the locals from 'main' function if it exists
                student_locals = student_globals.get('__main_locals__', {})

                # Find all variables in student's code that are of type dictionary
                student_dictionaries = {name: value for name, value in student_globals.items() if isinstance(value, dict) and name != "__builtins__" and name != "__main_locals__"}

                # Also include dictionaries from student_locals
                student_dictionaries.update({name: value for name, value in student_locals.items() if isinstance(value, dict)})

                # Assert that there is at least one dictionary
                assert student_dictionaries, (format_error_message(
                        custom_message=(
                            f"No dictionaries were found in your code. You must store the teams that your home team "
                            f"won against or lost against in a dictionary. See the README.md instructions.\n\n"),
                        test_case=test_case,
                        display_inputs=True
                    ))

                for _, student_dictionary in student_dictionaries.items():
                    won_against_list = student_dictionary.get("Won Against", None)
                    lost_against_list = student_dictionary.get("Lost Against", None)

                    if isinstance(won_against_list, list) and isinstance(lost_against_list, list):
                        break
                
                assert isinstance(won_against_list, list) and isinstance(lost_against_list, list), format_error_message(
                    custom_message=(
                        f"No dictionary in your code fulfilled all the following requirements:\n\n"
                        f"\t- Had a key called \"Won Against\" with a list for a value\n"
                        f"\t- Had a key called \"Lost Against\" with a list for a value\n\n"
                        f"Double check your spelling and make sure you are using a dictionary. "
                        f"Your code contained the following dictionaries:\n\n"
                        f"{student_dictionaries}\n\n"),
                    test_case=test_case,
                    display_inputs=True
                )

                won_against_list = [normalize_text(team_name) for team_name in won_against_list]
                lost_against_list = [normalize_text(team_name) for team_name in lost_against_list]

                team_name_in_list = True

                for team_name in expected_team_names:
                    if not(team_name in won_against_list or team_name in lost_against_list):
                        team_name_in_list = False
                        break

                assert team_name_in_list, format_error_message(
                    custom_message=(
                        f"The opposing team:\n\n"
                        f"{team_name}\n\n"
                        f"wasn't found in the \"Won Against\" list nor the \"Lost Against\" list.\n\n"
                        f"Here is your \"Won Against\" list (ignoring capitalization / punctuation):\n\n"
                        f"{won_against_list}\n\n"
                        f"Here is your \"Lost Against\" list (ignoring capitalization / punctuation):\n\n"
                        f"{lost_against_list}\n\n"
                        f"Here are all the dictionaries in your code:\n\n"
                        f"{student_dictionaries}\n\n"
                        f"Make sure you are correctly adding values to your lists in the dictionaries when they win or lose, "
                        f"or that you aren't transforming the team names in an unexpected way.\n"),
                    test_case=test_case,
                    display_inputs=True
                )
            # assert raises an AssertionError, but I don't want to actually catch it
            # this is just so I can have another Exception catch below it in case
            # anything else goes wrong.
            except AssertionError:
                raise
            
            except Exception as e:
                # Handle other exceptions
                exception_message_for_students(e, test_case)
    
    # the first AssertionError raises the problem here, this raises it to the main level so the test will stop
    except AssertionError:
        raise

    except Exception as outer_e:
        # Catches any problem in grabbing the test cases
        test_case = {"id_test_case": None}
        exception_message_for_students(outer_e, test_case=test_case) 