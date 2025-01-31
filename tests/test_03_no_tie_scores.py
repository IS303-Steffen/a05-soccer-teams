max_score = 25  # This value is pulled by yml_generator.py to assign a score to this test.
from conftest import normalize_text, load_student_code, format_error_message, exception_message_for_students
import re

# Checks if the expected printed messages actually appear, but doesn't check for specific inputs or correct calculations.
def test_03_no_tie_scores(current_test_name, input_test_cases):
    try:
        if not isinstance(input_test_cases, list):
            input_test_case = {"id_input_test_case": None}
            exception_message_for_students(ValueError("input_test_cases should be a list of dictionaries. Contact your professor."), input_test_case=input_test_case) 
            return  # Technically not needed, as exception_message_for_students throws a pytest.fail Error, but included for clarity that this ends the test.

        combined_normalized_printed = ''

        # Loop through each test case
        for input_test_case in input_test_cases:
            
            # Grab the necessary data from the test case dictionary
            inputs = input_test_case["inputs"]
            #expected_printed_messages = test_case["printed_messages"]
            #invalid_printed_messages = test_case["invalid_printed_messages"]
            
            # case_no_ties = False
            # case_ties = False
            matching_numbers_found = False

            num_repeat_iterations = 50

            # repeat test case 50 times, should have a 99.9999% chance of finding a tie score if it exists.
            for _ in range(num_repeat_iterations):
                # Load in the student's code and capture output
                manager_payload = load_student_code(current_test_name, inputs, input_test_case)

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
                    break
                    
            assert not matching_numbers_found, format_error_message(
                custom_message=(f"Your code doesn't prevent tie scores for the home and away teams.\n\n"
                                f"These scores were generated during your code:.\n\n"
                                f"{line}\n\n"
                                f"Make sure you either continue generating the scores when there is a tie until "
                                f"there is no longer a tie, or you find a way to never generate tie scores to begin with.\n"),
                current_test_name=current_test_name,
                input_test_case=input_test_case,
                display_inputs=True,
            )
    
    # assert raises an AssertionError, but I don't want to actually catch it
    # this is just so I can have another Exception catch below it in case
    # anything else goes wrong.
    except AssertionError:
        raise

    except Exception as e:
        # Handle other exceptions
        exception_message_for_students(e, input_test_case)