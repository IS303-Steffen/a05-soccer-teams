max_score = 15  # This value is pulled by yml_generator.py to assign a score to this test.
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
def test_04_correct_range_random_scores(current_test_name, input_test_cases):
    rec = pc_get_or_create(current_test_name, max_score)
    try:
        # Ensure test_cases is valid and iterable
        if not isinstance(input_test_cases, list):
            input_test_case = {"id_input_test_case": None}
            exception_message_for_students(ValueError("input_test_cases should be a list of dictionaries. Contact your professor."), input_test_case, current_test_name) 
            return  # Technically not needed, as exception_message_for_students throws a pytest.fail Error, but included for clarity that this ends the test.

        # Loop through each test case
        for input_test_case in input_test_cases:
            case_id = input_test_case["id_input_test_case"]
            # Grab the necessary data from the test case dictionary
            inputs = input_test_case["inputs"]
          
            all_score_values_found = False

            num_repeat_iterations = 15
            valid_score_values = {0, 1, 2, 3}
            found_number_values = set()
            case_failed_messages = []  # collect case's failure messages (exactly as before)
            # repeat test case 30 times, should have a 99.9999% chance of finding a tie score if it exists.
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
                    if 'record' in line.lower():
                        continue

                    found_numbers_strings = re.findall(r'\d+', line)

                    if found_numbers_strings:
                        # Convert found numbers to integers
                        found_numbers_ints = [int(num) for num in found_numbers_strings]

                        found_number_values.update(found_numbers_ints)
                        
            if found_number_values == valid_score_values:
                all_score_values_found = True
                break
                

        # Normalize the captured output to remove spaces, punctuation, and symbols
        normalized_captured_print_statements = [normalize_text(captured_print) for captured_print in captured_lines]
        normalized_captured_print_statements = '\n'.join(normalized_captured_print_statements)
                
        if not all_score_values_found:
            formatted = format_error_message(
                custom_message=(f"Your code isn't generating random scores in the correct range. Across 5 games * {num_repeat_iterations} "
                                f"iterations, your code generated these values for scores:\n"
                                f"```\n{found_number_values}\n```\n"
                                f"Your code should only be capable of generating these values (no more, no less):\n"
                                f"```\n{valid_score_values}\n```\n"
                                f"Double check that you are using the correct arguments in your random function to produce the correct range of values. "
                                f"Make sure you also aren't printing out any other lines with numbers in them that weren't specified in the assignment instructions\n"
                                f"### All your printed output:\n"
                                f"Below are all the printed messages from the most recent test run of your code (ignoring punctuation / capitalization):\n"
                                f"```\n{normalized_captured_print_statements}\n```\n"),
                current_test_name=current_test_name,
                input_test_case=input_test_case,
                display_inputs=True,
            )
            case_failed_messages.append(formatted)

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