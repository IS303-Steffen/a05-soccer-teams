max_score = 25  # This value is pulled by yml_generator.py to assign a score to this test.
from conftest import (
    normalize_text,
    load_student_code,
    format_error_message,
    exception_message_for_students,
    round_match,
    get_similarity_feedback,
    clear_database,
    pc_get_or_create,
    pc_finalize_and_maybe_fail,
    default_module_to_test
)
import re

# Checks if a correct dictionary is created given certain inputs
def test_05_storing_win_and_loss_teams(current_test_name, input_test_cases):
    rec = pc_get_or_create(current_test_name, max_score)
    try:
        # Ensure test_cases is valid and iterable
        if not isinstance(input_test_cases, list):
            input_test_case = {"id_input_test_case": None}
            exception_message_for_students(ValueError("input_test_cases should be a list of dictionaries. Contact your professor."), input_test_case, current_test_name) 
            return  # Technically not needed, as exception_message_for_students throws a pytest.fail Error, but included for clarity that this ends the test.

        for input_test_case in input_test_cases:
            case_id = input_test_case["id_input_test_case"]
            inputs = input_test_case["inputs"]
            # This provides a dictionary of dictionaries. Each key is a variable name,
            # the value is the actual dictionary we care about.

            expected_team_names = ["UVU", "Utah State", "UNLV", "TCU", "University of Utah"]
            expected_team_names = [normalize_text(name) for name in expected_team_names]

            # Load in the student's code and get globals
            manager_payload = load_student_code(current_test_name, inputs, input_test_case, default_module_to_test)
            
            if not manager_payload:
                continue # if there was an error in running student code, it's already been logged. Just skip to the next test case.

            student_variables = manager_payload.get('all_variables', {})

            # Find all variables in student's code that are of type dictionary
            student_dictionaries = {name: value for name, value in student_variables.items() if isinstance(value, dict) and name != "__builtins__" and name != "__main_locals__" and value}

            case_failed_messages = []

            # Assert that there is at least one dictionary
            if not student_dictionaries: 
                formatted = format_error_message(
                    custom_message=(
                        f"No dictionaries were found in your code. You must store the teams that your home team "
                        f"won against or lost against in a dictionary. See the README.md instructions.\n\n"),
                    current_test_name=current_test_name,
                    input_test_case=input_test_case,
                    display_inputs=True
                    )
                case_failed_messages.append(formatted)
                break
            
            student_dictionaries_string = ''  # Used to provide details if the test fails
            
            for dict_name, student_dictionary in student_dictionaries.items():
                dict_name = dict_name.rpartition(".")[-1]    
                student_dictionaries_string += f"{dict_name}: {student_dictionary}\n\n"
                won_against_list = student_dictionary.get("Won Against", None)
                lost_against_list = student_dictionary.get("Lost Against", None)

                if isinstance(won_against_list, list) and isinstance(lost_against_list, list):
                    break
            
            student_dictionaries_string = student_dictionaries_string.strip()

            if not isinstance(won_against_list, list) or not isinstance(lost_against_list, list):
                formatted = format_error_message(
                    custom_message=(
                        f"No dictionary in your code fulfilled all the following requirements:\n\n"
                        f"- `Had a key called \"Won Against\" with a list for a value`\n"
                        f"- `Had a key called \"Lost Against\" with a list for a value`\n\n"
                        f"Double check your spelling and make sure you are using a dictionary. "
                        f"Your code contained the following dictionaries:\n"
                        f"```\n{student_dictionaries_string}\n```\n"),
                    current_test_name=current_test_name,
                    input_test_case=input_test_case,
                    display_inputs=True
                    )
                case_failed_messages.append(formatted)
                break

            won_against_list = [normalize_text(team_name) for team_name in won_against_list]
            lost_against_list = [normalize_text(team_name) for team_name in lost_against_list]

            team_name_in_list = True

            for team_name in expected_team_names:
                if not(team_name in won_against_list or team_name in lost_against_list):
                    team_name_in_list = False
                    break

            if not team_name_in_list:
                formatted = format_error_message(
                    custom_message=(
                        f"The opposing team:\n"
                        f"```\n{team_name}\n```\n"
                        f"Wasn't found in the \"Won Against\" list nor the \"Lost Against\" list.\n"
                        f"### Your \"Won Against\" list:\n"
                        f"Here is your \"Won Against\" list (ignoring capitalization / punctuation):\n"
                        f"```\n{won_against_list}\n```\n"
                         f"### Your \"Lost Against\" list:\n"
                        f"Here is your \"Lost Against\" list (ignoring capitalization / punctuation):\n"
                        f"```\n{lost_against_list}\n```\n"
                        f"### Your dictionary/ies:\n"
                        f"Here are all the dictionaries in your code:\n"
                        f"```\n{student_dictionaries_string}\n```\n"
                        f"### How to fix it:\n"
                        f"Make sure you are correctly adding values to your lists in the dictionaries when they win or lose, "
                        f"or that you aren't transforming the team names in an unexpected way.\n\n"),
                    current_test_name=current_test_name,
                    input_test_case=input_test_case,
                    display_inputs=True
                    )
                case_failed_messages.append(formatted)
                break

        if case_failed_messages:
            # Join multiple messages (if both a required and invalid check failed)
            full_msg = "\n\n".join(case_failed_messages)
            rec.fail_case(case_id, custom_message=full_msg)
        else:
            rec.pass_case(case_id)

    # assert raises an AssertionError, but I don't want to actually catch it
    # this is just so I can have another Exception catch below it in case
    # anything else goes wrong.
    except AssertionError:
        raise
    
    except Exception as e:
        # Handle other exceptions
        exception_message_for_students(e, input_test_case, current_test_name)

    finally:
        # After all cases, emit a one-line summary or a short failure directing to the MD file
        pc_finalize_and_maybe_fail(rec)