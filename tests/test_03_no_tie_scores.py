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

# Checks if the expected printed messages actually appear, but doesn't check for specific inputs or correct calculations.
def test_03_no_tie_scores(current_test_name, input_test_cases):
    rec = pc_get_or_create(current_test_name, max_score)
    try:
        if not isinstance(input_test_cases, list):
            input_test_case = {"id_input_test_case": None}
            exception_message_for_students(ValueError("input_test_cases should be a list of dictionaries. Contact your professor."), input_test_case=input_test_case) 
            return  # Technically not needed, as exception_message_for_students throws a pytest.fail Error, but included for clarity that this ends the test.

        # Loop through each test case
        for input_test_case in input_test_cases:
            case_id = input_test_case["id_input_test_case"]
            # Grab the necessary data from the test case dictionary
            inputs = input_test_case["inputs"]
            #expected_printed_messages = test_case["printed_messages"]
            #invalid_printed_messages = test_case["invalid_printed_messages"]
            
            # case_no_ties = False
            # case_ties = False
            matching_numbers_found = False

            num_repeat_iterations = 15
            case_failed_messages = []  # collect case's failure messages (exactly as before)

            # repeat test case 50 times, should have a 99.9999% chance of finding a tie score if it exists.
            for _ in range(num_repeat_iterations):
                # Load in the student's code and capture output
                manager_payload = load_student_code(current_test_name, inputs, input_test_case, default_module_to_test)
            
                if not manager_payload:
                    continue # if there was an error in running student code, it's already been logged. Just skip to the next test case.

                captured_output = manager_payload.get('captured_output')

                # Split the captured output into lines
                captured_lines = captured_output.splitlines()
                
                # first catch if they ever print out actual tie scores:
                for line in captured_lines:

                    # ignore the line that has the final season record
                    if 'record' in line:
                        continue

                    numbers = re.findall(r'\d+', line)

                    # Convert found numbers to integers
                    numbers = [int(num) for num in numbers]

                    # Check if there are at least 2 numbers and if any two numbers are the same by getting rid of duplicates in a set
                    if len(numbers) > 1 and len(numbers) != len(set(numbers)):
                        matching_numbers_found = True
                        break
                if matching_numbers_found:
                    formatted = format_error_message(
                        custom_message=(f"Your code doesn't prevent tie scores for the home and away teams.\n\n"
                                        f"These scores were generated during your code:.\n"
                                        f"```\n{line}\n```\n"
                                        f"Make sure you either continue generating the scores when there is a tie until "
                                        f"there is no longer a tie, or you find a way to never generate tie scores to begin with. "
                                        f"Or, make sure you aren't printing any extra lines of code that have 2 numbers in them.\n"),
                        current_test_name=current_test_name,
                        input_test_case=input_test_case,
                        display_inputs=True,
                    )
                    case_failed_messages.append(formatted)
                    break
            # Record the case result for partial credit
            if case_failed_messages:
                # Join multiple messages (if both a required and invalid check failed)
                full_msg = "\n\n".join(case_failed_messages)
                rec.fail_case(case_id, reason="printed message mismatch", custom_message=full_msg)
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
